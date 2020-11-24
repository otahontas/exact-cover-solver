"""Package for custom datastructures."""
from abc import ABC, abstractmethod
from typing import TypeVar

from exact_cover_solver.data_creators import Universe, SetCollection


class Matrix(ABC):
    """Base class for matrix used by algorithm X implementations."""

    def __init__(self, universe: Universe, set_collection: SetCollection) -> None:
        """Initialize matrix details and call column and node creator methods.

        Args:
            universe: a list of integers representing some set of elements
            set_collection: a list of lists, each made from integers in the universe

        Raises:
            ValueError: Error is raised if universe or set_collection is empty.
        """
        if not universe:
            raise ValueError("Not possible to create matrix with empty universe.")
        if not set_collection:
            raise ValueError("Not possible to create matrix with empty set collection.")
        self.id = "root"
        self._universe = universe
        self._set_collection = set_collection
        self._create_columns()
        self._create_nodes()

    @abstractmethod
    def _create_columns(self) -> None:
        """Abstract method that should be implemented by subclass.

        Raises:
            NotImplementedError: Error is raised if this abstract method is called
                directly.
        """
        raise NotImplementedError

    @abstractmethod
    def _create_nodes(self) -> None:
        """Abstract method that should be implemented by subclass.

        Raises:
            NotImplementedError: Error is raised if this abstract method is called
                directly.
        """
        raise NotImplementedError


GenericMatrix = TypeVar("GenericMatrix", bound=Matrix)
