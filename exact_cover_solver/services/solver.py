"""Solver service, handles different solving modes."""

from typing import Optional, List

from exact_cover_solver.algos import AlgorithmX, Solution
from exact_cover_solver.algos.dlx import DLX


class Solver:
    """Class for solving an exact cover problem from given input."""

    def __init__(self):
        """Initialize algorithm."""
        self.__algorithm: Optional[AlgorithmX] = DLX()
        self.__problem: Optional[str] = None

    @property
    def algorithm(self) -> Optional[str]:
        """Maintain a reference to one of the algoX objects.

        Returns algo name when asked.

        Concrete class is set during runtime.
        """
        if isinstance(self.__algorithm, DLX):
            return "dlx"
        return None

    @algorithm.setter
    def algorithm(self, algorithm_name: str) -> None:
        """Replace algorithm object at runtime."""
        if algorithm_name == "dlx":
            self.__algorithm = DLX()
        else:
            raise ValueError("Algorithm not valid")

    @property
    def problem(self) -> str:
        """Maintain reference to problem."""
        return self.__problem

    @problem.setter
    def problem(self, problem: str) -> None:
        """Replace algorithm object at runtime."""
        if problem == "pentomino":
            self.__problem = problem
        else:
            raise ValueError("Problem not valid")

    def solve(self, board_height, board_width) -> List[Solution]:
        """Solves exact cover problem, input should correspond to current algo used."""
        pass
        # if self.__problem == "pentomino":
        #     pg = PentominoGenerator()
        #     universe, set_collection =
        #     pg.create_universe_and_set_collections(board_height, board_width)
        #     matrix = DLXMatrix(universe, set_collection)
        #     return self.__algorithm.solve(matrix)
        # else:
        #     raise ValueError("Not possible to solve, something is not right")
