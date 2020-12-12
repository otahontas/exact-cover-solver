import pytest

from exact_cover_solver.algos.dlx import DLX
from exact_cover_solver.algos.dictx import DictX
from exact_cover_solver.datastructures.dlxmatrix import DLXMatrix
from exact_cover_solver.datastructures.dictmatrix import DictMatrix

algo_and_matrix_classes = [(DLX, DLXMatrix), (DictX, DictMatrix)]


@pytest.fixture(params=algo_and_matrix_classes)
def algo_and_matrix_class(request):
    return request.param


@pytest.fixture
def problem_data_no_solution(request):
    if request.param == "numbers":
        return (
            [1, 2, 3, 4, 5],
            {1: [1, 2], 2: [3, 4], 3: [5, 1], 4: [2, 3], 5: [4, 5]},
        )
    elif request.param == "strings":
        return (
            ["Make", "Pera", "Mä"],
            {"1st": ["Make", "Pera"], "2nd": ["Pera", "Mä"], "3rd": ["Mä", "Make"]},
        )


@pytest.fixture
def problem_data_with_solution(request):
    if request.param == "single":
        return (
            [1, 2, 3, 4, 5, 6, 7],
            {
                1: [1, 4, 7],
                2: [1, 4],
                3: [4, 5, 7],
                4: [3, 5, 6],
                5: [2, 3, 6, 7],
                6: [2, 7],
            },
        )
    elif request.param == "multiple":
        return (
            [1, 2, 3, 4, 5, 6, 7],
            {
                1: [4, 7],
                2: [3],
                3: [2, 6],
                4: [1, 3, 5],
                5: [1, 4, 5, 7],
                6: [1, 2, 4, 5, 6, 7],
            },
        )


def calc_dlx_node_amount(root):
    """Calculate column size sum from given root, helper function for tests."""
    amount = 0
    column = root.right
    while column != root:
        amount += column.size
        column = column.right
    return amount


@pytest.mark.parametrize(
    "problem_data_with_solution, correct_solutions",
    [("single", [[2, 4, 6]]), ("multiple", [[2, 3, 5], [2, 6], [1, 3, 4]])],
    indirect=["problem_data_with_solution"],
)
def test_correct_solutions_is_found(
    problem_data_with_solution, correct_solutions, algo_and_matrix_class
):
    """Check all algo implementations find correct solutions.

    Solutions are sorted for easy comparison.
    """
    algo_class, matrix_class = algo_and_matrix_class
    matrix = matrix_class(problem_data_with_solution)
    algo = algo_class()
    solutions = algo.solve(matrix)

    sorted_solutions = sorted([sorted(solution) for solution in solutions])
    sorted_correct_solutions = sorted(
        [sorted(solution) for solution in correct_solutions]
    )

    assert sorted_solutions == sorted_correct_solutions


@pytest.mark.parametrize(
    "problem_data_no_solution",
    ["numbers", "strings"],
    indirect=["problem_data_no_solution"],
)
def test_non_valid_solutions_are_not_reported(
    problem_data_no_solution, algo_and_matrix_class
):
    algo_class, matrix_class = algo_and_matrix_class
    matrix = matrix_class(problem_data_no_solution)
    algo = algo_class()
    solutions = algo.solve(matrix)

    assert not solutions


@pytest.mark.parametrize(
    "problem_data_with_solution, correct_column",
    [("single", 1), ("multiple", 2)],
    indirect=["problem_data_with_solution"],
)
def test_optimal_column_is_chosen(
    problem_data_with_solution, correct_column, algo_and_matrix_class
):
    algo_class, matrix_class = algo_and_matrix_class
    matrix = matrix_class(problem_data_with_solution)
    algo = algo_class()
    if isinstance(algo, DLX):
        chosen_column = algo._choose_optimal_column_object(matrix.root)
        assert chosen_column.id == correct_column
    else:
        column_dict, _ = matrix.data
        chosen_column = algo._choose_optimal_column(column_dict)
        assert chosen_column == correct_column


@pytest.mark.parametrize(
    "problem_data_with_solution, original_amount, amount_after_cover_dlx, "
    "amount_after_cover_dict_x",
    [("single", 17, 12, 3), ("multiple", 18, 5, 6)],
    indirect=["problem_data_with_solution"],
)
def test_covering_detaches_correct_amount_of_objects(
    problem_data_with_solution,
    original_amount,
    amount_after_cover_dlx,
    amount_after_cover_dict_x,
    algo_and_matrix_class,
):
    algo_class, matrix_class = algo_and_matrix_class
    matrix = matrix_class(problem_data_with_solution)
    algo = algo_class()
    if isinstance(algo, DLX):
        amount_before = calc_dlx_node_amount(matrix.root)
        algo._cover(matrix.root.right)
        amount_after = calc_dlx_node_amount(matrix.root)

        assert amount_after == amount_after_cover_dlx
    else:
        column_dict, set_collection = matrix.data
        amount_before = sum(len(col) for col in column_dict.values())
        algo._cover(column_dict, set_collection, 1)
        amount_after = sum(len(col) for col in column_dict.values())

        assert amount_after == amount_after_cover_dict_x

    assert amount_before == original_amount


@pytest.mark.parametrize(
    "problem_data_with_solution",
    ["single", "multiple"],
    indirect=["problem_data_with_solution"],
)
def test_uncovering_restores_correct_amount_of_objects(
    problem_data_with_solution, algo_and_matrix_class
):
    algo_class, matrix_class = algo_and_matrix_class
    matrix = matrix_class(problem_data_with_solution)
    algo = algo_class()
    if isinstance(algo, DLX):
        original_amount = calc_dlx_node_amount(matrix.root)
        column = algo._choose_optimal_column_object(matrix.root)

        algo._cover(column)
        amount_after_cover = calc_dlx_node_amount(matrix.root)

        algo._uncover(column)
        amount_after_uncover = calc_dlx_node_amount(matrix.root)
    else:
        column_dict, set_collection = matrix.data
        original_amount = sum(len(col) for col in column_dict.values())
        column = algo._choose_optimal_column(column_dict)

        removed_columns = algo._cover(column_dict, set_collection, column)
        amount_after_cover = sum(len(col) for col in column_dict.values())

        algo._uncover(column_dict, set_collection, column, removed_columns)
        amount_after_uncover = sum(len(col) for col in column_dict.values())

    assert amount_after_cover != original_amount
    assert amount_after_uncover == original_amount
