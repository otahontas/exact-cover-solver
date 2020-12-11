from unittest.mock import MagicMock

import pytest

from exact_cover_solver.data_creators.sudoku_creator import SudokuCreator


@pytest.fixture
def creator():
    return SudokuCreator()


@pytest.fixture
def sudoku(request):
    if request.param == "empty_9x9":
        return [[0] * 9 for _ in range(9)]
    elif request.param == "almost_ready_9x9":
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
    elif request.param == "empty_16x16":
        return [[0] * 16 for _ in range(16)]


@pytest.mark.parametrize("sudoku", ["empty_9x9"], indirect=["sudoku"])
def test_problem_data_returns_correct_values(sudoku, creator):
    fake_universe = [1, 2]
    fake_subset_collection = {1: [1], 2: [2]}
    mocked_create_universe = MagicMock(return_value=fake_universe)
    mocked_create_subset_collection = MagicMock(return_value=fake_subset_collection)
    mocked_validate_sudoku_input = MagicMock()
    creator._create_universe = mocked_create_universe
    creator._create_subset_collection = mocked_create_subset_collection
    creator._validate_sudoku_input = mocked_validate_sudoku_input

    universe, subset_collection = creator.create_problem_data(sudoku)
    assert universe == fake_universe
    assert subset_collection == fake_subset_collection
    assert mocked_create_universe.call_count == 1
    assert mocked_create_subset_collection.call_count == 1
    assert mocked_validate_sudoku_input.call_count == 1


@pytest.mark.parametrize("sudoku", ["empty_9x9"], indirect=["sudoku"])
def test_problem_data_fails_if_validation_fails(creator, sudoku):
    mocked_validate_sudoku_input = MagicMock(side_effect=ValueError)
    creator._validate_sudoku_input = mocked_validate_sudoku_input
    with pytest.raises(ValueError):
        creator.create_problem_data(sudoku)


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
    """Test that different invalid sudoku's fail validation."""
    with pytest.raises(ValueError) as error:
        creator._validate_sudoku_input(sudoku)
        assert message in str(error.value)


@pytest.mark.parametrize(
    "sudoku", ["empty_9x9", "empty_16x16", "almost_ready_9x9"], indirect=["sudoku"]
)
def test_valid_sudoku_inputs_pass_validation(sudoku, creator):
    creator._validate_sudoku_input(sudoku)


@pytest.mark.parametrize(
    "sudoku, correct_amount",
    [("empty_9x9", 324), ("almost_ready_9x9", 324), ("empty_16x16", 1024)],
    indirect=["sudoku"],
)
def test_correct_universe_is_created_for_different_sudokus(
    sudoku, correct_amount, creator
):
    """Check that correct constrains are created.

    There should be 9 * 9 * 4 = 324 constrains (81 nums, constrains for cell, row,
    column and block) for 9x9 sudoku, and 16 * 16 * 4 = 1024 constrains for 16x16
    sudoku etc.
    """
    universe = creator._create_universe(sudoku)
    print(len(universe))
    assert len(universe) == correct_amount


@pytest.mark.parametrize(
    "sudoku, correct_amount",
    [("empty_9x9", 729), ("almost_ready_9x9", 79 + 18), ("empty_16x16", 4096)],
    indirect=["sudoku"],
)
def test_correct_length_subset_collection_is_created_for_different_sudokus(
    sudoku, correct_amount, creator
):
    """Check correct amount of candidate possibilities are created."""
    creator = SudokuCreator()
    subset_collection = creator._create_subset_collection(sudoku)
    assert len(subset_collection) == correct_amount
