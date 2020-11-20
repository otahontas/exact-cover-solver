"""Unit tests for dlx implementation of algo X."""
from exact_cover_solver.datastructures.dlxmatrix import DLXMatrix
from exact_cover_solver.algos.dlx import DLX


def test_correct_single_solution_is_found():
    universe = [1, 2, 3, 4, 5, 6, 7]
    set_collection = [
        ("A", [1, 4, 7]),
        ("B", [1, 4]),
        ("C", [4, 5, 7]),
        ("D", [3, 5, 6]),
        ("E", [2, 3, 6, 7]),
        ("F", [2, 7]),
    ]
    matrix = DLXMatrix(universe, set_collection)
    dlx = DLX()
    solutions = dlx.solve(matrix)

    assert len(solutions) == 1
    assert "B" and "D" and "F" in solutions[0]
    assert "A" and "C" and "E" not in solutions[0]


def test_no_solution_is_found_with_unsolvable_collection():
    universe = [1, 2, 3, 4, 5, 6, 7]
    set_collection = [
        ("A", [1, 6, 7]),
        ("B", [2, 6, 7]),
        ("C", [3, 6, 7]),
        ("D", [4, 6, 7]),
    ]

    matrix = DLXMatrix(universe, set_collection)
    dlx = DLX()
    solutions = dlx.solve(matrix)

    assert not solutions
