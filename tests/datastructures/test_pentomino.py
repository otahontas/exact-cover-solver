import pytest

from exact_cover_solver.datastructures.pentomino import Pentominoes


@pytest.fixture()
def pentominoes():
    return Pentominoes()


@pytest.mark.parametrize(
    "pentomino_name, correctly_transposed",
    [
        ("U", [[1, 1], [0, 1], [1, 1]]),
        ("X", [[0, 1, 0], [1, 1, 1], [0, 1, 0]]),
        ("T", [[1, 1, 1], [0, 1, 0], [0, 1, 0]]),
        ("Y", [[1, 0], [1, 1], [1, 0], [1, 0]]),
        ("I", [[1], [1], [1], [1], [1]]),
        ("F", [[0, 1, 0], [1, 1, 1], [0, 0, 1]]),
        ("P", [[1, 1], [1, 1], [1, 0]]),
        ("W", [[1, 0, 0], [1, 1, 0], [0, 1, 1]]),
        ("Z", [[1, 1, 0], [0, 1, 0], [0, 1, 1]]),
        ("N", [[1, 0], [1, 1], [0, 1], [0, 1]]),
        ("L", [[1, 1], [1, 0], [1, 0], [1, 0]]),
    ],
)
def test_pentomino_is_correctly_transposed(
    pentomino_name, correctly_transposed, pentominoes
):
    pentomino = pentominoes.get_pentomino_by_name(pentomino_name)
    assert pentomino._transpose(pentomino._shape) == correctly_transposed


@pytest.mark.parametrize(
    "pentomino_name, correctly_lr_flipped",
    [
        ("U", [[1, 0, 1], [1, 1, 1]]),
        ("X", [[0, 1, 0], [1, 1, 1], [0, 1, 0]]),
        ("T", [[0, 0, 1], [1, 1, 1], [0, 0, 1]]),
        ("Y", [[1, 1, 1, 1], [0, 0, 1, 0]]),
        ("I", [[1, 1, 1, 1, 1]]),
        ("F", [[0, 1, 0], [0, 1, 1], [1, 1, 0]]),
        ("P", [[1, 1, 1], [0, 1, 1]]),
        ("W", [[0, 1, 1], [1, 1, 0], [1, 0, 0]]),
        ("Z", [[0, 0, 1], [1, 1, 1], [1, 0, 0]]),
        ("N", [[0, 0, 1, 1], [1, 1, 1, 0]]),
        ("L", [[1, 1, 1, 1], [0, 0, 0, 1]]),
    ],
)
def test_pentomino_is_correctly_lr_flipped(
    pentomino_name, correctly_lr_flipped, pentominoes
):
    pentomino = pentominoes.get_pentomino_by_name(pentomino_name)
    assert pentomino._flip_left_right(pentomino._shape) == correctly_lr_flipped


@pytest.mark.parametrize(
    "pentomino_name, correctly_ud_flipped",
    [
        ("U", [[1, 1, 1], [1, 0, 1]]),
        ("X", [[0, 1, 0], [1, 1, 1], [0, 1, 0]]),
        ("T", [[1, 0, 0], [1, 1, 1], [1, 0, 0]]),
        ("Y", [[0, 1, 0, 0], [1, 1, 1, 1]]),
        ("I", [[1, 1, 1, 1, 1]]),
        ("F", [[0, 1, 1], [1, 1, 0], [0, 1, 0]]),
        ("P", [[1, 1, 0], [1, 1, 1]]),
        ("W", [[0, 0, 1], [0, 1, 1], [1, 1, 0]]),
        ("Z", [[0, 0, 1], [1, 1, 1], [1, 0, 0]]),
        ("N", [[0, 1, 1, 1], [1, 1, 0, 0]]),
        ("L", [[1, 0, 0, 0], [1, 1, 1, 1]]),
    ],
)
def test_pentomino_is_correctly_ud_flipped(
    pentomino_name, correctly_ud_flipped, pentominoes
):
    pentomino = pentominoes.get_pentomino_by_name(pentomino_name)
    assert pentomino._flip_up_down(pentomino._shape) == correctly_ud_flipped


@pytest.mark.parametrize(
    "pentomino_name, correct_amount",
    [
        ("V", 1),
        ("U", 4),
        ("X", 1),
        ("T", 4),
        ("Y", 8),
        ("I", 2),
        ("F", 8),
        ("P", 8),
        ("W", 4),
        ("Z", 4),
        ("N", 8),
        ("L", 8),
    ],
)
def test_correct_amount_of_orientations_is_generated(
    pentomino_name, correct_amount, pentominoes
):
    pentomino = pentominoes.get_pentomino_by_name(pentomino_name)
    assert len(pentomino.generate_all_orientations()) == correct_amount


def test_wrong_pentomino_index_does_not_work(pentominoes):
    amount = pentominoes.amount
    with pytest.raises(ValueError):
        pentominoes.get_name_by_index(amount + 1)


def test_wrong_pentomino_name_does_not_work(pentominoes):
    with pytest.raises(ValueError):
        pentominoes.get_pentomino_by_name("Ö")
