import pytest

from exact_cover_solver.data_creators.generic_creator import (
    GenericCreator,
    ParsingError,
)


@pytest.fixture()
def instance_without_init():
    return object.__new__(GenericCreator)


def test_correct_universe_and_set_collection_are_both_parsed():
    universe_input = "1,2,3,4"
    set_collection_input = "1,3;2,4;2,3;1,4"
    gc = GenericCreator(universe_input, set_collection_input)
    universe, set_collection = gc.create_problem_data()
    assert universe == [1, 2, 3, 4]
    assert set_collection == [[1, 3], [2, 4], [2, 3], [1, 4]]


def test_parsing_fails_with_badly_written_universe_input(instance_without_init):
    with pytest.raises(ParsingError):
        universe_input = "1a2,3,4"
        instance_without_init._parse_universe(universe_input)


def test_parsing_fails_with_badly_written_set_collection_input(instance_without_init):
    with pytest.raises(ParsingError):
        set_collection_input = "1a;j;4;1,4"
        instance_without_init._universe = set()
        instance_without_init._parse_set_collection(set_collection_input)


def test_parsing_fails_with_non_compatible_universe_and_set_collection():
    universe_input = "1,2"
    set_collection_input = "1,3;2,4"
    with pytest.raises(ParsingError):
        GenericCreator(universe_input, set_collection_input)


def test_parsing_fails_with_non_valid_universe(instance_without_init):
    with pytest.raises(ParsingError):
        universe_input = "1,2,2"
        instance_without_init._parse_universe(universe_input)
