"""Solver service, handles different solving modes."""

from datastructures.dlxmatrix import DLXMatrix
from algos.dlx import DLX


class Solver:
    """Service for solving an exact cover problem from given input."""

    def solve(self, universe, set_collection):
        """Solves exact cover problem.

        Input should be universe of elements (such as numbers from 1 to seven)
        and collection of sets consisting elements from universe.
        """
        matrix = DLXMatrix(universe, set_collection)
        dlx = DLX()
        dlx.solve(matrix)
