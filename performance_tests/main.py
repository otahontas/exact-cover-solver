"""Test finding all solutions for different pentomino boards with dlx.

Correct solution amounts are from wikipedia:
https://en.wikipedia.org/wiki/Pentomino#Constructing_rectangular_dimensions
"""

from exact_cover_solver.services.solver import Solver
import time


def generate_pentomino_board_solutions(
    board_height: int, board_width: int, correct_amount: int
) -> None:
    """Test correct amount of solutions is created with given board."""
    for algo in ["DLX", "DictX"]:
        solver = Solver()
        solver.algorithm = algo

        start_time = time.time()
        browser = solver.solve_pentomino_problem(board_height, board_width)

        time_solving = time.time() - start_time
        solutions_amount = len(browser.all_solutions)
        rounded_time = round(time_solving, 2)

        assert solutions_amount == correct_amount
        print(
            f"Algorithm {algo} correctly found {solutions_amount} solutions for "
            f"{board_height}x{board_width} board in {rounded_time} seconds."
        )


def main():
    """Run different type of big input performance tests against algorithms."""
    pentomino_option_sets = [[3, 20, 2], [4, 15, 368], [5, 12, 1010], [6, 10, 2339]]
    print("\n=== Running tests for pentomino boards===")
    for option_set in pentomino_option_sets:
        generate_pentomino_board_solutions(*option_set)


if __name__ == "__main__":
    main()
