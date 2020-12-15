from unittest.mock import Mock

import pytest
from exact_cover_solver.datastructures.dlxmatrix import DLXMatrix


@pytest.fixture
def problem_data(request):
    if request.param == "numbers":
        return (
            [1, 2, 3, 4, 5],
            {1: [1, 2], 2: [3, 4], 3: [5, 1], 4: [2, 3], 5: [4, 5]},
        )
    elif request.param == "strings":
        return (
            ["Make", "Pera", "Mä"],
            {"1st": ["Make", "Pera"], "2nd": ["Pera", "Mä"], "3rd": ["Mä", "Make"]},
        )


@pytest.mark.parametrize("problem_data", ["numbers", "strings"], indirect=True)
def test_first_and_last_columns_are_linked_to_root(problem_data):
    matrix = DLXMatrix(problem_data)
    universe, _ = problem_data
    assert matrix.root.right.id == universe[0]
    assert matrix.root.left.id == universe[-1]


@pytest.mark.parametrize("problem_data", ["numbers", "strings"], indirect=True)
def test_each_column_has_correct_size(problem_data):
    matrix = DLXMatrix(problem_data)
    _, subset_collection = problem_data
    column = matrix.root.right
    for subset in subset_collection.values():
        assert column.size == len(subset)
        column = column.right


@pytest.mark.parametrize("problem_data", ["numbers", "strings"], indirect=True)
def test_data_objects_are_circularly_linked_together(problem_data):
    matrix = DLXMatrix(problem_data)
    _, subset_collection = problem_data

    def find_correct_data_object(element, subset_id):
        column = matrix._find_column(element)
        data_object = column.down
        while data_object.id != subset_id:
            data_object = data_object.down
        return data_object

    for subset_id, subset_elements in subset_collection.items():
        rightmost_data_object = find_correct_data_object(subset_elements[-1], subset_id)
        leftmost_data_object = find_correct_data_object(subset_elements[0], subset_id)

        assert leftmost_data_object.left == rightmost_data_object
        assert rightmost_data_object.right == leftmost_data_object


def test_data_object_creation_fails_with_empty_subset():
    mocked_matrix = Mock(DLXMatrix)
    mocked_matrix._subset_collection = {1: []}
    with pytest.raises(ValueError):
        DLXMatrix._create_data_objects(mocked_matrix)


@pytest.mark.parametrize("problem_data", ["numbers", "strings"], indirect=True)
def test_column_search_fails_with_wrong_element(problem_data):
    matrix = DLXMatrix(problem_data)
    universe, _ = problem_data
    element = universe[0] * 1337
    with pytest.raises(ValueError):
        matrix._find_column(element)
