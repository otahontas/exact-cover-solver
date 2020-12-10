"""Dictionary-based 0s and 1s matrix implementation class."""

from .matrix_base import Matrix
from exact_cover_solver.types import SubsetCollection, ProblemData
from typing import Dict, Set, Optional, Tuple

ColumnDict = Dict[int, Set[int]]
ColumnValue = Set[int]


class DictMatrix(Matrix):
    """Matrix representation based on dictionaries and sets."""

    def __init__(self, constrains: ProblemData) -> None:
        """Initialize dictionary based matrix.

        Create initial variable for matrix, then pass the universe and the set
        collection constrains to parent initializer.

        Columns matrix includes dict with each element in universe as keys (=matrix
        column) and each row where element is presented collected to set as values.

        Args:
            constrains: Tuple containing universe and set collection.
        """
        self._columns: Optional[ColumnDict] = None
        super().__init__(constrains)

    def _create(self) -> None:
        """Create dict with sets representing elements in each set in collection.

        All sets are iterated through. For each element in set the set index is added
        to internal dictionary.
        """
        self._columns = {element: set() for element in self._universe}
        for set_index, set_elements in enumerate(self._set_collection):
            for element in set_elements:
                self._columns[element].add(set_index)

    @property
    def data(self) -> Tuple[ColumnDict, SubsetCollection]:
        """Get created dictionary and original set collection.

        Returns:
            Tuple containing created matrix and set collection used to create matrix.
        """
        return self._columns, self._set_collection
