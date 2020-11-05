"""Circular doubly linked list node definitions and iterators."""


class Node:
    """Single node definition."""

    def __init__(self, header, row):
        """Initialize single node."""
        self.header = header
        self.row = row
        self.up = self.down = self.left = self.right = self

    def deattach_column(self):
        """Remove node from matrix."""
        self.up.down = self.down
        self.down.up = self.up
        self.left.right = self.right
        self.right.left = self.left
        self.header.decrease_count()

    def attach(self):
        """Restore node placement in matrix."""
        self.down.up = self.up.down = self.right.left = self.left.right = self
        self.header.increase_count()


class HeaderNode(Node):
    """Column header node for control row."""

    def __init__(self, header_id):
        """Initialize header node with name and id."""
        super(HeaderNode, self).__init__(self, "Header")
        self.id = header_id
        self.size = 0

    def increase_count(self):
        self.size += 1

    def decrease_count(self):
        self.size -= 1


class RootNode:
    """Root node which links header columns together."""

    def __init__(self, left=None, right=None):
        """Initialize root."""
        self.left = left
        self.right = right
        self.id = "Root"
