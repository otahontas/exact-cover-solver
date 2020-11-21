"""Unit tests for dlx matrix."""
import pytest
from exact_cover_solver.datastructures.dlxmatrix import DLXMatrix


@pytest.fixture
def universe():
    return [num for num in range(1, 8)]


@pytest.fixture
def collection_with_single_solution():
    return [[1, 4, 7], [1, 4], [4, 5, 7], [3, 5, 6], [2, 3, 6, 7], [2, 7]]


def test_matrix_columns_are_linked_together_correctly(
    universe, collection_with_single_solution
):
    matrix = DLXMatrix(universe, collection_with_single_solution)
    assert matrix is not None
    assert matrix.id == "root"
    assert matrix.right.id == 1
    assert matrix.left.id == 7


def test_each_column_in_matrix_has_correct_size(
    universe, collection_with_single_solution
):
    matrix = DLXMatrix(universe, collection_with_single_solution)

    column_1 = matrix.right
    assert column_1.size == 2

    column_2 = column_1.right
    assert column_2.size == 2

    column_3 = column_2.right
    assert column_3.size == 2

    column_4 = column_3.right
    assert column_4.size == 3

    column_5 = column_4.right
    assert column_5.size == 2

    column_6 = column_5.right
    assert column_6.size == 2

    column_7 = column_6.right
    assert column_7.size == 4


def test_matrix_is_not_created_when_giving_empty_args():
    with pytest.raises(ValueError):
        DLXMatrix([], [])


def test_matrix_has_correct_string_representation():
    universe = [1, 2]
    set_collection = [[1], [1]]
    matrix = DLXMatrix(universe, set_collection)
    assert str(matrix) == "Column 1 has 2 rows: 0 1\nColumn 2 has 0 rows:\n"
