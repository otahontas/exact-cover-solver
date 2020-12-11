import pytest
from unittest.mock import Mock
from exact_cover_solver.datastructures.matrix_base import Matrix


class FakeMatrixWithCreate(Matrix):
    @staticmethod
    def _validate_problem_data(problem_data):
        """Fake validating and just return passed data."""
        return problem_data

    def _create(self):
        """Call not implemented abstract method."""
        super(FakeMatrixWithCreate, self)._create()


class FakeMatrixWithoutCreate(Matrix):
    def _create(self):
        """Don't do nyt anything when trying to create matrix contents."""
        pass


def test_not_possible_to_call_create_without_real_implementation():
    mocked_universe = Mock()
    mocked_subset_collection = Mock()
    mocked_problem_data = (mocked_universe, mocked_subset_collection)
    with pytest.raises(NotImplementedError):
        FakeMatrixWithCreate(mocked_problem_data)


@pytest.mark.parametrize(
    "problem_data",
    [
        (([1, 2, 3, 4, 5], {1: [1, 2], 2: [3, 4], 3: [5, 1], 4: [2, 3], 5: [4, 5]})),
        (
            (
                ["Make", "Pera", "Mä"],
                {"1st": ["Make", "Pera"], "2nd": ["Pera", "Mä"], "3rd": ["Mä", "Make"]},
            )
        ),
    ],
)
def test_validation_passes_with_valid_data(problem_data):
    FakeMatrixWithoutCreate(problem_data)


@pytest.mark.parametrize(
    "problem_data, message",
    [
        (([], {}), "empty universe"),
        (([1, 2], {}), "empty subset collection"),
        (([1, 1, 2], {}), "Universe should only have unique elements"),
        (([1, 2], {1: []}), "Empty subsets are not allowed."),
        (([1, 2], {1: [1, 1]}), "Subset should only have unique elements"),
        (([1, 2], {1: [1, 2], 2: [3]}), "are not elements of the universe"),
    ],
)
def test_validation_fails_with_invalid_data(problem_data, message):
    with pytest.raises(ValueError) as error:
        FakeMatrixWithoutCreate(problem_data)
        assert message in str(error.value)
