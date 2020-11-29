"""Dictionary based implementation for algorithm X."""

from typing import List

from exact_cover_solver.algos import AlgorithmX, Solution
from exact_cover_solver.data_creators import SetCollection
from exact_cover_solver.datastructures.dictmatrix import (
    DictMatrix,
    ColumnDict,
    ColumnValue,
)


class DictX(AlgorithmX):
    """Dictionary based implementation for algorithm X."""

    def __init__(self) -> None:
        super().__init__()

    def solve(self, matrix: AlgorithmX[DictMatrix]) -> List[Solution]:
        """Solve which rows cover the given matrix.

        Clears solutions bookkeeping from previous runs, then calls
        recursive method.

        Args:
            matrix: Matrix representation implemented with dictionaries and sets.

        Returns:
            List of solutions. Each solution is a list of indexes of rows that will
                exactly cover the given matrix.

        Raises:
            ValueError: Error is raised if given matrix has wrong type.
        """
        if not isinstance(matrix, DictMatrix):
            raise ValueError("Given matrix can't be processed by DictX algorithm.")
        self._solutions.clear()
        column_dict, set_collection = matrix.data
        self._search(column_dict, set_collection)
        return self._solutions

    def _search(
        self,
        column_dict: ColumnDict,
        set_collection: SetCollection,
        partial: Solution = None,
    ) -> None:
        """Perform algorithm X recursively and collect solutions.

        Args:
            column_dict: Matrix representation as a dictionary.
            set_collection: Original set collection used to create the matrix.
            partial: List including rows collected this far in recursion.
        """
        if not partial:
            partial: Solution = []

        if not column_dict:
            self._solutions.append(partial)
            return

        column = self._choose_optimal_column(column_dict)
        for row in column_dict[column]:
            partial.append(row)
            removed_columns = self._cover(column_dict, set_collection, row)
            self._search(column_dict, set_collection, partial)
            self._uncover(column_dict, set_collection, row, removed_columns)
            partial.pop()

    @staticmethod
    def _choose_optimal_column(column_dict: ColumnDict) -> int:
        """Find column with smallest size to minimize the branching factor.

        Args:
            column_dict: Dictionary of each column on current iteration.

        Returns:
            Key of optimal column.
        """
        key, size = 0, len(column_dict[0])
        for column, content in column_dict.items():
            key, size = (column, len(content)) if len(content) > size else (key, size)
        return key

    @staticmethod
    def _cover(
        column_dict: ColumnDict, set_collection: SetCollection, set_index: int
    ) -> List[ColumnValue]:
        """Cover columns in given set.

        Go through each element in given set and for each row where element is present,
        remove all other elements. Then remove column representing iterated element
        from column dictionary.

        Args:
            column_dict: Matrix representation as a dictionary
            set_collection: Original set collection used to create the matrix
            set_index: Which set elements to cover

        Returns:
            List including sets that have been removed from column dict.
        """
        removed_columns = []
        for element in set_collection[set_index]:
            for row in column_dict[element]:
                for other_element in set_collection[row]:
                    if other_element != element:
                        column_dict[other_element].remove(row)
            removed_columns.append(column_dict.pop(element))
        return removed_columns

    @staticmethod
    def _uncover(
        column_dict: ColumnDict,
        set_collection: SetCollection,
        set_index: int,
        removed_columns: List[ColumnValue],
    ) -> None:
        """Uncover columns.

        Restores removed columns in reversed order to dictionary.
        Args:
            column_dict: Matrix representation as a dictionary
            set_collection: Original set collection used to create the matrix
            set_index: Which set elements to uncover
            removed_columns: Columns removed while covering set
        """
        for counter, element in enumerate(reversed(set_collection[set_index])):
            index = len(removed_columns) - 1 - counter
            column_dict[element] = removed_columns[index]
            for row in column_dict[element]:
                for other_element in set_collection[row]:
                    if other_element != element:
                        column_dict[other_element].add(row)


# Add all private methods to pdoc when generating documentation
__pdoc__ = {
    f"DictX.{func}": True
    for func in dir(DictX)
    if callable(getattr(DictX, func)) and func.startswith("_")
}
