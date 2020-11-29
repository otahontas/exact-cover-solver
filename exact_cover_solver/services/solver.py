"""Solver service, handles different solving modes."""

from typing import Optional

from exact_cover_solver.algos import AlgorithmX
from exact_cover_solver.algos.dictx import DictX
from exact_cover_solver.algos.dlx import DLX
from exact_cover_solver.data_creators.generic_creator import GenericCreator
from exact_cover_solver.data_creators.pentomino_creator import PentominoCreator
from exact_cover_solver.datastructures.dictmatrix import DictMatrix
from exact_cover_solver.datastructures.dlxmatrix import DLXMatrix
from exact_cover_solver.services.pentomino_browser import PentominoBoardBrowser


class AlgorithmNotChosenError(Exception):
    """Exception raised when algorithm is not chosen.

    Attributes:
        message -- explanation of the error
    """

    def __init__(self, message="Algorithm is not chosen."):
        """Initialize error with message."""
        self.message = message
        super().__init__(self.message)


class Solver:
    """Class for solving an exact cover problem from given input.

    Algorithms list define possible algorithms used by class instances.
    """

    _algorithms = [DLX, DictX]
    _matrices = {"DLX": DLXMatrix, "DictX": DictMatrix}

    def __init__(self):
        """Initialize algorithm variable."""
        self._algorithm: Optional[AlgorithmX] = None

    @property
    def algorithm(self) -> Optional[str]:
        """Maintain a reference to one of the algorithm X objects.

        Returns:
            Name of the algorithm currently in use.

        Raises:
            AlgorithmNotChosenError: Raised if algorithm not chosen.
        """
        if not self._algorithm:
            raise AlgorithmNotChosenError
        return self._algorithm.__class__.__name__

    @algorithm.setter
    def algorithm(self, algorithm_name: str) -> None:
        """Replace algorithm object at runtime.

        Try to filter correct algorithm class, then create instance of that class.

        Args:
            algorithm_name: Name of the algorithm to be used
        """
        try:
            algo_class = next(
                algo_class
                for algo_class in self._algorithms
                if algo_class.__name__ == algorithm_name
            )
        except StopIteration:
            valid_names = [algo_class.__name__ for algo_class in self._algorithms]
            raise ValueError(
                f"Algorithm {algorithm_name} is not valid algorithm. "
                f"Valid algorithms are: {valid_names}"
            )
        self._algorithm = algo_class()

    def solve_generic_problem(self, universe: str, set_collection: str) -> str:
        """Parse given data, solve cover problem and format solution to string.

        Args:
            universe: used universe
            set_collection: set collection based on universe elements

        Returns:
            Solution formatted as printable string.
        """
        if not self._algorithm:
            raise AlgorithmNotChosenError
        generic_creator = GenericCreator(universe, set_collection)
        constrains = generic_creator.create_constrains()
        matrix_class = self._matrices[self.algorithm]
        solutions = self._algorithm.solve(matrix_class(constrains))
        if not solutions:
            return "No solutions found with given universe and set collection."
        formatted_solution = (
            f"For given set_collection: {set_collection} you can "
            f"create exact cover solution by following ways:\n"
        )
        for solution in solutions:
            formatted_solution = f"{formatted_solution}Choose rows: {solution}\n"
        return formatted_solution

    def solve_pentomino_problem(
        self, board_height: int, board_width: int
    ) -> PentominoBoardBrowser:
        """Generate needed data, solve cover problem and return solution browser.

        Args:
            board_height: Height of the pentomino board
            board_width: Width of the pentomino board

        Returns:
            PentominoBoardBrowser which can be used to browse generated solutions.
        """
        if not self._algorithm:
            raise AlgorithmNotChosenError
        pentomino_creator = PentominoCreator()
        pentomino_creator.change_board_size(board_height, board_width)
        constrains = pentomino_creator.create_constrains()
        matrix_class = self._matrices[self.algorithm]
        solutions = self._algorithm.solve(matrix_class(constrains))
        return PentominoBoardBrowser(pentomino_creator, solutions)
