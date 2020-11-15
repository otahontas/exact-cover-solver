"""Solver service, handles different solving modes."""

from exact_cover_solver.datastructures.dlxmatrix import DLXMatrix
from exact_cover_solver.algos.dlx import DLX


class Solver:
    """Service for solving an exact cover problem from given input."""

    @staticmethod
    def solve(universe, set_collection):
        """Solves exact cover problem.

        Input should be universe of elements (such as numbers from 1 to seven)
        and collection of sets consisting elements from universe.
        """
        matrix = DLXMatrix(universe, set_collection)
        dlx = DLX()
        dlx.solve(matrix)
