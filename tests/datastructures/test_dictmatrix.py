import pytest

from exact_cover_solver.datastructures.dictmatrix import DictMatrix


@pytest.fixture
def universe():
    return [num for num in range(1, 8)]


@pytest.fixture
def collection_with_single_solution():
    return [[1, 4, 7], [1, 4], [4, 5, 7], [3, 5, 6], [2, 3, 6, 7], [2, 7]]


def test_matrix_has_correct_columns(universe, collection_with_single_solution):
    constrains = (universe, collection_with_single_solution)
    matrix = DictMatrix(constrains)
    column_dict, _ = matrix.data
    assert matrix is not None
    assert matrix.id == "root"
    assert all(num in column_dict for num in universe)


def test_matrix_has_correct_elements_in_columns(
    universe, collection_with_single_solution
):
    constrains = (universe, collection_with_single_solution)
    matrix = DictMatrix(constrains)
    column_dict, _ = matrix.data
    assert (0 and 1) in column_dict[1]
    assert (4 and 5) in column_dict[2]
    assert (3 and 4) in column_dict[3]
    assert (0 and 1 and 2) in column_dict[4]
    assert (2 and 3) in column_dict[5]
    assert (3 and 4) in column_dict[6]
    assert (0 and 2 and 4 and 5) in column_dict[7]


def test_each_column_in_matrix_has_correct_size(
    universe, collection_with_single_solution
):
    constrains = (universe, collection_with_single_solution)
    matrix = DictMatrix(constrains)
    column_dict, _ = matrix.data
    assert len(column_dict[1]) == 2
    assert len(column_dict[2]) == 2
    assert len(column_dict[3]) == 2
    assert len(column_dict[4]) == 3
    assert len(column_dict[5]) == 2
    assert len(column_dict[6]) == 2
    assert len(column_dict[7]) == 4
