"""Dictionary-based 0s and 1s matrix implementation class."""

from exact_cover_solver.datastructures import Matrix
from exact_cover_solver.data_creators import Universe, SetCollection
from typing import Dict, Set, Optional, Tuple

ColumnDict = Dict[int, Set[int]]
ColumnValue = Set[int]


class DictMatrix(Matrix):
    """Matrix representation based on dictionaries and sets."""

    def __init__(self, universe: Universe, set_collection: SetCollection) -> None:
        """Initialize dictionary based matrix.

        Create initial variable for matrix, then pass the universe and the set
        collection constrains to parent initializer.

        Columns matrix includes dict with each element in universe as keys (=matrix
        column) and each row where element is presented collected to set as values.

        Args:
            universe: a list of integers representing some set of elements
            set_collection: a list of lists, each made from integers in the universe
        """
        self._columns: Optional[ColumnDict] = None
        super().__init__(universe, set_collection)

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
    def data(self) -> Tuple[ColumnDict, SetCollection]:
        """Get created dictionary and original set collection.

        Returns:
            Tuple containing created matrix and set collection used to create matrix.
        """
        return self._columns, self._set_collection


# Add all private methods to pdoc when generating documentation
__pdoc__ = {
    f"DictMatrix.{func}": True
    for func in dir(DictMatrix)
    if callable(getattr(DictMatrix, func)) and func.startswith("_")
}
