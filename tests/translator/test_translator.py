import pytest

from exact_cover_solver.translator import Translator
from exact_cover_solver.data_creators import PentominoCreator


@pytest.fixture
def translator():
    return Translator()


@pytest.mark.parametrize(
    "solutions, board_height, board_width, correct_board",
    [
        (
            [[17, 872, 232, 833, 211, 129, 109, 357, 675, 1103, 951, 501]],
            3,
            20,
            [
                [
                    "U",
                    "U",
                    "X",
                    "I",
                    "I",
                    "I",
                    "I",
                    "I",
                    "N",
                    "N",
                    "N",
                    "F",
                    "T",
                    "W",
                    "Y",
                    "Y",
                    "Y",
                    "Y",
                    "Z",
                    "V",
                ],
                [
                    "U",
                    "X",
                    "X",
                    "X",
                    "P",
                    "P",
                    "L",
                    "N",
                    "N",
                    "F",
                    "F",
                    "F",
                    "T",
                    "W",
                    "W",
                    "Y",
                    "Z",
                    "Z",
                    "Z",
                    "V",
                ],
                [
                    "U",
                    "U",
                    "X",
                    "P",
                    "P",
                    "P",
                    "L",
                    "L",
                    "L",
                    "L",
                    "F",
                    "T",
                    "T",
                    "T",
                    "W",
                    "W",
                    "Z",
                    "V",
                    "V",
                    "V",
                ],
            ],
        ),
        (
            [[25, 1265, 1164, 1071, 1557, 749, 205, 365, 523, 654, 161, 132]],
            4,
            15,
            [
                [
                    "U",
                    "U",
                    "X",
                    "Y",
                    "Y",
                    "Y",
                    "Y",
                    "P",
                    "P",
                    "P",
                    "W",
                    "W",
                    "N",
                    "N",
                    "N",
                ],
                [
                    "U",
                    "X",
                    "X",
                    "X",
                    "F",
                    "Y",
                    "T",
                    "P",
                    "P",
                    "W",
                    "W",
                    "N",
                    "N",
                    "Z",
                    "V",
                ],
                [
                    "U",
                    "U",
                    "X",
                    "F",
                    "F",
                    "F",
                    "T",
                    "T",
                    "T",
                    "W",
                    "L",
                    "Z",
                    "Z",
                    "Z",
                    "V",
                ],
                [
                    "I",
                    "I",
                    "I",
                    "I",
                    "I",
                    "F",
                    "T",
                    "L",
                    "L",
                    "L",
                    "L",
                    "Z",
                    "V",
                    "V",
                    "V",
                ],
            ],
        ),
    ],
)
def test_pentomino_solution_is_converted_to_board(
    solutions, board_height, board_width, correct_board, translator
):
    _, subset_collection = PentominoCreator().create_problem_data(
        board_height, board_width
    )
    board = translator.to_pentomino_boards(
        solutions, board_height, board_width, subset_collection
    )[0]
    assert board == correct_board


@pytest.mark.parametrize(
    "solutions, correct_sudoku",
    [
        (
            [
                [
                    (0, 0, 8),
                    (2, 1, 7),
                    (3, 1, 5),
                    (8, 1, 9),
                    (1, 2, 3),
                    (6, 2, 1),
                    (7, 2, 8),
                    (1, 3, 6),
                    (5, 3, 1),
                    (7, 3, 5),
                    (2, 4, 9),
                    (4, 4, 4),
                    (3, 5, 7),
                    (4, 5, 5),
                    (2, 6, 2),
                    (4, 6, 7),
                    (8, 6, 4),
                    (5, 7, 3),
                    (6, 7, 6),
                    (7, 7, 1),
                    (6, 8, 8),
                    (1, 0, 9),
                    (0, 4, 5),
                    (2, 2, 5),
                    (6, 0, 5),
                    (0, 3, 7),
                    (6, 4, 7),
                    (1, 7, 7),
                    (8, 7, 5),
                    (1, 8, 5),
                    (5, 6, 5),
                    (1, 1, 4),
                    (7, 0, 4),
                    (7, 8, 7),
                    (8, 8, 2),
                    (0, 1, 1),
                    (0, 2, 2),
                    (2, 0, 6),
                    (3, 0, 1),
                    (4, 8, 1),
                    (2, 5, 1),
                    (1, 6, 1),
                    (2, 7, 8),
                    (8, 4, 1),
                    (3, 6, 8),
                    (0, 6, 6),
                    (5, 0, 2),
                    (4, 0, 3),
                    (8, 0, 7),
                    (5, 2, 7),
                    (3, 2, 4),
                    (8, 2, 6),
                    (4, 2, 9),
                    (4, 1, 6),
                    (5, 1, 8),
                    (5, 4, 6),
                    (3, 8, 6),
                    (4, 3, 8),
                    (8, 3, 3),
                    (0, 5, 3),
                    (2, 3, 4),
                    (2, 8, 3),
                    (3, 4, 3),
                    (4, 7, 2),
                    (3, 3, 2),
                    (6, 3, 9),
                    (3, 7, 9),
                    (0, 8, 9),
                    (0, 7, 4),
                    (7, 4, 2),
                    (1, 5, 2),
                    (6, 1, 2),
                    (7, 1, 3),
                    (1, 4, 8),
                    (5, 5, 9),
                    (5, 8, 4),
                    (6, 5, 4),
                    (7, 5, 6),
                    (8, 5, 8),
                    (6, 6, 3),
                    (7, 6, 9),
                ]
            ],
            [
                [8, 1, 2, 7, 5, 3, 6, 4, 9],
                [9, 4, 3, 6, 8, 2, 1, 7, 5],
                [6, 7, 5, 4, 9, 1, 2, 8, 3],
                [1, 5, 4, 2, 3, 7, 8, 9, 6],
                [3, 6, 9, 8, 4, 5, 7, 2, 1],
                [2, 8, 7, 1, 6, 9, 5, 3, 4],
                [5, 2, 1, 9, 7, 4, 3, 6, 8],
                [4, 3, 8, 5, 2, 6, 9, 1, 7],
                [7, 9, 6, 3, 1, 8, 4, 5, 2],
            ],
        )
    ],
)
def test_sudoku_solution_is_converted_to_board(solutions, correct_sudoku, translator):
    board = translator.to_sudoku_boards(solutions)[0]
    assert board == correct_sudoku


@pytest.mark.parametrize(
    "solutions, subset_collection, correct_subsets",
    [
        ([[1]], {1: [1, 2]}, [[[1, 2]]]),
        (
            [["H", (1, 2), (3, 2)], ["G", (0, 0), (0, 1)]],
            {
                "H": [1, 2],
                (1, 2): [3, 4],
                (3, 2): [5, 6],
                "G": [7, 8],
                (0, 0): [9, 10],
                (0, 1): [11, 12],
            },
            [[[1, 2], [3, 4], [5, 6]], [[7, 8], [9, 10], [11, 12]]],
        ),
    ],
)
def test_correct_subsets_are_picked_to_solution(
    solutions, subset_collection, correct_subsets, translator
):
    solutions_with_subset = translator.to_generic_solutions(
        solutions, subset_collection
    )
    assert solutions_with_subset == correct_subsets
