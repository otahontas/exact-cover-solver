"""Unit tests for dlx data objects."""

from exact_cover_solver.datastructures.dlxdataobjects import DataObject, ColumnObject


def test_column_objects_column_is_linked_to_self_on_init():
    column = ColumnObject()
    assert column.column == column


def test_column_object_has_no_size_and_id_on_init_without_args():
    column = ColumnObject()
    assert column.id is None
    assert column.size == 0


def test_column_object_gets_id_from_args():
    column = ColumnObject("A")
    assert column.id == "A"


def test_data_object_is_linked_to_self_on_init():
    column = ColumnObject()
    data = DataObject(column)
    assert data.up is data.down is data.left is data.right is data
    assert data.column is column


def test_data_object_has_no_row_on_init():
    column = ColumnObject()
    data = DataObject(column)
    assert data.row is None


def test_data_object_gets_row_from_args():
    column = ColumnObject()
    data = DataObject(column, "1")
    assert data.row == "1"
