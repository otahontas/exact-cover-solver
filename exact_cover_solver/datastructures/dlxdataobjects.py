"""Circular doubly linked list object definitions."""


class DataObject:
    """Data object representing 1s in matrix."""

    def __init__(self, column: "ColumnObject", row: str) -> None:
        """Link data object to column object, set row identifier."""
        self.column = column
        self.row = row
        self.up = self.down = self.left = self.right = self

    def detach(self) -> None:
        """Detach data object from linked list, but don't erase it from memory."""
        self.down.up = self.up
        self.up.down = self.down
        self.column.decrease_size()

    def attach(self) -> None:
        """Attach data object back to its original position in linked list."""
        self.column.increase_size()
        self.up.down = self.down.up = self


class ColumnObject(DataObject):
    """Column object representing matrix columns."""

    def __init__(self, _id: int) -> None:
        """Set column size, link column object to itself.

        Also set column id to represent element in search universe.
        """
        super(ColumnObject, self).__init__(self, "column")
        self.id = _id
        self.size = 0

    def detach(self) -> None:
        """Detach column object from header list, but don't erase it from memory."""
        self.right.left = self.left
        self.left.right = self.right

    def attach(self) -> None:
        """Attach column object back to its original position in header list."""
        self.left.right = self.right.left = self

    def increase_size(self) -> None:
        """Increase size when attaching new node to column."""
        self.size += 1

    def decrease_size(self) -> None:
        """Decrease size when detaching node from column."""
        self.size -= 1
