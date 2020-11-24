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
        super().__init__(universe, set_collection)

    def _create_columns(self) -> None:
        """Create column."""
        pass

    def _create_nodes(self) -> None:
        """Create nodes."""
        pass
