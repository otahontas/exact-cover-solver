"""Solver service, handles different solving modes."""

from datastructures.node import Node, HeaderNode, RootNode


class Solver:
    """Service for solving an exact cover problem from given input."""

    def solve(self, universe, set_collection):
        """Solves exact cover problem.

        Input should be universe of elements (such as numbers from 1 to seven)
        and collection of sets consisting elements from universe."""
        root = self.create_root()
        self.create_headers(root, universe)
        self.create_nodes(root, set_collection)
        return root

    def create_root(self):
        """Create root column."""
        return RootNode()

    def create_headers(self, root, universe):
        """Create header columns and attach them to root."""
        previous = root
        for element in universe:
            header = HeaderNode(element)
            header.left = previous
            previous.right = header
            previous = header
        root.left = previous
        previous.right = root

    def create_nodes(self, root, set_collection):
        """Create nodes representing elements in each set in set collection."""
        for set_name, set_elements in set_collection:
            print("adding set ", set_name)
            for element in set_elements:
                # find correct header node
                header = root
                while header.id != element:
                    header = header.right
                cell = Node(header)
                if header.up is None and header.down is None:
                    # If column is empty, inserting this as first in column
                    header.up = header.down = cell
                    cell.up = cell.down = header
                else:
                    # Column not empty, inserting as last
                    prev_up = header.up
                    prev_up.down = cell
                    cell.up = prev_up
                    cell.down = header
                    header.up = cell
