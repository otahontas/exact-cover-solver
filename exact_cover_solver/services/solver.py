"""Solver service, handles different solving modes."""

from exact_cover_solver.datastructures.dlxmatrix import DLXMatrix
from exact_cover_solver.algos import AlgorithmX, Solution

from typing import Optional, List


class Solver:
    """Class for solving an exact cover problem from given input."""

    def __init__(self):
        """Initialize algorithm."""
        self.__algorithm: Optional[AlgorithmX] = None

    @property
    def algorithm(self) -> AlgorithmX:
        """Maintain a reference to one of the algoX objects.

        Concrete class is set during runtime.
        """
        return self.__algorithm

    @algorithm.setter
    def algorithm(self, algorithm: AlgorithmX) -> None:
        """Replace algorithm object at runtime."""
        self.__algorithm = algorithm

    def solve(self, data: DLXMatrix) -> List[Solution]:
        """Solves exact cover problem, input should correspond to current algo used."""
        return self.__algorithm.solve(data)
