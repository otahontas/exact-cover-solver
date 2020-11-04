"""Circular doubly linked list node definitions and iterators."""


class Node:
    """Single node definition."""

    def __init__(self, header):
        """Initialize single node."""
        self.header = header
        self.up = self.down = self.left = self.right = self

    def deattach(self):
        """Remove node from matrix."""
        self.up.down = self.down
        self.down.up = self.up
        self.left.right = self.right
        self.right.left = self.left

    def attach(self):
        """Restore node placement in matrix."""
        self.down.up = self.up.down = self.right.left = self.left.right = self


class HeaderNode:
    """Column header node for control row."""

    def __init__(self, id):
        """Initialize header node with name and id."""
        self.id = id
        self.size = 0
