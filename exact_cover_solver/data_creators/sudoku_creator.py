"""Data creator for sudoku problem."""
from exact_cover_solver.types import (
    ProblemData,
    Subset,
    Universe,
    SubsetCollection,
    SubsetId,
)
from typing import List, Tuple

SudokuInput = List[List[int]]
Point = Tuple[int, int]


class SudokuCreator:
    """Data creator for sudoku problem."""

    def create_problem_data(self, sudoku_input: SudokuInput) -> ProblemData:
        """Create universe and subset collection.

        Args:
            sudoku_input: Two-dimensional sudoku board, where empty cells are marked
                          with zero and other cells have preselected numbers.

        Returns:
            Data that can be used to create exact cover problem matrix.
        """
        self._validate_sudoku_input(sudoku_input)
        size = len(sudoku_input)
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
                if sudoku_input[y][x] == 0 or sudoku_input[y][x] is None:
                    for value in values:
                        subset_collection.append(self._create_subset(value, (y, x)))
                else:
                    subset_collection.append(
                        self._create_subset(sudoku_input[y][x], (y, x))
                    )
        return universe, subset_collection

    def _validate_sudoku_input(self, sudoku_input: SudokuInput) -> None:
        """Check that sudoku is valid sudoku.

        Args:
            sudoku_input: Two-dimensional sudoku board.

        Raises:
            ValueError: if input was not valid sudoku.
        """
        size = len(sudoku_input)
        seen_x = [set() for _ in range(size)]
        seen_block = [set() for _ in range(size)]
        for y, row in enumerate(sudoku_input):
            seen_y = set()
            if len(row) != size:
                raise ValueError(
                    f"Sudoku must have same length and height, but row "
                    f"{y + 1} has length {len(row)}, while height is "
                    f"{size}."
                )
            for x, num in enumerate(row):
                if num == 0:
                    continue

                if num in seen_y:
                    raise ValueError(
                        "Row should have unique numbers, but there was "
                        f"multiple {num}s on row {y + 1}"
                    )
                seen_y.add(num)

                if num in seen_x[x]:
                    raise ValueError(
                        "Column should have unique numbers, but there was "
                        f"multiple {num}s on column {x + 1}"
                    )
                seen_x[x].add(num)

                block_num = self._calculate_block_num((x, y))
                if num in seen_block[block_num]:
                    raise ValueError(
                        "Block should have unique numbers, but there was "
                        f"multiple {num}s on block {block_num + 1}"
                    )
                seen_block[block_num].add(num)

    def _create_subset(self, value: int, point: Point) -> Subset:
        """Create subset representing placing a value to point (x,y) in sudoku.

        Subset will have four values each representing some constrain:
        - Cell constrain: only one of value in each of cells
        - Row constrain: only one of possible values in each row
        - Column constrain: only one of possible values in each column
        - Block constrain: only one of possible value in each block
        """
        y, x = point
        block_num = self._calculate_block_num((x, y))
        return [
            f"cell_{y}_{x}",
            f"row_{y}_{value}",
            f"col_{x}_{value}",
            f"block_{block_num}_{value}",
        ]

    @staticmethod
    def _calculate_block_num(point: Point) -> int:
        """Calculate which block given point belongs.

        Args:
            point: Point (x,y)

        Returns:
            Number of the block point belongs.
        """
        x, y = point
        return (y // 3) * 3 + (x // 3)
