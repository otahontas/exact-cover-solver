"""Unit tests for dlx matrix."""
import pytest

from exact_cover_solver.services.solver import Solver, AlgorithmNotChosenError
from exact_cover_solver.algos.dlx import DLX
from exact_cover_solver.algos.dictx import DictX


@pytest.fixture
def solver():
    return Solver()


@pytest.fixture
def algo_names():
    return ["DLX", "DictX"]


@pytest.fixture
def algo_classes():
    return [DLX, DictX]


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


def test_correct_algo_name_sets_correct_algo_class(solver, algo_names, algo_classes):
    names_and_classes = tuple(zip(algo_names, algo_classes))
    for algo_name, algo_class in names_and_classes:
        solver.algorithm = algo_name
        assert isinstance(solver._algorithm, algo_class)
