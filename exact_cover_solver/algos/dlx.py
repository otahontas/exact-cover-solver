"""Dancing links implementation for algorithm X."""

from typing import List

from exact_cover_solver.algos import AlgorithmX, Solution
from exact_cover_solver.datastructures.dlxdataobjects import ColumnObject
from exact_cover_solver.datastructures.dlxmatrix import DLXMatrix


class DLX(AlgorithmX[DLXMatrix]):
    """Dancing links implementation for algorithm X."""

    def __init__(self) -> None:
        super().__init__()

    def solve(self, matrix: DLXMatrix) -> List[Solution]:
        """Solve which rows cover the given matrix.

        Clears solutions bookkeeping from previous runs, then calls
        recursive method.

        Args:
            matrix: Matrix representation implemented as circular doubly linked lists.

        Returns:
            List of solutions. Each solution is a list of indexes of rows that will
                exactly cover the given matrix.

        Raises:
            ValueError: Error is raised if given matrix has wrong type.
        """
        if not isinstance(matrix, DLXMatrix):
            raise ValueError("Given matrix can't be processed by DLX algorithm.")
        self._solutions.clear()
        self._search(matrix)
        return self._solutions

    def _search(self, matrix: DLXMatrix, partial: Solution = None) -> None:
        """Perform algorithm X recursively and collect solutions.

        Args:
            matrix: Matrix representation implemented as circular doubly linked lists.
            partial: List including rows collected this far in recursion.
        """
        if not partial:
            partial: Solution = []

        if matrix.right == matrix:
            self._solutions.append(partial[:])
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
        """Find column with smallest number of 1s to minimize the branching factor.

        Args:
            matrix: Matrix representation implemented as circular doubly linked lists.

        Returns:
            Linked list column node representing column with smallest number of 1s.
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
        in column from other column lists rows are in. Covering is done from top to
        bottom and from left to right.

        Args:
            column: Linked list column node.
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

        Uncovering is done from bottom to top and from right to left in order to undo
        steps done during column covering.

        Args:
            Linked list column node.
        """
        row = column.up
        while row != column:
            node = row.left
            while node != row:
                node.attach()
                node = node.left
            row = row.up
        column.attach()


# Add all private methods to pdoc when generating documentation
__pdoc__ = {
    f"DLX.{func}": True
    for func in dir(DLX)
    if callable(getattr(DLX, func)) and func.startswith("_")
}
