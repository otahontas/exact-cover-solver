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
    constrains = (universe, collection_with_single_solution)
    matrix = DLXMatrix(constrains)
    assert matrix is not None
    assert matrix.id == "root"
    assert matrix.right.id == 1
    assert matrix.left.id == 7


def test_each_column_in_matrix_has_correct_size(
    universe, collection_with_single_solution
):
    constrains = (universe, collection_with_single_solution)
    matrix = DLXMatrix(constrains)

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
