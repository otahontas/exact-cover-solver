"""Solver service, handles different solving modes."""
from typing import List

from .pentomino_browser import PentominoBoardBrowser
from exact_cover_solver.algos import DictX, DLX
from exact_cover_solver.data_creators import (
    PentominoCreator,
    SudokuCreator,
    SudokuInput,
)
from exact_cover_solver.datastructures import DictMatrix, DLXMatrix
from exact_cover_solver.types import Solution, ProblemData


class Solver:
    """Class for solving an exact cover problem from given input."""

    def solve_generic_problem(
        self, algorithm: str, problem_data: ProblemData
    ) -> List[Solution]:
        """Parse given data, solve cover problem and format solution to string.

        Args:
            algorithm: Name of the algorithm to use
            problem_data: Data needed to create an exact cover problem matrix. Should
                          be a tuple containing list of universe elements and dictionary
                          containing subsets with unique ids as keys and list of
                          subset elements as values.

        Returns:
            List of solutions, each solution having a list of ids identifying which
            subsets were picked to solution.
        """
        solutions = self._solve(algorithm, problem_data)
        # TODO: return solutions formatted with original data
        return solutions

    def solve_pentomino_problem(
        self, algorithm: str, board_height: int, board_width: int
    ) -> PentominoBoardBrowser:
        """Generate needed data, solve cover problem and return solution browser.

        Args:
            algorithm: Name of the algorithm to use
            board_height: Height of the pentomino board
            board_width: Width of the pentomino board

        Returns:
            PentominoBoardBrowser which can be used to browse generated solutions.
        """
        pentomino_creator = PentominoCreator()
        problem_data = pentomino_creator.create_problem_data(board_height, board_width)
        solutions = self._solve(algorithm, problem_data)
        return PentominoBoardBrowser(pentomino_creator, solutions)

    def solve_sudoku_problem(
        self, algorithm: str, sudoku_input: SudokuInput
    ) -> List[Solution]:
        """Generate needed data, solve cover problem and return solutions.

        Args:
            algorithm: Name of the algorithm to use
            sudoku_input: Two-dimensional sudoku board, where empty cells are marked
                          with zero and other cells have preselected numbers.

        Returns:
            List of solutions, each solution having a list of ids identifying which
            subsets were picked to solution.
        """
        sudoku_creator = SudokuCreator()
        problem_data = sudoku_creator.create_problem_data(sudoku_input)
        solutions = self._solve(algorithm, problem_data)
        # TODO: return sudokuboard browser
        return solutions

    @staticmethod
    def _solve(algorithm: str, problem_data: ProblemData) -> List[Solution]:
        """Solve exact cover problem.

        Args:
            algorithm: Name of the algorithm to use
            problem_data: Data needed to create an exact cover problem matrix.

        Returns:
            List of solutions, each solution having a list of ids identifying which
            subsets were picked to solution.

        Raises:
            ValueError: There's no algorithm with the given name.
        """
        if algorithm == "DLX":
            return DLX().solve(DLXMatrix(problem_data))
        elif algorithm == "DictX":
            return DictX().solve(DictMatrix(problem_data))
        else:
            valid_names = ["DLX", "DictX"]
            raise ValueError(
                f"Algorithm {algorithm} is not valid algorithm. "
                f"Valid algorithms are: {valid_names}"
            )
