import pytest
from unittest.mock import Mock
from exact_cover_solver.datastructures.matrix_base import Matrix


def test_not_possible_to_call_create_without_real_implementation():
    class FakeMatrix(Matrix):
        def _create(self):
            super(FakeMatrix, self)._create()

    with pytest.raises(NotImplementedError):
        mocked_tuple = (Mock(), Mock())
        matrix = FakeMatrix(mocked_tuple)
        matrix._create()
