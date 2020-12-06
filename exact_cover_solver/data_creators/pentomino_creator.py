"""Data creator for pentomino problem."""
from typing import Tuple, List, Optional

from .data_creator_base import DataCreator
from exact_cover_solver.types import Universe, SubsetCollection, ProblemData
from exact_cover_solver.datastructures.pentomino import Pentominoes, PentominoGrid

Point = Tuple[int, int]


class BoardSizeNotInitializedError(Exception):
    """Exception raised when board size not initialized.

    Attributes:
        message -- explanation of the error
    """

    def __init__(
        self, message: str = "Either board height or width is not initialized."
    ) -> None:
        """Initialize error with message."""
        self.message = message
        super().__init__(self.message)


class PentominoCreator(DataCreator):
    """Data creator for pentomino problem.

    Problem has always same amount of pentominoes, cells on board and same universe,
    but the board size varies.
    """

    _CELLS_AMOUNT = 60
    _pentominoes = Pentominoes()
    _universe: Universe = [num for num in range(_pentominoes.amount + _CELLS_AMOUNT)]

    def __init__(self) -> None:
        """Initialize DLX with empty set collection and without dimensions."""
        self._set_collection: SubsetCollection = []
        self._width: Optional[int] = None
        self._height: Optional[int] = None

    def create_problem_data(self) -> ProblemData:
        """Create data representing the pentomino problem in certain board size.

        Returns:
            Tuple containing universe and set collection.

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

    @property
    def board_size(self) -> Tuple[int, int]:
        """Get board size.

        Returns:
            Tuple containing height and width.

        Raises:
            BoardSizeNotInitializedError: Raised if current height or width is None.
        """
        if not self._height or not self._width:
            raise BoardSizeNotInitializedError()
        return self._height, self._width

    def _generate_set_collection(self) -> None:
        """Generate all possible ways to place each pentomino on the board.

        Each generated set includes index for pentomino (value in range 0-11) and five
        cells pentomino can be placed to (values in range 12-72).
        """
        if not self._height or not self._width:
            raise BoardSizeNotInitializedError()
        self._set_collection.clear()
        for index, pentomino in enumerate(self._pentominoes.as_list()):
            for orientation in pentomino.generate_all_orientations():
                pentomino_height = len(orientation)
                pentomino_width = len(orientation[0])
                for row in range(self._height + 1 - pentomino_height):
                    for col in range(self._width + 1 - pentomino_width):
                        point = (row, col)
                        covered = self._solve_covered_cells(orientation, point)
                        self._set_collection.append([index, *covered])

    def _solve_covered_cells(self, pentomino: PentominoGrid, start: Point) -> List[int]:
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
        for y in range(pentomino_height):
            for x in range(pentomino_width):
                if pentomino[y][x] == 1:
                    covered.append(self._point_to_cell_num((start_y + y, start_x + x)))
        return covered

    def _point_to_cell_num(self, point: Point) -> int:
        """Convert point to cell num, used internally."""
        if not self._width:
            raise BoardSizeNotInitializedError()
        y, x = point
        return y * self._width + x + self._pentominoes.amount

    def cell_num_to_point(self, cell: int) -> Point:
        """Convert cell num to point, called from outside."""
        if not self._width:
            raise BoardSizeNotInitializedError()
        cell -= self._pentominoes.amount
        y = cell // self._width
        x = cell - (y * self._width)
        return y, x
