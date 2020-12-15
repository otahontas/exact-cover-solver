"""Exact cover matrix implementation with dictionaries and sets."""

from .matrix_base import Matrix
from exact_cover_solver.types import (
    SubsetCollection,
    ProblemData,
    UniverseElement,
    SubsetId,
)
from typing import Dict, Set, Tuple

ColumnValue = Set[SubsetId]
ColumnDict = Dict[UniverseElement, ColumnValue]


class DictMatrix(Matrix):
    """Exact cover matrix implementation with dictionaries and sets."""

    def __init__(self, problem_data: ProblemData) -> None:
        """Initialize matrix with columns dictionary.

        Args:
            problem_data: Data needed to create matrix.
        """
        self._column_dict: ColumnDict = {}
        super().__init__(problem_data)

    def _create(self) -> None:
        """Create dict for universe elements and for subsets where element appears."""
        self._column_dict = {element: set() for element in self._universe}
        for subset_id, subset_elements in self._subset_collection.items():
            for element in subset_elements:
                self._column_dict[element].add(subset_id)

    @property
    def data(self) -> Tuple[ColumnDict, SubsetCollection]:
        """Get created dictionary and original set collection.

        Returns:
            Tuple containing created matrix and set collection used to create matrix.
        """
        return self._column_dict, self._subset_collection
