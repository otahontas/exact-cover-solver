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
    return [4, 4, 1, 4, 8, 2, 8, 8, 4, 4, 4, 8]


def test_transpose_works_correctly(correct_transposed_pentominoes):
    pg = PentominoGenerator(6, 10)
    transposed = list(map(pg.transpose, pg.pentominoes))
    assert transposed == correct_transposed_pentominoes


def test_left_right_flip_works_correctly(correct_left_right_flipped_pentominoes):
    pg = PentominoGenerator(6, 10)
    transposed = list(map(pg.flip_left_right, pg.pentominoes))
    assert transposed == correct_left_right_flipped_pentominoes


def test_up_down_flip_works_correctly(correct_up_down_flipped_pentominoes):
    pg = PentominoGenerator(6, 10)
    transposed = list(map(pg.flip_up_down, pg.pentominoes))
    assert transposed == correct_up_down_flipped_pentominoes


def test_correct_amount_of_orientations_is_generated(correct_orientation_amounts):
    pg = PentominoGenerator(6, 10)
    amounts = [len(x) for x in list(map(pg.generate_all_orientations, pg.pentominoes))]
    assert amounts == correct_orientation_amounts