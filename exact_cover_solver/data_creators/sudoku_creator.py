"""Data creator for sudoku problem."""
from exact_cover_solver.types import (
    ProblemData,
    Subset,
    Universe,
    SubsetCollection,
)
from typing import List, Tuple, Set

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
        universe = self._create_universe(sudoku_input)
        subset_collection = self._create_subset_collection(sudoku_input)
        return universe, subset_collection

    def _validate_sudoku_input(self, sudoku_input: SudokuInput) -> None:
        """Check that sudoku is valid sudoku.

        Args:
            sudoku_input: Two-dimensional sudoku board.

        Raises:
            ValueError: if input was not valid sudoku.
        """
        size = len(sudoku_input)
        seen_x: List[Set[int]] = [set() for _ in range(size)]
        seen_block: List[Set[int]] = [set() for _ in range(size)]
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

    @staticmethod
    def _create_universe(sudoku_input: SudokuInput) -> Universe:
        """Create universe of all possible constrains.

        Each possible (x,y) placement in board will have four different constrains:
        - Cell constrain: only one of value in each of cells
        - Row constrain: only one of possible values in each row
        - Column constrain: only one of possible values in each column
        - Block constrain: only one of possible value in each block

        Args:
            sudoku_input: Two-dimensional sudoku board.

        Returns:
            List of universe elements
        """
        size = len(sudoku_input)
        universe: Universe = []
        for i in range(size):
            for j in range(size):
                value = j + 1
                universe.append(("cell", j, i))
                universe.append(("row", i, value))
                universe.append(("col", i, value))
                universe.append(("block", i, value))
        return universe

    def _create_subset_collection(self, sudoku_input: SudokuInput) -> SubsetCollection:
        """Create all possible ways to place numbers on sudoku board.

        For points where value has been defined already, only one subset is created.
        Otherwise subset is created for all possible values from 1 to size of sudoku,
        e.g. 1 to 9.

        Args:
            sudoku_input: Two-dimensional sudoku board.

        Returns:
            Dictionary with subset names and their elements.
        """
        size = len(sudoku_input)
        subset_collection: SubsetCollection = {}
        for y in range(size):
            for x in range(size):
                defined_value = sudoku_input[y][x]
                values = range(1, size + 1) if defined_value == 0 else [defined_value]
                for value in values:
                    subset_id = (y, x, value)
                    subset_collection[subset_id] = self._create_subset(value, (x, y))
        return subset_collection

    def _create_subset(self, value: int, point: Point) -> Subset:
        """Create a subset of constrains that represent placing a value to point.

        Args:
            value: Value to place to point
            point: Point (x,y)

        Returns:
            List of constrains.
        """
        block_num = self._calculate_block_num(point)
        x, y = point
        return [
            ("cell", y, x),
            ("row", y, value),
            ("col", x, value),
            ("block", block_num, value),
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
