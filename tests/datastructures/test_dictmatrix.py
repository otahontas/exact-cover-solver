import pytest

from exact_cover_solver.datastructures.dictmatrix import DictMatrix


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
def test_matrix_has_correct_columns(problem_data):
    universe, _ = problem_data
    matrix = DictMatrix(problem_data)
    column_dict, _ = matrix.data
    assert all(element in column_dict for element in universe)


@pytest.mark.parametrize("problem_data", ["numbers", "strings"], indirect=True)
def test_matrix_has_correct_elements_in_columns(problem_data):
    matrix = DictMatrix(problem_data)
    _, subset_collection = problem_data
    column_dict, _ = matrix.data
    for element, subset_ids in column_dict.items():
        for subset_id in subset_ids:
            assert element in subset_collection[subset_id]


@pytest.mark.parametrize("problem_data", ["numbers", "strings"], indirect=True)
def test_correct_data_is_returned_from_data_property(problem_data):
    matrix = DictMatrix(problem_data)
    _, subset_collection = problem_data
    assert matrix.data == (matrix._column_dict, subset_collection)
