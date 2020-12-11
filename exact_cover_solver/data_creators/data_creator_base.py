"""Abstract base for data creator implementations.

Data creators are used to generate exact cover data for different types of problems,
such as finding Pentomino tilings and solving Sudoku.
"""

from abc import ABC, abstractmethod
from typing import Any

from exact_cover_solver.types import ProblemData


class DataCreator(ABC):
    """Abstract base class for data creator."""

    @abstractmethod
    def create_problem_data(self, *args: Any, **kwargs: Any) -> ProblemData:
        """Abstract creator method that should be implemented by a subclass.

        Args:
            args: Any non-keyword arguments implemented method takes
            kwargs: Any keyword arguments implemented method takes

        Returns:
            Data that can be used to create exact cover problem matrix.

        Raises:
            NotImplementedError: Error is raised if this abstract method is called
                directly.
        """
        raise NotImplementedError
