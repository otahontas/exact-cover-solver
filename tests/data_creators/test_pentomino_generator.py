"""Unit tests for pentomino generator."""

import pytest

from exact_cover_solver.data_creators.pentomino_creator import PentominoCreator


@pytest.fixture
def correct_transposed_pentominoes():
    return {
        "V": [[1, 1, 1], [1, 0, 0], [1, 0, 0]],
        "U": [[1, 1], [0, 1], [1, 1]],
        "X": [[0, 1, 0], [1, 1, 1], [0, 1, 0]],
        "T": [[1, 1, 1], [0, 1, 0], [0, 1, 0]],
        "Y": [[1, 0], [1, 1], [1, 0], [1, 0]],
        "I": [[1], [1], [1], [1], [1]],
        "F": [[0, 1, 0], [1, 1, 1], [0, 0, 1]],
        "P": [[1, 1], [1, 1], [1, 0]],
        "W": [[1, 0, 0], [1, 1, 0], [0, 1, 1]],
        "Z": [[1, 1, 0], [0, 1, 0], [0, 1, 1]],
        "N": [[1, 0], [1, 1], [0, 1], [0, 1]],
        "L": [[1, 1], [1, 0], [1, 0], [1, 0]],
    }


@pytest.fixture
def correct_left_right_flipped_pentominoes():
    return {
        "V": [[1, 1, 1], [0, 0, 1], [0, 0, 1]],
        "U": [[1, 0, 1], [1, 1, 1]],
        "X": [[0, 1, 0], [1, 1, 1], [0, 1, 0]],
        "T": [[0, 0, 1], [1, 1, 1], [0, 0, 1]],
        "Y": [[1, 1, 1, 1], [0, 0, 1, 0]],
        "I": [[1, 1, 1, 1, 1]],
        "F": [[0, 1, 0], [0, 1, 1], [1, 1, 0]],
        "P": [[1, 1, 1], [0, 1, 1]],
        "W": [[0, 1, 1], [1, 1, 0], [1, 0, 0]],
        "Z": [[0, 0, 1], [1, 1, 1], [1, 0, 0]],
        "N": [[0, 0, 1, 1], [1, 1, 1, 0]],
        "L": [[1, 1, 1, 1], [0, 0, 0, 1]],
    }


@pytest.fixture
def correct_up_down_flipped_pentominoes():
    return {
        "V": [[1, 0, 0], [1, 0, 0], [1, 1, 1]],
        "U": [[1, 1, 1], [1, 0, 1]],
        "X": [[0, 1, 0], [1, 1, 1], [0, 1, 0]],
        "T": [[1, 0, 0], [1, 1, 1], [1, 0, 0]],
        "Y": [[0, 1, 0, 0], [1, 1, 1, 1]],
        "I": [[1, 1, 1, 1, 1]],
        "F": [[0, 1, 1], [1, 1, 0], [0, 1, 0]],
        "P": [[1, 1, 0], [1, 1, 1]],
        "W": [[0, 0, 1], [0, 1, 1], [1, 1, 0]],
        "Z": [[0, 0, 1], [1, 1, 1], [1, 0, 0]],
        "N": [[0, 1, 1, 1], [1, 1, 0, 0]],
        "L": [[1, 0, 0, 0], [1, 1, 1, 1]],
    }


@pytest.fixture
def correct_orientation_amounts():
    """For more details, see https://en.wikipedia.org/wiki/Pentomino#Symmetry."""
    return {
        "V": 4,
        "U": 4,
        "X": 1,
        "T": 4,
        "Y": 8,
        "I": 2,
        "F": 8,
        "P": 8,
        "W": 4,
        "Z": 4,
        "N": 4,
        "L": 8,
    }


def test_transpose_works_correctly(correct_transposed_pentominoes):
    pg = PentominoCreator()
    transposed = {
        label: pg._transpose(pentomino)
        for (label, pentomino) in pg._pentominoes.items()
    }
    assert transposed == correct_transposed_pentominoes


def test_left_right_flip_works_correctly(correct_left_right_flipped_pentominoes):
    pg = PentominoCreator()
    flipped = {
        label: pg._flip_left_right(pentomino)
        for (label, pentomino) in pg._pentominoes.items()
    }
    assert flipped == correct_left_right_flipped_pentominoes


def test_up_down_flip_works_correctly(correct_up_down_flipped_pentominoes):
    pg = PentominoCreator()
    flipped = {
        label: pg._flip_up_down(pentomino)
        for (label, pentomino) in pg._pentominoes.items()
    }
    assert flipped == correct_up_down_flipped_pentominoes


def test_correct_amount_of_orientations_is_generated(correct_orientation_amounts):
    pg = PentominoCreator()
    amounts = {
        label: len(pg._generate_all_orientations(pentomino))
        for (label, pentomino) in pg._pentominoes.items()
    }
    assert amounts == correct_orientation_amounts


def test_correct_cells_are_covered():
    pg = PentominoCreator()
    pg._width = 10
    pentomino = [[1, 1, 1], [1, 0, 0], [1, 0, 0]]

    start = (0, 0)
    covered = pg._solve_covered_cells(pentomino, start)
    assert covered == [0, 1, 2, 10, 20]

    pentomino = [[1, 1, 1, 1], [1, 0, 0, 0]]
    start = (4, 6)
    covered = pg._solve_covered_cells(pentomino, start)
    assert covered == [46, 47, 48, 49, 56]


def test_generator_generates_correct_amount_of_set_collections_for_3_20_board():
    """Generate 3x20 board collections.

    For info about correct amounts, see following link:
    https://boyetblog.s3.amazonaws.com/PCPlus/294.pentominoes.pdf.
    """
    correct_amounts = {
        "V": 72,
        "U": 110,
        "X": 18,
        "T": 72,
        "Y": 136,
        "I": 48,
        "F": 144,
        "P": 220,
        "W": 72,
        "Z": 72,
        "N": 68,
        "L": 136,
    }
    correct_total_amount = 1168
    correct_universe_size = 72

    pg = PentominoCreator()
    pg._height = 3
    pg._width = 20
    pg._generate_set_collection()

    assert len(pg._universe) == correct_universe_size
    indexes = pg._pentomino_indexes
    for pentomino in correct_amounts:
        assert (
            len([row for row in pg._set_collection if row[0] == indexes[pentomino]])
            == correct_amounts[pentomino]
        )
    assert len(pg._set_collection) == correct_total_amount
