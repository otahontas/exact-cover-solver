class AlgorithmX:
    def solve(self, root):
        """Solve exact cover problem and return rows that are chosen in solution."""
        self._search(root)

    def _search(self, root, partial=[]):
        """jee"""

        # Check if we have a solution, return if so
        if root.right == root:
            print("solution found, it includes following rows:")
            for row in partial:
                print(row, end="")
            print("")
            return

        # Find header
        header = self._find_column_with_lowest_ones(root)

        # Check if header count is zero
        if not header.size:
            print("\n === No ones in this column, returning ===")
            return

        # first one
        row_node = header.down
        new_partial = partial[:]
        new_partial.append(row_node.row)

        covered = self._cover(row_node, root)
        self._print(root)  # check
        self._search(root, new_partial)
        for node in covered:
            node.deattach()

        # second one
        row_node = row_node.down
        new_partial = partial[:]
        new_partial.append(row_node.row)

        covered = self._cover(row_node, root)
        self._print(root)  # check
        self._search(root, new_partial)
        for node in covered:
            node.deattach()


    def _cover(self, start_node, root):
        """Cover.
        For each column in this row, deattach column and for each cell in deattached
        column, deattach row.
        """
        covered = []  # for now put covered in list
        curr_node = start_node
        while True:
            tmp1 = curr_node
            while tmp1 != curr_node.header:
                tmp2 = tmp1
                while tmp2.right != tmp2:
                    tmp2.deattach()
                    covered.append(tmp2)
                    tmp2 = tmp2.right
                tmp2.deattach()
                covered.append(tmp2)
                tmp1 = tmp1.down
            curr_node.header.deattach()
            covered.append(curr_node.header)
            if curr_node.right is curr_node:
                break
            curr_node = curr_node.right
        return covered

    def _uncover(self, start_node, root):
        raise NotImplementedError

    def _find_column_with_lowest_ones(self, root):
        """Loop through columns to find column with lowest ones."""
        curr = root.right
        col = curr
        size = curr.size
        while curr != root:
            col, size = (curr, curr.size) if curr.size < size else (col, size)
            curr = curr.right
        return col

    def _print(self, root):
        """Print matrix nodes based on root."""
        print("\n=== Situation ===")
        header = root.right
        while header != root:
            print(header.id, header.size)
            node = header.down
            while node != header:
                print(node, node.row)
                node = node.down
            header = header.right
