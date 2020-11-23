"""Universe and set collection creator for pentomino problem."""
from typing import Tuple, List, Dict, Set, Optional

from exact_cover_solver.data_creators import DataCreator, Universe, SetCollection

Pentomino = List[List[int]]
Point = Tuple[int, int]


class BoardSizeNotInitializedError(Exception):
    """Exception raised when board size not initialized.

    Attributes:
        message -- explanation of the error
    """

    def __init__(self, message="Either board height or width is not initialized."):
        """Initialize error with message."""
        self.message = message
        super().__init__(self.message)


class PentominoCreator(DataCreator):
    """Universe and set collection creator for pentomino problem.

    Problem has always same amount of pentominoes, cells on board and same universe,
    but the board size varies.
    """

    _PENTOMINOES_AMOUNT = 12
    _CELLS_AMOUNT = 60
    _universe: Universe = [num for num in range(_PENTOMINOES_AMOUNT + _CELLS_AMOUNT)]
    _pentominoes: Dict[str, Pentomino] = {
        "V": [[1, 1, 1], [1, 0, 0], [1, 0, 0]],
        "U": [[1, 0, 1], [1, 1, 1]],
        "X": [[0, 1, 0], [1, 1, 1], [0, 1, 0]],
        "T": [[1, 0, 0], [1, 1, 1], [1, 0, 0]],
        "Y": [[1, 1, 1, 1], [0, 1, 0, 0]],
        "I": [[1, 1, 1, 1, 1]],
        "F": [[0, 1, 0], [1, 1, 0], [0, 1, 1]],
        "P": [[1, 1, 1], [1, 1, 0]],
        "W": [[1, 1, 0], [0, 1, 1], [0, 0, 1]],
        "Z": [[1, 0, 0], [1, 1, 1], [0, 0, 1]],
        "N": [[1, 1, 0, 0], [0, 1, 1, 1]],
        "L": [[1, 1, 1, 1], [1, 0, 0, 0]],
    }
    _pentomino_indexes: Dict[str, int] = {
        "V": 0,
        "U": 1,
        "X": 2,
        "T": 3,
        "Y": 4,
        "I": 5,
        "F": 6,
        "P": 7,
        "W": 8,
        "Z": 9,
        "N": 10,
        "L": 11,
    }

    def __init__(self) -> None:
        """Initialize DLX with empty set collection and without dimensions."""
        self._set_collection: SetCollection = []
        self._width: Optional[int] = None
        self._height: Optional[int] = None

    def create_universe_and_set_collection(self) -> Tuple[Universe, SetCollection]:
        """Create data representing the pentomino problem in certain board size.

        Returns:
            Tuple containing universe, a list of integers representing some set of
                elements and collection of sets, a list of lists, each made from
                integers in the universe

        Raises:
            BoardSizeNotInitializedError: Raised if current height or width is None.
        """
        if not self._height or not self._width:
            raise BoardSizeNotInitializedError()
        return self._universe, self._set_collection

    def change_board_size(self, height: int, width: int) -> None:
        """Change board size and generate collection of sets in advance.

        This means that collection of sets can be kept in memory as long as board size
        is not changed.

        Args:
            height: Height of the pentomino board, must be 6, 5, 4 or 3
            width: Width of the pentomino board, must be 10, 12, 15 or 20

        Raises:
            ValueError: Error is raised if wrong size or width is given
        """
        if height not in [6, 5, 4, 3]:
            raise ValueError(f"Height {height} is not allowed.")

        if width not in [10, 12, 15, 20]:
            raise ValueError(f"Width {width} is not allowed.")

        if height * width != self._CELLS_AMOUNT:
            raise ValueError(f"{width}x{height} board is not allowed.")

        self._height = height
        self._width = width
        self._generate_set_collection()

    def _generate_set_collection(self) -> None:
        """Generate all possible ways to place each pentomino on the board.

        Each generated set includes index for pentomino (value in range 0-11) and five
        cells pentomino can be placed to (values in range 12-72).
        """
        self._set_collection.clear()
        for pentomino in self._pentominoes:
            for orientation in self._generate_all_orientations(
                self._pentominoes[pentomino]
            ):
                pentomino_height = len(orientation)
                pentomino_width = len(orientation[0])
                for row in range(self._height + 1 - pentomino_height):
                    for col in range(self._width + 1 - pentomino_width):
                        point = (row, col)
                        covered = self._solve_covered_cells(orientation, point)
                        self._set_collection.append(
                            [
                                self._pentomino_indexes[pentomino],
                                *[(self._PENTOMINOES_AMOUNT + x) for x in covered],
                            ]
                        )

    def _solve_covered_cells(self, pentomino: Pentomino, start: Point) -> List[int]:
        """Find cells this pentomino covers.

        Args:
            pentomino: Single pentomino polygon
            start: Point where upper-left corner of pentomino grid is placed

        Returns:
            List of all cells (indexed 0-59) this pentomino covers.

        """
        start_y, start_x = start
        covered: List[int] = []
        pentomino_height = len(pentomino)
        pentomino_width = len(pentomino[0])
        for row in range(pentomino_height):
            for column in range(pentomino_width):
                if pentomino[row][column] == 1:
                    cell_index = (start_y + row) * self._width + start_x + column
                    covered.append(cell_index)
        return covered

    def _generate_all_orientations(self, pentomino: Pentomino) -> List[Pentomino]:
        """Generate different orientations for this pentomino.

        If pentomino is N, prune half of the orientations away. This helps pruning
        algoX branches.

        Args:
            pentomino: Single pentomino polygon

        Returns:
            List of all unique orientations for the given pentomino.

        """
        seen: Set[str] = set()
        orientations = []
        for transposed in (pentomino, self._transpose(pentomino)):
            for left_right_flipped in (transposed, self._flip_left_right(transposed)):
                for up_down_flipped in (
                    left_right_flipped,
                    self._flip_up_down(left_right_flipped),
                ):
                    orientation_as_string = str(up_down_flipped)
                    if orientation_as_string not in seen:
                        seen.add(orientation_as_string)
                        orientations.append(up_down_flipped)
        if pentomino == self._pentominoes["N"]:
            return orientations[::2]
        return orientations

    @staticmethod
    def _flip_up_down(pentomino: Pentomino) -> Pentomino:
        """Reverse each column.

        Args:
            pentomino: Single pentomino polygon

        Returns:
            Pentomino with each column reversed.
        """
        return pentomino[::-1]

    @staticmethod
    def _flip_left_right(pentomino: Pentomino) -> Pentomino:
        """Reverse each row.

        Args:
            pentomino: Single pentomino polygon

        Returns:
            Pentomino with each row reversed.
        """
        return [row[::-1] for row in pentomino]

    @staticmethod
    def _transpose(pentomino: Pentomino) -> Pentomino:
        """Transpose whole pentomino.

        Args:
            pentomino: Single pentomino polygon

        Returns:
            Transposed pentomino.
        """
        return [list(x) for x in zip(*pentomino)]


# Add all private methods to pdoc when generating documentation
__pdoc__ = {
    f"PentominoCreator.{func}": True
    for func in dir(PentominoCreator)
    if callable(getattr(PentominoCreator, func)) and func.startswith("_")
}
