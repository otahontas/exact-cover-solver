"""Wrappers to represent dancing links data and column objects as matrix."""

from typing import Optional

from .matrix_base import Matrix
from .dlxdataobjects import DataObject, ColumnObject
from exact_cover_solver.types import ProblemData


class DLXMatrix(Matrix):
    """Matrix representation and initialization methods for circular linked lists."""

    def __init__(self, constrains: ProblemData) -> None:
        """Initialize linked list based matrix.

        Create initial links to column objects, then pass the universe and the set
        collection constrains to parent initializer.

        Args:
            constrains: Tuple containing universe and set collection.
        """
        self.right: Optional[ColumnObject] = None
        self.left: Optional[ColumnObject] = None
        super().__init__(constrains)

    def _create(self) -> None:
        """Call creator methods for different linked list data types."""
        self._create_column_nodes()
        self._create_data_nodes()

    def _create_column_nodes(self) -> None:
        """Create column columns and attach them to root."""
        previous = self
        for element in self._universe:
            column = ColumnObject(column_id=element)
            column.left = previous
            previous.right = column
            previous = column
        self.left = previous
        previous.right = self

    def _create_data_nodes(self) -> None:
        """Create nodes representing elements in each set in collection.

        All sets are iterated through. For each element in set the element is
        linked to the correct column and columns column. Elements in set are
        also linked together to form a circular row.
        """

        def find_column(_id: int) -> ColumnObject:
            """Find column with given id."""
            correct_column = self
            while correct_column.id != _id:
                correct_column = correct_column.right
            return correct_column

        for set_number, set_elements in enumerate(self._set_collection):
            previous = None
            first = None

            for element in set_elements:
                column = find_column(element)
                cell = DataObject(column, set_number)

                prev_up = column.up
                prev_up.down = cell

                cell.up = prev_up
                cell.down = column
                column.up = cell

                if previous:
                    previous.right = cell
                    cell.left = previous
                else:
                    first = cell

                previous = cell
                column.size += 1

            previous.right = first
            first.left = previous
