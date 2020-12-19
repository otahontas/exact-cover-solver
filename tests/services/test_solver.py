import pytest

from exact_cover_solver.services.solver import Solver
from unittest.mock import Mock


@pytest.fixture
def solver():
    return Solver()


@pytest.fixture
def algo_names():
    return ["DLX", "DictX"]


def test_wrong_algorithm_name_is_not_allowed(solver):
    with pytest.raises(ValueError):
        solver._solve("WrongAlgo", Mock())


def test_all_algo_names_are_returned_in_error_message(solver, algo_names):
    with pytest.raises(ValueError) as error:
        solver._solve("WrongAlgo", Mock())
        for algo_name in algo_names:
            assert algo_name in error
