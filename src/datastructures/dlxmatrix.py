"""DLX matrix implementation based on data objects."""

from .dlxdataobjects import DataObject, ColumnObject


class DLXMatrix:
    def __init__(self, universe, set_collection):
        """Create column and data objects and link them to this matrix object."""
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

    def create_nodes(self, root, set_collection):
        """Create nodes representing elements in each set in set collection.

        All sets are iterated through. For each element in set the element is
        linked to the correct column and columns column. Elements in set are
        also linked together to form a circular row.
        """

        def find_column(_id):
            column = root
            while column.id != _id:
                column = column.right
            return column

        for set_name, set_elements in set_collection:
            previous = None
            first = None
            for element in set_elements:
                column = find_column(element)
                cell = DataObject(column, row=set_name)
                if not column.up and not column.down:
                    column.up = column.down = cell
                    cell.up = cell.down = column
                else:
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
                column.increase_count()
            previous.right = first
            first.left = previous
