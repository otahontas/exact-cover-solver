from exact_cover_solver.data_creators.sudoku_creator import SudokuCreator


def test_correct_amount_of_data_is_created_for_empty_sudoku():
    """Check that correct constrains and candidate possibilities are created.

    There should be 9 * 9 * 4 = 324 constrains (81 nums, constrains for cell, row,
    column and block) and 9 * 9 * 9 = 729 candidates for cells (81 cells, 9 possible
    nums for each cell.
    """
    creator = SudokuCreator()
    sudoku = [[0] * 9 for _ in range(9)]
    universe, subset_collection = creator.create_problem_data(sudoku)
    assert len(universe) == 324
    assert len(subset_collection) == 729


def test_correct_amount_of_data_is_created_for_almost_ready_sudoku():
    """Check that correct constrains and candidate possibilities are created.

    There is only two numbers missing so possibilities should have row for
    the pre-chosen values 79 times and 18 possible nums for two placements.
    """
    creator = SudokuCreator()
    sudoku = [
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
    universe, subset_collection = creator.create_problem_data(sudoku)
    assert len(universe) == 324
    assert len(subset_collection) == 79 + 18
