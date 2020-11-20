"""Wrappers to represent dancing links data and column objects as matrix."""

from exact_cover_solver.datastructures.dlxdataobjects import DataObject, ColumnObject


class DLXMatrix:
    """Matrix representation and initialization methods for circular linked lists."""

    def __init__(self, universe, set_collection):
        """Create column and data objects and link them to this matrix object."""
        if not universe or not set_collection:
            raise ValueError("Not possible to create matrix without universe or sets.")

        self.id = "root"
        self.create_columns(universe)
        self.create_nodes(set_collection)

    def create_columns(self, universe):
        """Create column columns and attach them to root."""
        previous = self
        for element in universe:
            column = ColumnObject(_id=element)
            column.left = previous
            previous.right = column
            previous = column
        self.left = previous
        previous.right = self

    def create_nodes(self, set_collection):
        """Create nodes representing elements in each set in set collection.

        All sets are iterated through. For each element in set the element is
        linked to the correct column and columns column. Elements in set are
        also linked together to form a circular row.
        """

        def find_column(_id):
            """Find column with given id."""
            correct_column = self
            while correct_column.id != _id:
                correct_column = correct_column.right
            return correct_column

        for set_name, set_elements in set_collection:
            previous = None
            first = None
            for element in set_elements:
                column = find_column(element)
                cell = DataObject(column, row=set_name)
                prev_up = column.up
                prev_up.down = cell
                cell.up = prev_up
                cell.down = column
                column.up = cell
                if previous:
                    previous.right = cell
                    cell.left = previous
                else:
                    first = cell
                previous = cell
                column.size += 1
            previous.right = first
            first.left = previous

    def __repr__(self):
        """Return printable representation of matrix."""
        s = ""
        column = self.right
        while column != self:
            data = column.down
            data_str = ""
            while data != column:
                data_str = f"{data_str} {data.row}"
                data = data.down
            s = f"{s}Column {column.id} has {column.size} objects:{data_str}\n"
            column = column.right
        return s
