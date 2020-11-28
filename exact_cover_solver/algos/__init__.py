"""Package for algorithms.

Defines the interface for algorithm X implementations and custom types used in
this package.
"""

from abc import ABC, abstractmethod
from typing import List, Generic, Optional
from exact_cover_solver.datastructures import GenericMatrix

Solution = List[int]


class AlgorithmX(ABC, Generic[GenericMatrix]):
    """Abstract base class for algorithm X that solves the exact cover problem.

    Algorithm X is a straightforward recursive, nondeterministic, depth-first
    and backtracking algorithm.
    """

    def __init__(self) -> None:
        """Initialize with empty solution counter and matrix."""
        self._solutions: List[Solution] = []
        self._matrix: Optional[GenericMatrix] = None

    @abstractmethod
    def solve(self, matrix: GenericMatrix) -> List[Solution]:
        """Abstract solving method that should be implemented by a subclass.

        Args:
            matrix: Representation of an exact cover problem matrix that can be consumed
                by a subclass.

        Returns:
            List of solutions. Each solution is a list of indexes of rows that will
                exactly cover the given matrix.

        Raises:
            NotImplementedError: Error is raised if this abstract method is called
                directly.
        """
        raise NotImplementedError
