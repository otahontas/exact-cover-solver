import pytest
from unittest.mock import patch

from exact_cover_solver.data_creators.pentomino_creator import (
    PentominoCreator,
    BoardSizeNotInitializedError,
)


@pytest.fixture
def generator():
    return PentominoCreator()


@pytest.fixture
def generator_method_and_params(request):
    method_name, params = request.param
    method = getattr(PentominoCreator(), method_name)
    return method, params


@pytest.mark.parametrize("height, width", [(6, 10), (5, 12), (4, 15), (3, 20)])
def test_correct_board_size_can_be_set(height, width, generator):
    with patch.object(generator, "_generate_set_collection") as mocked_generate:
        generator.change_board_size(height, width)
        assert generator.board_size == (height, width)
        assert mocked_generate.call_count == 1


@pytest.mark.parametrize("height, width", [(2, 20), (3, 19), (4, 20)])
def test_not_correct_size_can_not_be_set(height, width, generator):
    with patch.object(generator, "_generate_set_collection") as mocked_generate:
        with pytest.raises(ValueError):
            generator.change_board_size(height, width)
        assert not mocked_generate.called


@pytest.mark.parametrize(
    "generator_method_and_params",
    [
        ("create_problem_data", None),
        ("_generate_set_collection", None),
        ("_point_to_cell_num", (0, 0)),
        ("cell_num_to_point", 0),
    ],
    indirect=True,
)
def test_certain_methods_fail_if_board_size_not_set(generator_method_and_params):
    """Test error is raised when calling different methods too early."""
    method, params = generator_method_and_params
    with pytest.raises(BoardSizeNotInitializedError):
        if params is not None:
            method(params)
        else:
            method()


def test_board_size_property_fails_if_board_size_not_set(generator):
    with pytest.raises(BoardSizeNotInitializedError):
        assert not generator.board_size


@pytest.mark.parametrize(
    "point, width, correct_cell",
    [((0, 1), 20, 13), ((1, 2), 15, 29), ((3, 4), 12, 52), ((4, 5), 10, 57)],
)
def test_point_is_converted_to_cell_num(point, width, correct_cell, generator):
    """Test point to cell conversion with different points and board widths."""
    generator._width = width
    assert generator._point_to_cell_num(point) == correct_cell


@pytest.mark.parametrize(
    "correct_point, width, cell",
    [((0, 1), 20, 13), ((1, 2), 15, 29), ((3, 4), 12, 52), ((4, 5), 10, 57)],
)
def test_cell_num_is_converted_to_point(correct_point, width, cell, generator):
    """Test point to cell conversion with different points and board widths."""
    generator._width = width
    assert generator.cell_num_to_point(cell) == correct_point


@pytest.mark.parametrize(
    "point, width, pentomino, correct_covered",
    [
        ((0, 0), 10, [[1, 1, 1], [1, 0, 0], [1, 0, 0]], [12, 13, 14, 22, 32]),
        ((4, 6), 10, [[1, 1, 1, 1], [1, 0, 0, 0]], [58, 59, 60, 61, 68]),
    ],
)
def test_correct_cells_are_covered(point, width, pentomino, correct_covered, generator):
    """Test cell coverage with different pentominoes."""
    generator._width = width
    assert generator._solve_covered_cells(pentomino, point) == correct_covered


@pytest.mark.parametrize("height, width", [(6, 10), (5, 12), (4, 15), (3, 20)])
def test_same_size_universe_is_generated_for_each_board_size(height, width, generator):
    correct_universe_size = 72
    generator.change_board_size(height, width)
    universe, _ = generator.create_problem_data()
    assert len(universe) == correct_universe_size


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
    pentomino_name, correct_amount, generator
):
    """Test that each pentomino generates correct amount of sets in 3x20 board.

    Test patches the whole pentomino list with single pentomino for each test.

    For info about correct amounts, see following link:
    https://boyetblog.s3.amazonaws.com/PCPlus/294.pentominoes.pdf.
    """
    pentomino = generator._pentominoes.get_pentomino_by_name(pentomino_name)
    with patch.object(generator, "_pentominoes") as mocked_pentominoes:
        mocked_pentominoes.as_list.return_value = [pentomino]
        generator.change_board_size(3, 20)
        _, set_collection = generator.create_problem_data()
        assert len(set_collection) == correct_amount


def test_set_collection_does_not_have_previous_set_collection(generator):
    generator.change_board_size(3, 20)
    _, set_collection = generator.create_problem_data()
    first_run_size = len(set_collection)

    generator.change_board_size(3, 20)
    _, set_collection = generator.create_problem_data()
    second_run_size = len(set_collection)

    assert first_run_size == second_run_size
