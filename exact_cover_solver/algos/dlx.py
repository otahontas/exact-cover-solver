"""Dancing links implementation for algorithm X."""

from exact_cover_solver.algos import AlgorithmX
from copy import copy
import time


class DLX(AlgorithmX):
    """Dancing links implementation for algorithm X."""

    def __init__(self):
        """Set up solution counter."""
        self.solutions = []
        self.partial = set()

    def solve(self, matrix):
        """Solve exact cover problem."""
        self._search(matrix)

    def _iterative_search(self, h):
        """Perform algorithm X iteratively.

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

        stack = []
        stack.append(("top", None, None))
        while stack:
            state, r, c = stack.pop()
            if state == "top":
                if h.right == h:
                    self.solutions.append(copy(self.partial))
                else:
                    c = self._choose_optimal_column_object(h)
                    if c.size:
                        self._cover(c)
                        r = c
                        stack.append(("loop_start", r, c))
            if state == "loop_start":
                r = r.down
                if r == c:
                    self._uncover(c)
                else:
                    self.partial.add(r.row)
                    j = r
                    while (j := j.right) != r:
                        self._cover(j.column)
                    stack.append(("loop_middle", r, c))
                    stack.append(("top", None, None))
            if state == "loop_middle":
                j = r
                while (j := j.left) != r:
                    self._uncover(j.column)
                self.partial.remove(r.row)
                stack.append(("loop_start", r, c))

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

    def _choose_optimal_column_object(self, h):
        """Find column with smallest number of 1s.

        This is done to minimize the branching factor.
        """
        j = h.right
        c = j
        s = j.size
        while (j := j.right) != h:
            c, s = (j, j.size) if j.size < s else (c, s)
        return c

    def _cover(self, c):
        """Cover given column c.

        First remove c from the header list and then remove all rows in c's own list
        from other column lists they're in.

        Covering is done from top to bottom and left to right manner.
        """
        c.deattach()
        i = c
        while (i := i.down) != c:
            j = i
            while (j := j.right) != i:
                j.deattach()

    def _uncover(self, c):
        """Uncover given column c.

        Unovering is done from bottom to top and right to left manner in order to undo
        deattaches done in covering step.
        """
        i = c
        while (i := i.up) != c:
            j = i
            while (j := j.left) != i:
                j.attach()
        c.attach()
