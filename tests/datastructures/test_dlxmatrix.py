"""Unit tests for dlx matrix."""
import pytest
from exact_cover_solver.datastructures.dlxmatrix import DLXMatrix


def test_matrix_columns_are_linked_together_correctly():
    universe = [1, 2, 3, 4, 5, 6, 7]
    set_collection = [
        ("A", [1, 4, 7]),
        ("B", [1, 4]),
        ("C", [4, 5, 7]),
        ("D", [3, 5, 6]),
        ("E", [2, 3, 6, 7]),
        ("F", [2, 7]),
    ]

    matrix = DLXMatrix(universe, set_collection)
    assert matrix is not None
    assert matrix.id == "root"
    assert matrix.right.id == 1
    assert matrix.left.id == 7


def test_each_column_in_matrix_has_correct_size():
    universe = [1, 2, 3, 4, 5, 6, 7]
    set_collection = [
        ("A", [1, 4, 7]),
        ("B", [1, 4]),
        ("C", [4, 5, 7]),
        ("D", [3, 5, 6]),
        ("E", [2, 3, 6, 7]),
        ("F", [2, 7]),
    ]
    matrix = DLXMatrix(universe, set_collection)

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
