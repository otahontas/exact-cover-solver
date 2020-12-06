"""Abstract base and types for algorithm X implementations.

Algorithm X is a straightforward recursive, nondeterministic, depth-first and
backtracking algorithm.
"""

from abc import ABC, abstractmethod
from typing import List, Generic
from exact_cover_solver.datastructures import GenericMatrix

Solution = List[int]


class AlgorithmX(ABC, Generic[GenericMatrix]):
    """Abstract base class for algorithm X.

    Attributes:
        _solutions: List for solutions algorithm produces.
    """

    def __init__(self) -> None:
        """Initialize with empty solution counter."""
        self._solutions: List[Solution] = []

    @abstractmethod
    def solve(self, matrix: GenericMatrix) -> List[Solution]:
        """Abstract solving method that should be implemented by a subclass.

        Args:
            matrix: Exact cover problem matrix that can be consumed by a subclass.

        Returns:
            List of solutions algorithm has produced.

        Raises:
            NotImplementedError: abstract method was directly called.
        """
        raise NotImplementedError