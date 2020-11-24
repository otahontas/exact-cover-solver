"""Dancing links implementation for algorithm X."""

from typing import List

from exact_cover_solver.algos import AlgorithmX, Solution
from exact_cover_solver.datastructures.dictmatrix import DictMatrix


class DictX(AlgorithmX):
    """Dictionary based implementation for algorithm X."""

    def solve(self, matrix: AlgorithmX[DictMatrix]) -> List[Solution]:
        """Not implemented."""
        raise NotImplementedError
