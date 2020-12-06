import pytest
from exact_cover_solver.algos.algox_base import AlgorithmX
from unittest.mock import Mock


def test_not_possible_to_call_solve_without_real_implementation():
    class FakeAlgoX(AlgorithmX):
        def solve(self, matrix):
            super(FakeAlgoX, self).solve(matrix)

    with pytest.raises(NotImplementedError):
        algo = FakeAlgoX()
        algo.solve(Mock())
