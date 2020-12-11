"""Data creator for pentomino problem."""
from typing import Tuple, List

from .data_creator_base import DataCreator
from exact_cover_solver.types import Universe, SubsetCollection, ProblemData
from exact_cover_solver.datastructures.pentomino import Pentominoes, PentominoGrid

Point = Tuple[int, int]


class PentominoCreator(DataCreator):
    """Data creator for pentomino problem.

    Attributes:
        _PENTOMINOES: Pentominoes to create problem data.
        _CELLS_AMOUNT: Number of cells in to cover.
    """

    def __init__(self) -> None:
        """Initialize with pre-defined pentominoes."""
        self._PENTOMINOES = Pentominoes()
        self._CELLS_AMOUNT = self._PENTOMINOES.amount * self._PENTOMINOES.ORDER

    def create_problem_data(self, height: int, width: int) -> ProblemData:
        """Create data representing the pentomino problem in certain board size.

        Args:
            height: Height of the pentomino board, must be 6, 5, 4 or 3
            width: Width of the pentomino board, must be 10, 12, 15 or 20

        Returns:
            Data that can be used to create exact cover problem matrix.

        Raises:
            ValueError: If wrong size or width is given
        """
        if height not in [6, 5, 4, 3]:
            raise ValueError(f"Height {height} is not allowed.")

        if width not in [10, 12, 15, 20]:
            raise ValueError(f"Width {width} is not allowed.")

        if height * width != self._CELLS_AMOUNT:
            raise ValueError(f"{width}x{height} board is not allowed.")
        universe = self._create_universe(height, width)
        subset_collection = self._create_subset_collection(height, width)
        return universe, subset_collection

    def _create_universe(self, height: int, width: int) -> Universe:
        """Create universe of all possible placements and names of pentominoes.

        Args:
            height: Height of the pentomino board
            width: Width of the pentomino board

        Returns:
            List of universe elements.
        """
        names = self._PENTOMINOES.names
        placements = [(x, y) for y in range(height) for x in range(width)]
        return [*names, *placements]

    def _create_subset_collection(self, height: int, width: int) -> SubsetCollection:
        """Create all possible ways to place each pentomino on the board.

        Each generated set is named with unique id and includes six universe
        values: pentomino name and five points pentomino can be placed to.

        Args:
            height: Height of the pentomino board
            width: Width of the pentomino board

        Returns:
            Dictionary with subset names and their elements.
        """
        subset_collection: SubsetCollection = {}
        subset_id = 0
        for pentomino in self._PENTOMINOES.as_list():
            for orientation in pentomino.generate_all_orientations():
                pentomino_height = len(orientation)
                pentomino_width = len(orientation[0])
                for row in range(height + 1 - pentomino_height):
                    for col in range(width + 1 - pentomino_width):
                        point = (col, row)
                        covered = self._solve_covered_cells(orientation, point)
                        subset_collection[subset_id] = [pentomino.name, *covered]
                        subset_id += 1
        return subset_collection

    @staticmethod
    def _solve_covered_cells(pentomino: PentominoGrid, start: Point) -> List[Point]:
        """Find points this pentomino covers.

        Args:
            pentomino: Single pentomino polygon
            start: Point (x,y) where upper-left corner of pentomino grid is placed

        Returns:
            List of points this pentomino covers.
        """
        start_x, start_y = start
        covered: List[Point] = []
        pentomino_height = len(pentomino)
        pentomino_width = len(pentomino[0])
        for y in range(pentomino_height):
            for x in range(pentomino_width):
                if pentomino[y][x] == 1:
                    covered.append((start_x + x, start_y + y))
        return covered
