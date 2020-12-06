"""Data creator for sudoku problem."""
from .data_creator_base import DataCreator
from exact_cover_solver.types import ProblemData, Subset
from typing import List, Tuple

Sudoku = List[List[int]]
Point = Tuple[int, int]


class SudokuCreator(DataCreator):
    """Data creator for sudoku problem."""

    def create_problem_data(self, sudoku: Sudoku = None) -> ProblemData:
        """Create universe and subset collection."""
        self._check_that_sudoku_is_valid(sudoku)
        if not sudoku:
            raise ValueError
        size = len(sudoku)
        values = range(1, size + 1)

        # Create universe of constrains
        universe = []
        for i in range(9):
            for j in range(9):
                num = j + 1
                universe.append(f"cell_{i}_{j}")
                universe.append(f"row_{i}_{num}")
                universe.append(f"col_{i}_{num}")
                universe.append(f"block_{i}_{num}")

        subset_collection = []
        for y in range(size):
            for x in range(size):
                if sudoku[y][x] == 0 or sudoku[y][x] is None:
                    for value in values:
                        subset_collection.append(self._create_subset(value, (y, x)))
                else:
                    subset_collection.append(self._create_subset(sudoku[y][x], (y, x)))
        return universe, subset_collection

    @staticmethod
    def _check_that_sudoku_is_valid(sudoku: Sudoku) -> None:
        """Check that sudoku is valid sudoku (no duplicates etc.)."""
        if not sudoku:
            raise ValueError("You called sudoku creator without sudoku as argument.")
        # TODO: Add validator checker here
        # TODO: set some max size here for sudoku size (4x4, 5x5?)
        # TODO: set some min size for clues, so amount of solutions does not explode

    @staticmethod
    def _create_subset(value: int, point: Point) -> Subset:
        """Create subset representing placing a value to point (x,y) in sudoku.

        Subset will have four values each representing some constrain:
        - Cell constrain: only one of value in each of cells
        - Row constrain: only one of possible values in each row
        - Column constrain: only one of possible values in each column
        - Block constrain: only one of possible value in each block
        """
        y, x = point
        block_num = (y // 3) * 3 + (x // 3)
        return [
            f"cell_{y}_{x}",
            f"row_{y}_{value}",
            f"col_{x}_{value}",
            f"block_{block_num}_{value}",
        ]
