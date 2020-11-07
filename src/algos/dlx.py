"""Dancing links implementation for algorithm X."""

from .algos import AlgorithmX


class DLX(AlgorithmX):
    def __init__(self):
        """Set up solution counter."""
        self.solutions = 0
        self.partial = set()

    def solve(self, matrix):
        """Solve exact cover problem and return rows that are chosen in solution."""
        self._search(matrix)

    def _search(self, h):
        """Perform algorithm X recursively."""

        # If R[h] = h, solution has been found
        print("")
        print("=== NEW RECURSION STARTED === ")
        self._print(h)
        print("current partial:", self.partial)
        if h.right == h:
            print("solution found! It includes following rows: ", end=" ")
            for row in self.partial:
                print(row, end=" ")
            print("")
            return

        # Otherwise choose column c optimally
        c = self._choose_optimal_column_object(h)

        # If this column doesn't have 1s, terminate unsuccesfully
        if not c.size:
            return

        # Cover column c
        self._cover(c)

        # Go through rows of column c
        r = c
        while (r := r.down) != c:
            # Include row in partial solution
            self.partial.add(r.row)
            # Cover each column on this row
            j = r
            print("Starting to cover")
            while (j := j.right) != r:
                self._cover(j.header)
            print("After covering")
            self._print(h)
            # Launch new recursive search
            self._search(h)
            # Remove this row from partial solution
            self.partial.remove(r.row)
            # Uncover each column on this row
            print("Starting to uncover")
            j = r
            while (j := j.left) != r:
                self._uncover(j.header)
            print("After uncovering")
            self._print(h)
        # Uncover column c and return
        self._cover(c)

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

        First remove c from the header list and the remove all rows in c's own list
        from other column lists they're in.

        Covering is done from top to bottom and left to right manner.
        """
        c.right.left = c.left
        c.left.right = c.right
        i = c
        while (i := i.down) != c:
            j = i
            while (j := j.right) != i:
                j.down.up = j.up
                j.up.down = j.down
                j.header.size -= 1

    def _uncover(self, c):
        """Uncover given column c

        Unovering is done from bottom to top and right to left manner in order to undo
        deattaches done in covering step.
        """
        i = c
        while (i := i.up) != c:
            j = i
            while (j := j.left) != i:
                j.header.size += 1
                j.up.down = j
                j.down.up = j
        c.left.right = c
        c.right.left = c

    def _print(self, root):
        """Print matrix nodes based on root."""
        header = root.right
        while header != root:
            print(header.id, header.size)
            node = header.down
            while node != header:
                print(node, node.row)
                node = node.down
            header = header.right
