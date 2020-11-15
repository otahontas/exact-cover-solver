"""Circular doubly linked list object definitions."""


class DataObject:
    """Data object representing 1s in matrix."""

    def __init__(self, column, row=None):
        """Link data object to column object, optionally set row name."""
        self.column = column
        self.row = row
        self.up = self.down = self.left = self.right = self

    def detach(self):
        """Detach data object from linked list, but don't erase it from memory."""
        self.down.up = self.up
        self.up.down = self.down
        self.column.size -= 1

    def attach(self):
        """Attach data object back to its original position in linked list."""
        self.column.size += 1
        self.up.down = self.down.up = self


class ColumnObject(DataObject):
    """Column object representing matrix columns."""

    def __init__(self, _id=None):
        """Set column size, link column object to itself."""
        super(ColumnObject, self).__init__(self)
        self.id = _id
        self.size = 0

    def detach(self):
        """Detach column object from header list, but don't erase it from memory."""
        self.right.left = self.left
        self.left.right = self.right

    def attach(self):
        """Attach column object back to its original position in header list."""
        self.left.right = self.right.left = self
