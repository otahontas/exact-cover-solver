"""Dancing links implementation for algorithm X."""

from exact_cover_solver.algos import AlgorithmX, Solution
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

        c = self._choose_optimal_column_object(matrix)

        if not c.size:
            return

        self._cover(c)

        r = c.down
        while r != c:
            partial.append(r.row)
            j = r.right
            while j != r:
                self._cover(j.column)
                j = j.right
            self._search(matrix, partial)
            j = r.left
            while j != r:
                self._uncover(j.column)
                j = j.left
            partial.pop()
            r = r.down
        self._uncover(c)

    @staticmethod
    def _choose_optimal_column_object(matrix: DLXMatrix) -> ColumnObject:
        """Find column with smallest number of 1s.

        This is done to minimize the branching factor.
        """
        j = matrix.right
        c = j
        s = j.size
        while j != matrix:
            c, s = (j, j.size) if j.size < s else (c, s)
            j = j.right
        return c

    @staticmethod
    def _cover(c: ColumnObject) -> None:
        """Cover given column c.

        First remove c from the header list and then remove all rows in c's own list
        from other column lists they're in.

        Covering is done from top to bottom and left to right manner.
        """
        c.detach()
        i = c.down
        while i != c:
            j = i.right
            while j != i:
                j.detach()
                j = j.right
            i = i.down

    @staticmethod
    def _uncover(c: ColumnObject) -> None:
        """Uncover given column c.

        Uncovering is done from bottom to top and right to left manner in order to undo
        covering steps.
        """
        i = c.up
        while i != c:
            j = i.left
            while j != i:
                j.attach()
                j = j.left
            i = i.up
        c.attach()
