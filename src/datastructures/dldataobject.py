"""Circular doubly linked list node classes."""


class DataObject:
    """Single node definition."""

    def __init__(self, header, row):
        """Initialize single node."""
        self.header = header
        self.row = row
        self.up = self.down = self.left = self.right = self


class ColumnObject(DataObject):
    """Column header node for control row."""

    def __init__(self, header_id):
        """Initialize header node with name and id."""
        super(ColumnObject, self).__init__(self, "Header")
        self.id = header_id
        self.size = 0


class RootNode:
    """Root node which links header columns together."""

    def __init__(self, left=None, right=None):
        """Initialize root."""
        self.left = left
        self.right = right
        self.id = "Root"
