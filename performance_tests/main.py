"""Test finding all solutions for different pentomino boards with dlx.

Correct solution amounts are from wikipedia:
https://en.wikipedia.org/wiki/Pentomino#Constructing_rectangular_dimensions
"""

from exact_cover_solver.services.solver import Solver
import time


def generate_pentomino_board_solutions(
    algo, board_height: int, board_width: int, correct_amount: int
) -> None:
    """Test that 6x10 board gets correct amount of solutions."""
    solver = Solver()
    solver.algorithm = algo
    start_time = time.time()
    browser = solver.solve_pentomino_problem(board_height, board_width)
    solutions = browser._solutions
    time_solving = time.time() - start_time
    print(
        f"There should be {correct_amount} solutions for {board_height}x{board_width} "
        f"board. Algorithm found {len(solutions)} solutions in {time_solving} secs."
    )


generate_pentomino_board_solutions("DLX", 3, 20, 2)
generate_pentomino_board_solutions("DLX", 4, 15, 368)
generate_pentomino_board_solutions("DLX", 5, 12, 1010)
generate_pentomino_board_solutions("DLX", 6, 10, 2339)

generate_pentomino_board_solutions("DictX", 3, 20, 2)
generate_pentomino_board_solutions("DictX", 4, 15, 368)
generate_pentomino_board_solutions("DictX", 5, 12, 1010)
generate_pentomino_board_solutions("DictX", 6, 10, 2339)
