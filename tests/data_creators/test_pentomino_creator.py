import pytest
from unittest.mock import MagicMock

from exact_cover_solver.data_creators.pentomino_creator import PentominoCreator
from exact_cover_solver.datastructures import Pentominoes


@pytest.fixture
def creator():
    return PentominoCreator()


def test_generator_is_initialized_with_correct_attributes(creator):
    assert isinstance(creator._PENTOMINOES, Pentominoes)
    assert creator._CELLS_AMOUNT == 60


@pytest.mark.parametrize("height, width", [(6, 10), (5, 12), (4, 15), (3, 20)])
def test_problem_data_returns_correct_values_with_correct_sizes(height, width, creator):
    fake_universe = [1, 2]
    fake_subset_collection = {1: [1], 2: [2]}
    mocked_create_universe = MagicMock(return_value=fake_universe)
    mocked_create_subset_collection = MagicMock(return_value=fake_subset_collection)
    creator._create_universe = mocked_create_universe
    creator._create_subset_collection = mocked_create_subset_collection

    universe, subset_collection = creator.create_problem_data(height, width)
    assert universe == fake_universe
    assert subset_collection == fake_subset_collection
    assert mocked_create_universe.call_count == 1
    assert mocked_create_subset_collection.call_count == 1


@pytest.mark.parametrize("height, width", [(2, 20), (3, 19), (4, 20)])
def test_error_is_raised_when_invalid_size_is_given(height, width, creator):
    mocked_create_universe = MagicMock()
    mocked_create_subset_collection = MagicMock()
    creator._create_universe = mocked_create_universe
    creator._create_subset_collection = mocked_create_subset_collection
    with pytest.raises(ValueError):
        creator.create_problem_data(height, width)
        assert not mocked_create_universe.called
        assert not mocked_create_subset_collection.called


@pytest.mark.parametrize("height, width", [(6, 10), (5, 12), (4, 15), (3, 20)])
def test_same_size_universe_is_generated_for_each_board_size(height, width, creator):
    correct_universe_size = 72
    universe = creator._create_universe(height, width)
    assert len(universe) == correct_universe_size


@pytest.mark.parametrize(
    "height, width, points",
    [
        (6, 10, [(0, 0), (0, 5), (9, 0), (9, 5)]),
        (5, 12, [(0, 0), (0, 4), (11, 0), (11, 4)]),
        (4, 15, [(0, 0), (0, 3), (14, 0), (14, 3)]),
        (3, 20, [(0, 0), (0, 2), (19, 0), (19, 2)]),
    ],
)
def test_universe_has_corner_points_for_each_board_size(height, width, points, creator):
    universe = creator._create_universe(height, width)
    assert all(point in universe for point in points)


@pytest.mark.parametrize(
    "pentomino_name, correct_amount",
    [
        ("V", 18),
        ("U", 110),
        ("X", 18),
        ("T", 72),
        ("Y", 136),
        ("I", 48),
        ("F", 144),
        ("P", 220),
        ("W", 72),
        ("Z", 72),
        ("N", 136),
        ("L", 136),
    ],
)
def test_correct_amounts_of_sets_is_generated_for_3_20_board(
    pentomino_name, correct_amount, creator
):
    """Test that each pentomino generates correct amount of sets in 3x20 board.

    Test patches the whole pentomino list with single pentomino for each test.

    For info about correct amounts, see following link:
    https://boyetblog.s3.amazonaws.com/PCPlus/294.pentominoes.pdf. It's otherwise
    the same, but in this program V pentominoes are used only ones, hence 4x smaller
    amount .
    """
    pentomino = Pentominoes().get_pentomino_by_name(pentomino_name)
    creator._PENTOMINOES.as_list = MagicMock(return_value=[pentomino])
    subset_collection = creator._create_subset_collection(3, 20)
    assert len(subset_collection) == correct_amount


@pytest.mark.parametrize(
    "start, pentomino_grid, correct_covered",
    [
        (
            (0, 0),
            [[0, 0, 1], [0, 0, 1], [1, 1, 1]],
            [(2, 0), (2, 1), (0, 2), (1, 2), (2, 2)],
        ),
        (
            (6, 4),
            [[1, 1, 1, 1], [1, 0, 0, 0]],
            [(6, 4), (7, 4), (8, 4), (9, 4), (6, 5)],
        ),
    ],
)
def test_correct_cells_are_covered(start, pentomino_grid, correct_covered, creator):
    """Test cell coverage with different pentominoes from different starting points."""
    covered = creator._solve_covered_points(pentomino_grid, start)
    assert covered == correct_covered
