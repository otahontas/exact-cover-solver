class AlgorithmX:
    def solve(self, root):
        """Solve exact cover problem and return rows that are chosen in solution."""
        self._recurse(root)

    def _recurse(self, root):
        """jee"""
        header = self._find_column_with_lowest_ones(root)

        # Select row  and add it to partial solution
        = header.down

        # For each column in this row, deattach column and for each cell in deattached
        # column, deattach row
        selected = node

        header_of_selected = node.header
        while selected != header_of_selected:
            row_node = selected.right
            while row_node != selected:
                row_node.deattach()
                row_node = row_node.right
            selected.deattach()
            selected = selected.down


        # deattach header columns
        #node.header.deattach()
        #node = node.right
        #while node.header != header:
        #    node.header.deattach()
        #    node = node.right


        # check
        header = root.right
        while header != root:
            print(header.id, header.size)
            # print whats in column
            node = header.down
            while node != header:
                print(node, node.row)
                node = node.down
            header = header.right


    def _find_column_with_lowest_ones(self, root):
        """Loop through columns to find column with lowest ones."""
        curr = root.right
        col = curr
        size = curr.size
        while curr != root:
            col, size = (curr, curr.size) if curr.size < size else (col, size)
            curr = curr.right
        return col
