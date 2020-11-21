"""Unit tests for pentomino generator."""

import pytest

from exact_cover_solver.services.pentomino_generator import PentominoGenerator


@pytest.fixture
def correct_transposed_pentominoes():
    return [
        [[1, 1, 1], [1, 0, 0], [1, 0, 0]],
        [[1, 1], [0, 1], [1, 1]],
        [[0, 1, 0], [1, 1, 1], [0, 1, 0]],
        [[1, 1, 1], [0, 1, 0], [0, 1, 0]],
        [[1, 0], [1, 1], [1, 0], [1, 0]],
        [[1], [1], [1], [1], [1]],
        [[0, 1, 0], [1, 1, 1], [0, 0, 1]],
        [[1, 1], [1, 1], [1, 0]],
        [[1, 0, 0], [1, 1, 0], [0, 1, 1]],
        [[1, 1, 0], [0, 1, 0], [0, 1, 1]],
        [[1, 0], [1, 1], [0, 1], [0, 1]],
        [[1, 1], [1, 0], [1, 0], [1, 0]],
    ]


@pytest.fixture
def correct_left_right_flipped_pentominoes():
    return [
        [[1, 1, 1], [0, 0, 1], [0, 0, 1]],
        [[1, 0, 1], [1, 1, 1]],
        [[0, 1, 0], [1, 1, 1], [0, 1, 0]],
        [[0, 0, 1], [1, 1, 1], [0, 0, 1]],
        [[1, 1, 1, 1], [0, 0, 1, 0]],
        [[1, 1, 1, 1, 1]],
        [[0, 1, 0], [0, 1, 1], [1, 1, 0]],
        [[1, 1, 1], [0, 1, 1]],
        [[0, 1, 1], [1, 1, 0], [1, 0, 0]],
        [[0, 0, 1], [1, 1, 1], [1, 0, 0]],
        [[0, 0, 1, 1], [1, 1, 1, 0]],
        [[1, 1, 1, 1], [0, 0, 0, 1]],
    ]


@pytest.fixture
def correct_up_down_flipped_pentominoes():
    return [
        [[1, 0, 0], [1, 0, 0], [1, 1, 1]],
        [[1, 1, 1], [1, 0, 1]],
        [[0, 1, 0], [1, 1, 1], [0, 1, 0]],
        [[1, 0, 0], [1, 1, 1], [1, 0, 0]],
        [[0, 1, 0, 0], [1, 1, 1, 1]],
        [[1, 1, 1, 1, 1]],
        [[0, 1, 1], [1, 1, 0], [0, 1, 0]],
        [[1, 1, 0], [1, 1, 1]],
        [[0, 0, 1], [0, 1, 1], [1, 1, 0]],
        [[0, 0, 1], [1, 1, 1], [1, 0, 0]],
        [[0, 1, 1, 1], [1, 1, 0, 0]],
        [[1, 0, 0, 0], [1, 1, 1, 1]],
    ]


@pytest.fixture
def correct_orientation_amounts():
    return [4, 4, 1, 4, 8, 2, 8, 8, 4, 4, 8, 8]


def test_transpose_works_correctly(correct_transposed_pentominoes):
    pg = PentominoGenerator()
    transposed = [pg._transpose(pentomino) for pentomino in pg.pentominoes]
    assert transposed == correct_transposed_pentominoes


def test_left_right_flip_works_correctly(correct_left_right_flipped_pentominoes):
    pg = PentominoGenerator()
    flipped = [pg._flip_left_right(pentomino) for pentomino in pg.pentominoes]
    assert flipped == correct_left_right_flipped_pentominoes


def test_up_down_flip_works_correctly(correct_up_down_flipped_pentominoes):
    pg = PentominoGenerator()
    flipped = [pg._flip_up_down(pentomino) for pentomino in pg.pentominoes]
    assert flipped == correct_up_down_flipped_pentominoes


def test_correct_amount_of_orientations_is_generated(correct_orientation_amounts):
    pg = PentominoGenerator()
    amounts = [
        len(orientations)
        for orientations in [
            pg._generate_all_orientations(pentomino) for pentomino in pg.pentominoes
        ]
    ]
    assert amounts == correct_orientation_amounts


def test_correct_cells_are_covered():
    pg = PentominoGenerator()
    board_width = 10
    pentomino = [[1, 1, 1], [1, 0, 0], [1, 0, 0]]

    start = (0, 0)
    covered = pg._solve_covered_cells(pentomino, start, board_width)
    assert covered == [0, 1, 2, 10, 20]

    pentomino = [[1, 1, 1, 1], [1, 0, 0, 0]]
    start = (4, 6)
    covered = pg._solve_covered_cells(pentomino, start, board_width)
    assert covered == [46, 47, 48, 49, 56]
#
#
# def test_generator_generates_correct_amount_of_set_collections_for_6_10_board():
#     pg = PentominoGenerator(6, 10)
#     pg.generate()
#
#     assert len(list(filter(lambda x: (0 in x[1]), pg.set_collection))) == 128
#     assert len(pg.set_collection) == 1932
#
