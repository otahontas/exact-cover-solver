"""Exact cover matrix implementation with dancing links."""
from typing import Union, Optional

from .matrix_base import Matrix
from .dlxdataobjects import RootObject, ColumnObject, DataObject
from exact_cover_solver.types import ProblemData, UniverseElement


class DLXMatrix(Matrix):
    """Exact cover matrix implementation with dancing links.."""

    def __init__(self, problem_data: ProblemData) -> None:
        """Initialize matrix with root object.

        Args:
            problem_data: Data needed to create matrix.
        """
        self.root = RootObject()
        super().__init__(problem_data)

    def _create(self) -> None:
        """Call creator methods for column and data objects."""
        self._create_column_objects()
        self._create_data_objects()

    def _create_column_objects(self) -> None:
        """Create column objects representing elements in universe.

        Column objects are linked to root and together to form a circular row.
        """
        previous_column: Union[ColumnObject, RootObject] = self.root
        for element in self._universe:
            created_column = ColumnObject(element)
            created_column.left = previous_column
            previous_column.right = created_column
            previous_column = created_column
        self.root.left = previous_column
        previous_column.right = self.root

    def _create_data_objects(self) -> None:
        """Create data objects representing elements in each subset.

        Data objects are linked to correct column object and linked together to form
        a circular row.
        """
        for subset_id, subset_elements in self._subset_collection.items():
            leftmost_data_object: Optional[DataObject] = None
            previous_data_object: Optional[DataObject] = None

            for element in subset_elements:
                column = self._find_column(element)
                created_data_object = DataObject(column, subset_id)

                lowest_data_object = column.up
                lowest_data_object.down = created_data_object

                created_data_object.up = lowest_data_object
                created_data_object.down = column
                column.up = created_data_object

                if not leftmost_data_object:
                    leftmost_data_object = created_data_object

                if previous_data_object:
                    previous_data_object.right = created_data_object
                    created_data_object.left = previous_data_object

                previous_data_object = created_data_object
                column.increase_size()

            if not previous_data_object or not leftmost_data_object:
                raise ValueError(
                    "Cannot not link subset elements together for subset "
                    f"{subset_id}: {subset_elements}"
                )
            previous_data_object.right = leftmost_data_object
            leftmost_data_object.left = previous_data_object

    def _find_column(self, element: UniverseElement) -> ColumnObject:
        """Find column object representing given element.

        Args:
            element: Element to look for

        Returns:
            Column object of the correct object

        Raises:
            ValueError: if root object does not have any links or there is no
                        column for given element.
        """
        column = self.root.right
        while True:
            if isinstance(column, RootObject):
                raise ValueError(f"Could not find column with element {element}")
            if column.id == element:
                return column
            column = column.right
