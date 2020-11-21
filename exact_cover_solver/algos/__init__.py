"""Package for algorithms, defines interface for algorithm X implementations."""

from abc import ABC, abstractmethod
from typing import Any


class AlgorithmX(ABC):
    """Abstract base class for algorithm X for solving the exact cover problem.

    Algorithm X is a straightforward recursive, nondeterministic, depth-first
    and backtracking algorithm, implemented usually with dancing links technique.
    """

    @abstractmethod
    def solve(self, *args, **kwargs) -> Any:
        """Abstract solving method that should be implemented by subclasses."""
