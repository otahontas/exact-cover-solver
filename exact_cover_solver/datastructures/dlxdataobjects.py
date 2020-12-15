"""Dancing link matrix objects."""

from typing import Union

from exact_cover_solver.types import SubsetId, UniverseElement


class RootObject:
    """Column object to link matrix column and data objects together."""

    def __init__(self) -> None:
        """Initialize links."""
        self.left: Union[RootObject, ColumnObject] = self
        self.right: Union[RootObject, ColumnObject] = self


class ColumnObject:
    """Column object representing matrix columns."""

    def __init__(self, column_id: UniverseElement) -> None:
        """Initialize column object details and links.

        Args:
            column_id: Which element this column represents.
        """
        self.id = column_id
        self.size = 0
        self.up: Union[ColumnObject, DataObject] = self
        self.down: Union[ColumnObject, DataObject] = self
        self.left: Union[ColumnObject, RootObject] = self
        self.right: Union[ColumnObject, RootObject] = self

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


class DataObject:
    """Data object representing elements in subsets."""

    def __init__(self, column: ColumnObject, subset_id: SubsetId) -> None:
        """Initialize data object details and links.

        Args:
            column: Column object this data object should be linked to
            subset_id: Id of the subset this data object belongs to.
        """
        self.column = column
        self.id = subset_id
        self.up: Union[DataObject, ColumnObject] = self
        self.down: Union[DataObject, ColumnObject] = self
        self.left: DataObject = self
        self.right: DataObject = self

    def detach(self) -> None:
        """Detach data object from linked list, but don't erase it from memory."""
        self.down.up = self.up
        self.up.down = self.down
        self.column.decrease_size()

    def attach(self) -> None:
        """Attach data object back to its original position in linked list."""
        self.column.increase_size()
        self.up.down = self.down.up = self
