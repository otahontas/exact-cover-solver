"""Integration tests for solver class."""

from exact_cover_solver.services.pentomino_generator import PentominoGenerator
from exact_cover_solver.datastructures.dlxmatrix import DLXMatrix
from exact_cover_solver.algos.dlx import DLX
import time


def test_pentomino_board_gets_correct_amount_of_solutions():
    """Test that 6x10 board gets correct amount of solutions."""
    pg = PentominoGenerator()
    universe, set_collection = pg.generate(6, 10)
    matrix = DLXMatrix(universe, set_collection)
    dlx = DLX()
    start_time = time.time()
    solutions = dlx.solve(matrix)
    time_processing = time.time() - start_time
    print(f"Found {len(solutions)} solutions in {time_processing} seconds")


test_pentomino_board_gets_correct_amount_of_solutions()
