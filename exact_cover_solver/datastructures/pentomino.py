"""Class for single pentomino and container class for all pentominoes."""

from typing import List, Set

PentominoGrid = List[List[int]]


class Pentomino:
    """Single pentomino class and methods for generating orientations."""

    def __init__(self, name: str, shape: PentominoGrid) -> None:
        """Create pentomino.

        Args:
            name: Name of the pentomino
            shape: Shape as two dimensional array
        """
        self._name = name
        self._shape = shape

    def generate_all_orientations(self) -> List[PentominoGrid]:
        """Generate different orientations for this pentomino.

        For V pentomino, only the original orientation is returned. This helps
        algorithm to skip creating unnecessary solutions which are only mirrored /
        flipped from unique solutions.

        Returns:
            List of all unique orientations for the this pentomino.
        """
        if self._name == "V":
            return [self._shape]

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
    """Collection of all pentominoes.

    Attributes:
         ORDER: Pentominoes are order 5 polyominos
         _pentomino_list: List of all pentominoes in their base form.
    """

    def __init__(self) -> None:
        """Initialize order and pentominoes."""
        self.ORDER = 5
        self._pentomino_list = [
            Pentomino("V", [[0, 0, 1], [0, 0, 1], [1, 1, 1]]),
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

    def get_name_by_index(self, index: int) -> str:
        """Return pentomino name by given index."""
        try:
            return self._pentomino_list[index].name
        except IndexError:
            raise ValueError(f"No pentomino with index {index}.")

    def get_pentomino_by_name(self, name: str) -> Pentomino:
        """Return pentomino object by name."""
        try:
            return next(
                pentomino
                for pentomino in self._pentomino_list
                if pentomino.name == name
            )
        except StopIteration:
            raise ValueError(f"No pentomino with name {name}")

    @property
    def amount(self) -> int:
        """Get amount of pentominoes in this collection."""
        return len(self._pentomino_list)

    @property
    def names(self) -> List[str]:
        """Get all used names in pentomino list."""
        return [pentomino.name for pentomino in self._pentomino_list]
