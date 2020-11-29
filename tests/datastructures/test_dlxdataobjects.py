"""Unit tests for dlx data objects."""

# TODO: check these through

from exact_cover_solver.datastructures.dlxdataobjects import DataObject, ColumnObject


def test_column_objects_column_is_linked_to_self_on_init():
    column = ColumnObject(1)
    assert column.column == column


def test_column_object_has_no_size_on_init():
    column = ColumnObject(1)
    assert column.size == 0


def test_column_object_gets_id_from_args():
    column = ColumnObject(2)
    assert column.id == 2


def test_data_object_is_linked_to_self_on_init():
    column = ColumnObject(1)
    data = DataObject(column, 0)
    assert data.up is data.down is data.left is data.right is data
    assert data.column is column


def test_data_object_gets_row_from_args():
    column = ColumnObject(1)
    data = DataObject(column, 0)
    assert data.row == 0
