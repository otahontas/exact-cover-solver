"""Integration tests for solver class."""

from exact_cover_solver.services.pentomino_generator import PentominoGenerator
from exact_cover_solver.datastructures.dlxmatrix import DLXMatrix
from exact_cover_solver.algos.dlx import DLX


def test_pentomino_board_gets_correct_amount_of_solutions():
    pg = PentominoGenerator(6, 10)
    universe, set_collection = pg.generate()
    matrix = DLXMatrix(universe, set_collection)
    dlx = DLX()
    dlx.solve(matrix)
    assert len(dlx.solutions) == 2339
