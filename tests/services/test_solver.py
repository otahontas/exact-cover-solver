import pytest

from exact_cover_solver.services.pentomino_browser import PentominoBoardBrowser
from exact_cover_solver.services.solver import Solver, AlgorithmNotChosenError
from exact_cover_solver.algos import DLX, DictX
from unittest.mock import Mock


@pytest.fixture
def solver():
    return Solver()


@pytest.fixture
def solver_method_and_params(request):
    method_name, *params = request.param
    method = getattr(Solver(), method_name)
    print(params)
    return method, params


@pytest.fixture
def algo_names():
    return ["DLX", "DictX"]


def test_wrong_algorithm_name_is_not_allowed(solver):
    with pytest.raises(ValueError):
        solver.algorithm = "WrongAlgo"


def test_no_algorithm_name_is_returned_after_initialization(solver):
    assert solver._algorithm is None
    with pytest.raises(AlgorithmNotChosenError):
        assert solver.algorithm


def test_all_algo_names_are_returned_in_error_message(solver, algo_names):
    with pytest.raises(ValueError) as error:
        solver.algorithm = "WrongAlgo"
        for algo_name in algo_names:
            assert algo_name in error


@pytest.mark.parametrize("algo_name, algo_class", [("DLX", DLX), ("DictX", DictX)])
def test_correct_algo_name_sets_correct_algo_class(algo_name, algo_class, solver):
    solver.algorithm = algo_name
    assert isinstance(solver._algorithm, algo_class)


@pytest.mark.parametrize("algo_name, algo_class", [("DLX", DLX), ("DictX", DictX)])
def test_correct_algo_name_is_returned_after_setting_instance(
    algo_name, algo_class, solver
):
    solver._algorithm = algo_class()
    assert solver.algorithm == algo_name


@pytest.mark.parametrize(
    "solver_method_and_params",
    [
        ("solve_pentomino_problem", 3, 20),
        ("solve_generic_problem", "", ""),
    ],
    indirect=True,
)
def test_certain_methods_fail_if_board_size_not_set(solver_method_and_params):
    """Test error is raised when calling different methods too early."""
    method, params = solver_method_and_params
    with pytest.raises(AlgorithmNotChosenError):
        if params is not None:
            method(*params)
        else:
            method()


def test_pentomino_problem_call_returns_solution_browser(solver):
    """Mock solver to return preset solutions, so heavy solving process won't run."""
    solver._algorithm = Mock()
    solver._algorithm.solve.return_value = [
        [183, 163, 411, 729, 916, 398, 829, 247, 577, 1115, 71, 1029],
        [183, 163, 675, 443, 1038, 988, 537, 247, 869, 337, 53, 908],
        [198, 162, 420, 668, 903, 332, 864, 242, 532, 1033, 18, 983],
        [198, 162, 614, 452, 1110, 1024, 572, 242, 824, 393, 0, 911],
    ]
    solver._matrices = {"Mock": Mock()}
    browser = solver.solve_pentomino_problem(3, 20)
    assert isinstance(browser, PentominoBoardBrowser)
    assert "1" and "4" in browser.current_status
    assert solver._algorithm.solve.call_count == 1


def test_generic_problem_returns_solution_formatted(solver):
    """Mock solver to return preset solutions, so solving process won't run."""
    solver._algorithm = Mock()
    solver._algorithm.solve.return_value = [[1, 2, 3], [4, 5, 6]]
    solver._matrices = {"Mock": Mock()}
    solution = solver.solve_generic_problem("1", "1")
    assert all(element in solution for element in ["1", "2", "3", "4", "5", "6"])
    assert solver._algorithm.solve.call_count == 1


def test_empty_solutions_are_reported(solver):
    solver._algorithm = Mock()
    solver._algorithm.solve.return_value = []
    solver._matrices = {"Mock": Mock()}
    solution = solver.solve_generic_problem("1", "1")
    assert "No solutions" in solution
    assert solver._algorithm.solve.call_count == 1
