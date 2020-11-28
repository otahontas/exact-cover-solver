"""Dictionary-based 0s and 1s matrix implementation classes."""

from exact_cover_solver.datastructures import Matrix
from exact_cover_solver.data_creators import Universe, SetCollection


class DictMatrix(Matrix):
    """Dict based matrix."""

    def __init__(self, universe: Universe, set_collection: SetCollection) -> None:
        """Create column and data objects and link them to this matrix object.

        Args:
            universe: a list of integers representing some set of elements
            set_collection: a list of lists, each made from integers in the universe
        """
        self._grid = None
        super().__init__(universe, set_collection)

    def _create_columns(self) -> None:
        """Create column."""
        pass

    def _create_data_nodes(self) -> None:
        """Create nodes."""
        self._grid = {col: set() for col in self._universe}
        for index, row in enumerate(self._set_collection):
            for element in row:
                self._grid[element].add(index)

    @property
    def grid(self):
        return self._grid
