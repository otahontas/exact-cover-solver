import pytest

from exact_cover_solver.translator import Translator
from exact_cover_solver.data_creators import PentominoCreator


@pytest.fixture
def translator():
    return Translator()


@pytest.mark.parametrize(
    "solutions, board_height, board_width, correct_board",
    (
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
    ),
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
