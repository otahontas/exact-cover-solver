"""Abstract base and types for data creator implementations.

Data creators are used to generate exact cover data for different types of problems,
such as finding Pentomino tilings and solving Sudoku.
"""

from abc import ABC, abstractmethod
from typing import List, Tuple

Universe = List[int]
SetCollection = List[List[int]]
Constrains = Tuple[Universe, SetCollection]


class DataCreator(ABC):
    """Abstract base class for data creator.

    Creator generates universe and collection of sets that together represent some
    problem reduced to exact cover problem.
    """

    @abstractmethod
    def create_constrains(self) -> Constrains:
        """Abstract creator method that should be implemented by a subclass.

        Returns:
            Tuple containing:
                - universe, a list of integers representing some set of elements
                - collection of sets, a list of lists, each made from integers in
                    the universe

        Raises:
            NotImplementedError: Error is raised if this abstract method is called
                directly.
        """
        raise NotImplementedError
