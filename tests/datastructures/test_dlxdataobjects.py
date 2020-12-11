from unittest.mock import Mock

from exact_cover_solver.datastructures.dlxdataobjects import (
    DataObject,
    ColumnObject,
    RootObject,
)


def test_root_object_is_linked_to_self_on_init():
    root = RootObject()
    assert root.right is root.left is root


def test_other_objects_can_be_attached_to_root():
    root = RootObject()
    column_1 = ColumnObject(Mock())
    column_2 = ColumnObject(Mock())
    root.left = column_1
    root.right = column_2


def test_column_objects_column_is_linked_to_self_on_init():
    mocked_id = Mock()
    column = ColumnObject(mocked_id)
    assert column.left is column.right is column.up is column.down is column


def test_column_object_has_no_size_on_init():
    mocked_id = Mock()
    column = ColumnObject(mocked_id)
    assert column.size == 0


def test_column_object_gets_id_from_args():
    mocked_id = Mock()
    column = ColumnObject(mocked_id)
    assert column.id == mocked_id


def test_other_objects_can_be_attached_to_columns():
    column = ColumnObject(Mock())
    data_1 = DataObject(Mock(), Mock())
    data_2 = DataObject(Mock(), Mock())
    column_1 = ColumnObject(Mock())
    column_2 = ColumnObject(Mock())

    column.left = column_1
    column.right = column_2

    column.up = data_1
    column.down = data_2


def test_data_object_is_linked_to_self_and_column_on_init():
    mocked_column = Mock()
    mocked_id = Mock()
    data = DataObject(mocked_column, mocked_id)
    assert data.up is data.down is data.left is data.right is data
    assert data.column is mocked_column


def test_data_object_gets_id_from_args():
    mocked_column = Mock()
    mocked_id = Mock()
    data = DataObject(mocked_column, mocked_id)
    assert data.id == mocked_id


def test_other_objects_can_be_attached_to_data_objects():
    column = ColumnObject(Mock())
    data = DataObject(Mock(), column)
    data_1 = DataObject(Mock(), Mock())
    data_2 = DataObject(Mock(), Mock())
    data_3 = DataObject(Mock(), Mock())

    data.left = data_1
    data.right = data_2

    data.up = column
    data.down = data_3
