import pytest
from exact_cover_solver.datastructures import Matrix


def test_not_possible_to_call_create_without_real_implementation():
    class FakeMatrix(Matrix):
        def _create(self):
            super(FakeMatrix, self)._create()

    with pytest.raises(NotImplementedError):
        matrix = FakeMatrix(([1], [[1]]))
        matrix._create()


@pytest.mark.parametrize("args", [([]), ([], [[1]]), ([1], [])])
def test_init_fails_with_wrong_arguments(args):
    class FakeMatrix(Matrix):
        def __init__(self, constrains):
            super(FakeMatrix, self).__init__(constrains)

        def _create(self):
            pass

    with pytest.raises(ValueError):
        FakeMatrix(args)
