"""Abstract base for exact cover matrix implementations.

Matrix is an incidence matrix, i.e. a representation of exact cover problem set elements
as columns and possible subsets as rows. When subset at row x has element y in it,
matrix(x,y) will be 1, otherwise 0.
"""
from abc import ABC, abstractmethod
from typing import TypeVar

from exact_cover_solver.types import ProblemData


class Matrix(ABC):
    """Base class for matrix used by algorithm X implementations."""

    def __init__(self, problem_data: ProblemData) -> None:
        """Initialize matrix details and call column and node creator methods.

        Args:
            problem_data: Data needed to create an exact cover problem matrix.
        """
        universe, subset_collection = self._validate_problem_data(problem_data)
        self._universe = universe
        self._subset_collection = subset_collection
        self._create()

    @staticmethod
    def _validate_problem_data(problem_data: ProblemData) -> ProblemData:
        """Check that given universe and subset collection are valid.

        Args:
            problem_data: Data needed to create an exact cover problem matrix.

        Raises:
            ValueError: if data is invalid for some reason.
        """
        universe, subset_collection = problem_data
        if not universe:
            raise ValueError("Not possible to create matrix with empty universe.")
        if not subset_collection:
            raise ValueError(
                "Not possible to create matrix with empty subset collection."
            )
        universe_set = set(universe)
        if len(universe_set) != len(universe):
            raise ValueError("Universe should only have unique elements.")
        for subset in subset_collection.values():
            print(subset)
            if len(set(subset)) != len(subset):
                raise ValueError("Subset should only have unique elements.")
            if any(element not in universe_set for element in subset):
                raise ValueError(
                    f"Some elements in subset {subset} are not elements "
                    "of the universe."
                )
        return universe, subset_collection

    @abstractmethod
    def _create(self) -> None:
        """Abstract matrix creating method that should be implemented by subclass.

        Raises:
            NotImplementedError: Error is raised if this abstract method is called
                directly.
        """
        raise NotImplementedError


GenericMatrix = TypeVar("GenericMatrix", bound=Matrix)
