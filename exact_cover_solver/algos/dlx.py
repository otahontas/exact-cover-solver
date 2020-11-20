"""Dancing links implementation for algorithm X."""

from exact_cover_solver.algos import AlgorithmX
from exact_cover_solver.types import Solution
from exact_cover_solver.datastructures.dlxmatrix import DLXMatrix
from exact_cover_solver.datastructures.dlxdataobjects import ColumnObject

from typing import List


class DLX(AlgorithmX):
    """Dancing links implementation for algorithm X."""

    def __init__(self) -> None:
        """Initialize solution list."""
        self.__solutions: List[Solution] = []

    def solve(self, matrix: DLXMatrix) -> List[Solution]:
        """Solve exact cover problem for given matrix."""
        self.__solutions.clear()
        self._search(matrix)
        return self.__solutions

    def _search(self, matrix: DLXMatrix, partial: Solution = None) -> None:
        """Perform algorithm X recursively.

        Algorithm:
        - If R[h] = h, solution has been found
        - Otherwise choose column c optimally. If column doesn't have 1s, terminate.
        - Cover column c
        - Go through rows of column c
            - Include row in partial solution
            - Cover each column on row
            - Search for solution recursively
            - Uncover each column on row
            - Remove row from partial solution
        - Uncover column c
        """
        if not partial:
            partial: Solution = []

        if matrix.right == matrix:
            self.__solutions.append(partial[:])
            return

        column = self._choose_optimal_column_object(matrix)

        if not column.size:
            return

        self._cover(column)

        row = column.down
        while row != column:
            partial.append(row.row)
            node = row.right
            while node != row:
                self._cover(node.column)
                node = node.right
            self._search(matrix, partial)
            node = row.left
            while node != row:
                self._uncover(node.column)
                node = node.left
            partial.pop()
            row = row.down
        self._uncover(column)

    @staticmethod
    def _choose_optimal_column_object(matrix: DLXMatrix) -> ColumnObject:
        """Find column with smallest number of 1s.

        This is done to minimize the branching factor.
        """
        current_column = matrix.right
        column = current_column
        size = current_column.size
        while current_column != matrix:
            column, size = (
                (current_column, current_column.size)
                if current_column.size < size
                else (column, size)
            )
            current_column = current_column.right
        return column

    @staticmethod
    def _cover(column: ColumnObject) -> None:
        """Cover given column.

        First remove column from the header list and then remove all rows
        in column from other column lists rows are in.

        Covering is done from top to bottom and left to right manner.
        """
        column.detach()
        row = column.down
        while row != column:
            node = row.right
            while node != row:
                node.detach()
                node = node.right
            row = row.down

    @staticmethod
    def _uncover(column: ColumnObject) -> None:
        """Uncover given column.

        Uncovering is done from bottom to top and right to left manner in order to undo
        covering steps.
        """
        row = column.up
        while row != column:
            node = row.left
            while node != row:
                node.attach()
                node = node.left
            row = row.up
        column.attach()
