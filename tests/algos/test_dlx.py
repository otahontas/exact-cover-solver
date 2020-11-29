"""Unit tests for dlx implementation of algo X."""
import pytest

from exact_cover_solver.algos.dlx import DLX
from exact_cover_solver.datastructures.dictmatrix import DictMatrix
from exact_cover_solver.datastructures.dlxmatrix import DLXMatrix


@pytest.fixture
def universe():
    return [num for num in range(1, 8)]


@pytest.fixture
def collection_with_single_solution():
    return [[1, 4, 7], [1, 4], [4, 5, 7], [3, 5, 6], [2, 3, 6, 7], [2, 7]]


@pytest.fixture
def collection_without_solution():
    return [[1, 6, 7], [2, 6, 7], [3, 6, 7], [4, 6, 7]]


@pytest.fixture
def collection_with_multiple_solutions():
    return [
        [4, 7],
        [3],
        [2, 6],
        [1, 3, 5],
        [1, 4, 5, 7],
        [1, 2, 4, 5, 6, 7],
    ]


def calc_node_amount(changed_matrix):
    tmp_amount = 0
    column = changed_matrix.right
    while column != changed_matrix:
        tmp_amount += column.size
        column = column.right
    return tmp_amount


def test_correct_single_solution_is_found(universe, collection_with_single_solution):
    constrains = (universe, collection_with_single_solution)
    matrix = DLXMatrix(constrains)
    dlx = DLX()
    solutions = dlx.solve(matrix)
    assert len(solutions) == 1
    assert 1 and 3 and 5 in solutions[0]


def test_no_solution_is_found_with_unsolvable_collection(
    universe, collection_without_solution
):
    constrains = (universe, collection_without_solution)
    matrix = DLXMatrix(constrains)
    dlx = DLX()
    solutions = dlx.solve(matrix)
    assert not solutions


def test_all_solutions_are_found_with_multiple_solutions(
    universe, collection_with_multiple_solutions
):
    constrains = (universe, collection_with_multiple_solutions)
    matrix = DLXMatrix(constrains)
    dlx = DLX()
    solutions = dlx.solve(matrix)
    assert len(solutions) == 3


def test_optimal_column_is_chosen(universe, collection_with_single_solution):
    constrains = (universe, collection_with_single_solution)
    matrix = DLXMatrix(constrains)
    dlx = DLX()
    chosen_column = dlx._choose_optimal_column_object(matrix)
    assert chosen_column.id == 1


def test_covering_detaches_correct_amount_of_nodes(
    universe, collection_with_single_solution
):
    constrains = (universe, collection_with_single_solution)
    matrix = DLXMatrix(constrains)
    dlx = DLX()

    amount = calc_node_amount(matrix)
    assert amount == 17
    dlx._cover(matrix.right)
    amount = calc_node_amount(matrix)
    assert amount == 12


def test_uncovering_restores_correct_nodes(universe, collection_with_single_solution):
    constrains = (universe, collection_with_single_solution)
    matrix = DLXMatrix(constrains)
    dlx = DLX()
    column = matrix.right

    original_amount = calc_node_amount(matrix)

    dlx._cover(column)
    amount_after_cover = calc_node_amount(matrix)
    assert amount_after_cover != original_amount

    dlx._uncover(column)
    amount_after_uncover = calc_node_amount(matrix)
    assert amount_after_uncover == original_amount


def test_solve_errors_when_trying_to_give_wrong_matrix():
    dlx = DLX()
    with pytest.raises(ValueError):
        dlx.solve(DictMatrix)
