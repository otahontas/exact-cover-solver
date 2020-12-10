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

    def __init__(self, constrains: ProblemData) -> None:
        """Initialize matrix details and call column and node creator methods.

        Args:
            constrains: Tuple containing universe and set collection.

        Raises:
            ValueError: Error is raised if universe or set_collection is empty or
                tuple doesn't contain enough information.
        """
        try:
            universe, set_collection = constrains
        except ValueError:
            raise ValueError("Constrains should contain universe and set_collection.")
        if not universe:
            raise ValueError("Not possible to create with empty universe.")
        if not set_collection:
            raise ValueError("Not possible to create with empty set collection.")
        self.id = "root"
        self._universe = universe
        self._set_collection = set_collection
        self._create()

    @abstractmethod
    def _create(self) -> None:
        """Abstract matrix creating method that should be implemented by subclass.

        Raises:
            NotImplementedError: Error is raised if this abstract method is called
                directly.
        """
        raise NotImplementedError


GenericMatrix = TypeVar("GenericMatrix", bound=Matrix)
