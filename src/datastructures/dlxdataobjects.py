"""Circular doubly linked list object definitions."""


class DataObject:
    """Data object representing 1s in matrix."""

    def __init__(self, column, row=None):
        """Link data object to column object, optionally set row name."""
        self.column = column
        self.row = row
        self.up = self.down = self.left = self.right = self

    def deattach(self):
        """Deattach object from linked list, but don't erase it from memory"""
        raise NotImplementedError

    def attach(self):
        """Attach object back to its original position in linked list."""
        raise NotImplementedError


class ColumnObject(DataObject):
    """Column object representing matrix columns."""

    def __init__(self, _id=None):
        """Set column size, link column object to itself."""
        super(ColumnObject, self).__init__(self)
        self.id = _id
        self.size = 0
