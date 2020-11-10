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
