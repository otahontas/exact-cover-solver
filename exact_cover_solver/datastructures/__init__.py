"""Package for custom datastructures."""
from abc import ABC, abstractmethod
from typing import TypeVar

from exact_cover_solver.types import Constrains


class Matrix(ABC):
    """Base class for matrix used by algorithm X implementations."""

    def __init__(self, constrains: Constrains) -> None:
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

# Add all private methods to pdoc when generating documentation
__pdoc__ = {
    f"Matrix.{func}": True
    for func in dir(Matrix)
    if callable(getattr(Matrix, func)) and func.startswith("_")
}
