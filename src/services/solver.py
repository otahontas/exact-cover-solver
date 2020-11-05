"""Solver service, handles different solving modes."""

from datastructures.node import Node, HeaderNode, RootNode
from algos.algorithmX import AlgorithmX


class Solver:
    """Service for solving an exact cover problem from given input."""

    def solve(self, universe, set_collection):
        """Solves exact cover problem.

        Input should be universe of elements (such as numbers from 1 to seven)
        and collection of sets consisting elements from universe."""
        root = self.create_root()
        self.create_headers(root, universe)
        self.create_nodes(root, set_collection)
        algoX = AlgorithmX()
        algoX.solve(root)

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
        """Create nodes representing elements in each set in set collection.


        All sets are iterated through. For each element in set the element is
        linked to the correct column and columns header. Elements in set are
        also linked together to form a circular row.
        """

        def find_header(header_id):
            header = root
            while header.id != header_id:
                header = header.right
            return header

        for set_name, set_elements in set_collection:
            previous = None
            first = None
            for element in set_elements:
                header = find_header(element)
                cell = Node(header, set_name)
                if not header.up and not header.down:
                    header.up = header.down = cell
                    cell.up = cell.down = header
                else:
                    prev_up = header.up
                    prev_up.down = cell
                    cell.up = prev_up
                    cell.down = header
                    header.up = cell
                if previous:
                    previous.right = cell
                    cell.left = previous
                else:
                    first = cell
                previous = cell
                header.increase_count()
            previous.right = first
            first.left = previous
