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
        boards = solver.solve_sudoku_problem(algo, sudoku)
        time_solving = time.time() - start_time

        solutions_amount = len(boards)
        rounded_time = round(time_solving, 2)
        print(
            f"Algorithm {algo} found {solutions_amount} solutions in {rounded_time} "
            "seconds."
        )


def run_pentomino_tests():
    """Test all pentomino boards."""
    pentomino_option_sets = [[3, 20, 2], [4, 15, 368], [5, 12, 1010], [6, 10, 2339]]
    for option_set in pentomino_option_sets:
        generate_pentomino_board_solutions(*option_set)


def run_sudoku_tests():
    """Test all pentomino boards."""
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
    sudoku_with_30_hints = [
        [1, 2, 3, 4, 5, 6, 7, 8, 9],
        [4, 5, 6, 7, 8, 9, 1, 2, 3],
        [7, 8, 9, 1, 2, 3, 4, 5, 6],
        [2, 3, 4, 5, 6, 7, 8, 9, 1],
        [5, 6, 7, 8, 9, 1, 2, 3, 4],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]
    generate_sudoku_solutions(sudoku_with_30_hints)
    sudoku_with_24_hints = [
        [1, 2, 3, 4, 5, 6, 7, 8, 9],
        [4, 5, 6, 7, 8, 9, 1, 2, 3],
        [7, 8, 9, 1, 2, 3, 4, 5, 6],
        [2, 3, 4, 5, 6, 7, 8, 9, 1],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]
    generate_sudoku_solutions(sudoku_with_24_hints)
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


def generate_generic_sample_data(n, m):
    """Generate data for generic tests.

    Creates 10 sample subsets with each having n / 10 unique numbers between 0 - n.
    Each subset is put to collection m times, so there should m ** 10 solutions in the
    end with N = n * m * 10 size input.
    """
    base = 10
    universe = [i for i in range(n)]
    subsets = [[j for j in range(i, i + n // base)] for i in range(0, n, n // base)]
    subset_collection = {}
    subset_index = 0
    for i in range(base * m):
        subset_collection[i] = subsets[subset_index]
        subset_index += 1
        subset_index %= 10
    return universe, subset_collection


def run_one_generic_test(n, m):
    """Run test with given sample size."""
    problem_data = generate_generic_sample_data(n, m)
    for algo in ["DLX", "DictX"]:
        solver = Solver()

        start_time = time.time()
        solutions = solver.solve_generic_problem(algo, problem_data)
        time_solving = time.time() - start_time
        rounded_time = round(time_solving, 2)

        assert len(solutions) == m ** 10
        print(
            f"Algorithm {algo} found {len(solutions)} solutions in {rounded_time} "
            f"seconds for input size {n * m * 10}."
        )


def run_generic_tests():
    """Test with different sized inputs."""
    for m in range(1, 5):
        for n in [100, 1000, 10000]:
            run_one_generic_test(n, m)


def main() -> None:
    """Run different type of big input performance tests against algorithms."""
    run_pentomino_tests()
    run_sudoku_tests()
    run_generic_tests()


if __name__ == "__main__":
    main()
