"""Test finding all solutions for different pentomino boards with dlx.

Correct solution amounts are from wikipedia:
https://en.wikipedia.org/wiki/Pentomino#Constructing_rectangular_dimensions
"""
from typing import List

from exact_cover_solver import Solver
import time


def generate_pentomino_board_solutions(
    board_height: int, board_width: int, correct_amount: int
) -> None:
    """Test correct amount of solutions is created with given board."""
    for algo in ["DLX", "DictX"]:
        solver = Solver()

        start_time = time.time()
        boards = solver.solve_pentomino_problem(algo, board_height, board_width)

        time_solving = time.time() - start_time
        solutions_amount = len(boards)
        rounded_time = round(time_solving, 2)

        assert solutions_amount == correct_amount
        print(
            f"Algorithm {algo} correctly found {solutions_amount} solutions for "
            f"{board_height}x{board_width} board in {rounded_time} seconds."
        )


def generate_sudoku_solutions(sudoku: List[List[int]]) -> None:
    """Test solutions can be created for given sudoku."""
    for algo in ["DLX", "DictX"]:
        solver = Solver()

        start_time = time.time()
        solutions_amount = len(solver.solve_sudoku_problem(algo, sudoku))

        time_solving = time.time() - start_time
        rounded_time = round(time_solving, 2)
        print(
            f"Algorithm {algo} found {solutions_amount} solutions in {rounded_time} "
            "seconds."
        )


def main() -> None:
    """Run different type of big input performance tests against algorithms."""
    pentomino_option_sets = [[3, 20, 2], [4, 15, 368], [5, 12, 1010], [6, 10, 2339]]
    print("\n=== Running tests for pentomino boards===")
    for option_set in pentomino_option_sets:
        generate_pentomino_board_solutions(*option_set)
    print("\n=== Running tests for sudokus===")
    # see https://www.conceptispuzzles.com/index.aspx?uri=info/article/424
    hardest_sudoku_ever = [
        [8, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 3, 6, 0, 0, 0, 0, 0],
        [0, 7, 0, 0, 9, 0, 2, 0, 0],
        [0, 5, 0, 0, 0, 7, 0, 0, 0],
        [0, 0, 0, 0, 4, 5, 7, 0, 0],
        [0, 0, 0, 1, 0, 0, 0, 3, 0],
        [0, 0, 1, 0, 0, 0, 0, 6, 8],
        [0, 0, 8, 5, 0, 0, 0, 1, 0],
        [0, 9, 0, 0, 0, 0, 4, 0, 0],
    ]
    generate_sudoku_solutions(hardest_sudoku_ever)
    almost_empty_sudoku = [
        [1, 0, 0, 0, 0, 0, 0, 0, 2],
        [0, 2, 0, 0, 0, 0, 0, 1, 0],
        [0, 0, 3, 0, 0, 0, 4, 0, 0],
        [0, 0, 0, 4, 8, 3, 0, 0, 0],
        [0, 0, 0, 1, 5, 2, 0, 0, 0],
        [0, 0, 0, 7, 9, 6, 0, 0, 0],
        [0, 0, 6, 0, 0, 0, 7, 0, 0],
        [0, 9, 0, 0, 0, 0, 0, 8, 0],
        [8, 0, 0, 0, 0, 0, 0, 0, 9],
    ]
    generate_sudoku_solutions(almost_empty_sudoku)


if __name__ == "__main__":
    main()
