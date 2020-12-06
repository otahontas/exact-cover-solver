"""Unit tests for dlx implementation of algo X."""
import pytest

from exact_cover_solver.algos import DLX, DictX
from exact_cover_solver.datastructures.dlxmatrix import DLXMatrix
from exact_cover_solver.datastructures.dictmatrix import DictMatrix


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


def calc_dlx_node_amount(changed_matrix):
    """Calculate nodes in dlx matrix, helper function for tests."""
    tmp_amount = 0
    column = changed_matrix.right
    while column != changed_matrix:
        tmp_amount += column.size
        column = column.right
    return tmp_amount


@pytest.mark.parametrize(
    "algo_class, matrix_class", [(DLX, DLXMatrix), (DictX, DictMatrix)]
)
def test_correct_single_solution_is_found(
    algo_class, matrix_class, universe, collection_with_single_solution
):
    constrains = (universe, collection_with_single_solution)
    matrix = matrix_class(constrains)
    algo = algo_class()
    solutions = algo.solve(matrix)
    assert len(solutions) == 1
    assert 1 and 3 and 5 in solutions[0]


@pytest.mark.parametrize(
    "algo_class, matrix_class", [(DLX, DLXMatrix), (DictX, DictMatrix)]
)
def test_no_solution_is_found_with_unsolvable_collection(
    algo_class, matrix_class, universe, collection_without_solution
):
    constrains = (universe, collection_without_solution)
    matrix = matrix_class(constrains)
    algo = algo_class()
    solutions = algo.solve(matrix)
    assert not solutions


@pytest.mark.parametrize(
    "algo_class, matrix_class", [(DLX, DLXMatrix), (DictX, DictMatrix)]
)
def test_all_solutions_are_found_with_multiple_solutions(
    algo_class, matrix_class, universe, collection_with_multiple_solutions
):
    constrains = (universe, collection_with_multiple_solutions)
    matrix = matrix_class(constrains)
    algo = algo_class()
    solutions = algo.solve(matrix)
    assert len(solutions) == 3


def test_optimal_column_is_chosen_in_dlx(universe, collection_with_single_solution):
    constrains = (universe, collection_with_single_solution)
    matrix = DLXMatrix(constrains)
    dlx = DLX()
    chosen_column = dlx._choose_optimal_column_object(matrix)
    assert chosen_column.id == 1


def test_optimal_column_is_chosen_in_dict_x(universe, collection_with_single_solution):
    constrains = (universe, collection_with_single_solution)
    matrix = DictMatrix(constrains)
    dict_x = DictX()
    column_dict, _ = matrix.data
    chosen_column = dict_x._choose_optimal_column(column_dict)
    assert chosen_column == 1


def test_covering_detaches_correct_amount_of_nodes_in_dlx(
    universe, collection_with_single_solution
):
    constrains = (universe, collection_with_single_solution)
    matrix = DLXMatrix(constrains)
    dlx = DLX()

    original_amount = calc_dlx_node_amount(matrix)
    assert original_amount == 17
    dlx._cover(matrix.right)
    amount_after_cover = calc_dlx_node_amount(matrix)
    assert amount_after_cover == 12


def test_uncovering_restores_correct_nodes_in_dlx(
    universe, collection_with_single_solution
):
    constrains = (universe, collection_with_single_solution)
    matrix = DLXMatrix(constrains)
    dlx = DLX()
    column = matrix.right

    original_amount = calc_dlx_node_amount(matrix)

    dlx._cover(column)
    amount_after_cover = calc_dlx_node_amount(matrix)
    assert amount_after_cover != original_amount

    dlx._uncover(column)
    amount_after_uncover = calc_dlx_node_amount(matrix)
    assert amount_after_uncover == original_amount


def test_covering_detaches_correct_amount_of_nodes_in_dictx(
    universe, collection_with_single_solution
):
    constrains = (universe, collection_with_single_solution)
    matrix = DictMatrix(constrains)
    dict_x = DictX()
    column_dict, set_collection = matrix.data

    original_amount = sum(len(col) for col in column_dict.values())
    assert original_amount == 17
    dict_x._cover(column_dict, set_collection, 0)
    amount_after_cover = sum(len(col) for col in column_dict.values())
    assert amount_after_cover == 3


def test_uncovering_restores_correct_nodes_in_dict_x(
    universe, collection_with_single_solution
):
    constrains = (universe, collection_with_single_solution)
    matrix = DictMatrix(constrains)
    dict_x = DictX()
    column_dict, set_collection = matrix.data

    original_amount = sum(len(col) for col in column_dict.values())

    removed_columns = dict_x._cover(column_dict, set_collection, 1)
    amount_after_cover = sum(len(col) for col in column_dict.values())
    assert amount_after_cover != original_amount

    dict_x._uncover(column_dict, set_collection, 1, removed_columns)
    amount_after_uncover = sum(len(col) for col in column_dict.values())
    assert amount_after_uncover == original_amount


@pytest.mark.parametrize(
    "algo_class, matrix_class", [(DLX, DictMatrix), (DictX, DLXMatrix)]
)
def test_solve_errors_when_trying_to_give_wrong_matrix(algo_class, matrix_class):
    algo = algo_class()
    with pytest.raises(ValueError):
        matrix_no_init = object.__new__(matrix_class)
        algo.solve(matrix_no_init)
