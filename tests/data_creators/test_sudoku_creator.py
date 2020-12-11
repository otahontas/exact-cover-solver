import pytest

from exact_cover_solver.data_creators.sudoku_creator import SudokuCreator


@pytest.fixture
def creator():
    return SudokuCreator()


@pytest.fixture
def empty_sudoku():
    return [[0] * 9 for _ in range(9)]


@pytest.fixture
def almost_ready_sudoku():
    return [
        [0, 2, 3, 4, 5, 6, 7, 8, 9],
        [4, 0, 6, 7, 8, 9, 1, 2, 3],
        [7, 8, 9, 1, 2, 3, 4, 5, 6],
        [2, 3, 4, 5, 6, 7, 8, 9, 1],
        [5, 6, 7, 8, 9, 1, 2, 3, 4],
        [8, 9, 1, 2, 3, 4, 5, 6, 7],
        [3, 4, 5, 6, 7, 8, 9, 1, 2],
        [6, 7, 8, 9, 1, 2, 3, 4, 5],
        [9, 1, 2, 3, 4, 5, 6, 7, 8],
    ]


def test_correct_amount_of_data_is_created_for_empty_sudoku(creator, empty_sudoku):
    """Check that correct constrains and candidate possibilities are created.

    There should be 9 * 9 * 4 = 324 constrains (81 nums, constrains for cell, row,
    column and block) and 9 * 9 * 9 = 729 candidates for cells (81 cells, 9 possible
    nums for each cell.
    """
    universe, subset_collection = creator.create_problem_data(empty_sudoku)
    assert len(universe) == 324
    assert len(subset_collection) == 729


def test_correct_amount_of_data_is_created_for_almost_ready_sudoku(
    creator, almost_ready_sudoku
):
    """Check that correct constrains and candidate possibilities are created.

    There is only two numbers missing so possibilities should have row for
    the pre-chosen values 79 times and 18 possible nums for two placements.
    """
    creator = SudokuCreator()
    universe, subset_collection = creator.create_problem_data(almost_ready_sudoku)
    assert len(universe) == 324
    assert len(subset_collection) == 79 + 18


@pytest.mark.parametrize(
    "sudoku, message",
    [
        ([[1, 2, 3, 4, 5, 6, 7, 8, 9], [1]], "must have same length and height"),
        ([[1, 0, 0, 0, 0, 0, 0, 0, 0] for _ in range(9)], "Column should have unique"),
        ([[1, 1, 0, 0, 0, 0, 0, 0, 0] for _ in range(9)], "Row should have unique"),
        (
            [
                [1, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 1, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0],
            ],
            "Block should have unique",
        ),
    ],
)
def test_non_valid_sudoku_input_does_not_pass_validation(sudoku, message, creator):
    """Test that different invalid sudokus fail validation."""
    with pytest.raises(ValueError) as error:
        creator._validate_sudoku_input(sudoku)
        assert message in str(error.value)


def test_valid_sudoku_inputs_pass_validation(
    empty_sudoku, almost_ready_sudoku, creator
):
    creator._validate_sudoku_input(empty_sudoku)
    creator._validate_sudoku_input(almost_ready_sudoku)
