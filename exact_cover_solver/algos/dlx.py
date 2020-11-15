"""Dancing links implementation for algorithm X."""

from exact_cover_solver.algos import AlgorithmX
from copy import copy


class DLX(AlgorithmX):
    """Dancing links implementation for algorithm X."""

    def __init__(self):
        """Set up solution counter."""
        self.solutions = []
        self.partial = set()

    def solve(self, matrix):
        """Solve exact cover problem"""
        self._search(matrix)

    def _search(self, h):
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
        if h.right == h:
            self.solutions.append(copy(self.partial))
            return

        c = self._choose_optimal_column_object(h)

        if not c.size:
            return

        self._cover(c)

        r = c
        while (r := r.down) != c:
            self.partial.add(r.row)
            j = r
            while (j := j.right) != r:
                self._cover(j.column)
            self._search(h)
            while (j := j.left) != r:
                self._uncover(j.column)
            self.partial.remove(r.row)
        self._uncover(c)

    @staticmethod
    def _choose_optimal_column_object(h):
        """Find column with smallest number of 1s.

        This is done to minimize the branching factor.
        """
        j = h.right
        c = j
        s = j.size
        while (j := j.right) != h:
            c, s = (j, j.size) if j.size < s else (c, s)
        return c

    @staticmethod
    def _cover(c):
        """Cover given column c.

        First remove c from the header list and then remove all rows in c's own list
        from other column lists they're in.

        Covering is done from top to bottom and left to right manner.
        """
        c.detach()
        i = c
        while (i := i.down) != c:
            j = i
            while (j := j.right) != i:
                j.detach()

    @staticmethod
    def _uncover(c):
        """Uncover given column c.

        Uncovering is done from bottom to top and right to left manner in order to undo
        covering steps.
        """
        i = c
        while (i := i.up) != c:
            j = i
            while (j := j.left) != i:
                j.attach()
        c.attach()
