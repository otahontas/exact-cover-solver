"""DLX matrix implementation based on data objects."""

class DLXMatrix:
    pass

class RootNode:
    """Root node which links header columns together."""

    def __init__(self, left=None, right=None):
        """Initialize root."""
        self.left = left
        self.right = right
        self.id = "Root"

