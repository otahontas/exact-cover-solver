"""Package for data creators.

Defines the interface for data creators for different type of problems, such as
pentomino and sudoku. Also defines custom types used to represent data.
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
    def create_universe_and_set_collection(self) -> Constrains:
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
