"""Class for single pentomino and container class for all pentominoes."""

from typing import List, Set

PentominoGrid = List[List[int]]


class Pentomino:
    """Single pentomino class and methods for generating orientations."""

    def __init__(self, name: str, shape: PentominoGrid):
        """Create pentomino.

        Args:
            name: Name of the pentomino
            shape: Shape as two dimensional array
        """
        self._name = name
        self._shape = shape

    def generate_all_orientations(self) -> List[PentominoGrid]:
        """Generate different orientations for this pentomino.

        If pentomino is N, prune half of the orientations away. This helps pruning
        algoX branches.

        Returns:
            List of all unique orientations for the this pentomino.
        """
        seen: Set[str] = set()
        orientations = []
        for transposed in (self._shape, self._transpose(self._shape)):
            for left_right_flipped in (transposed, self._flip_left_right(transposed)):
                for up_down_flipped in (
                    left_right_flipped,
                    self._flip_up_down(left_right_flipped),
                ):
                    orientation_as_string = str(up_down_flipped)
                    if orientation_as_string not in seen:
                        seen.add(orientation_as_string)
                        orientations.append(up_down_flipped)
        if self._name == "N":
            return orientations[::2]
        return orientations

    @property
    def name(self) -> str:
        """Get name of this pentomino."""
        return self._name

    @staticmethod
    def _flip_up_down(pentomino: PentominoGrid) -> PentominoGrid:
        """Reverse each column.

        Args:
            pentomino: Single pentomino polygon

        Returns:
            Pentomino with each column reversed.
        """
        return pentomino[::-1]

    @staticmethod
    def _flip_left_right(pentomino: PentominoGrid) -> PentominoGrid:
        """Reverse each row.

        Args:
            pentomino: Single pentomino polygon

        Returns:
            Pentomino with each row reversed.
        """
        return [row[::-1] for row in pentomino]

    @staticmethod
    def _transpose(pentomino: PentominoGrid) -> PentominoGrid:
        """Transpose whole pentomino.

        Args:
            pentomino: Single pentomino polygon

        Returns:
            Transposed pentomino.
        """
        return [list(x) for x in zip(*pentomino)]


class Pentominoes:
    """Collection of all pentominoes."""

    def __init__(self):
        """Create all pentominoes, save them to list."""
        self._pentomino_list = [
            Pentomino("V", [[1, 1, 1], [1, 0, 0], [1, 0, 0]]),
            Pentomino("U", [[1, 0, 1], [1, 1, 1]]),
            Pentomino("X", [[0, 1, 0], [1, 1, 1], [0, 1, 0]]),
            Pentomino("T", [[1, 0, 0], [1, 1, 1], [1, 0, 0]]),
            Pentomino("Y", [[1, 1, 1, 1], [0, 1, 0, 0]]),
            Pentomino("I", [[1, 1, 1, 1, 1]]),
            Pentomino("F", [[0, 1, 0], [1, 1, 0], [0, 1, 1]]),
            Pentomino("P", [[1, 1, 1], [1, 1, 0]]),
            Pentomino("W", [[1, 1, 0], [0, 1, 1], [0, 0, 1]]),
            Pentomino("Z", [[1, 0, 0], [1, 1, 1], [0, 0, 1]]),
            Pentomino("N", [[1, 1, 0, 0], [0, 1, 1, 1]]),
            Pentomino("L", [[1, 1, 1, 1], [1, 0, 0, 0]]),
        ]

    def as_list(self) -> List[Pentomino]:
        """Get collection as list."""
        return self._pentomino_list

    def get_name_by_index(self, index) -> str:
        """Return pentomino name by given index."""
        return self._pentomino_list[index].name

    @property
    def amount(self) -> int:
        """Get amount of pentominoes in this collection."""
        return len(self._pentomino_list)


# Add all private methods to pdoc when generating documentation
__pdoc__ = {
    f"Pentomino.{func}": True
    for func in dir(Pentomino)
    if callable(getattr(Pentomino, func)) and func.startswith("_")
}
