"""Dancing links implementation for algorithm X."""

from typing import List

from exact_cover_solver.algos import AlgorithmX, Solution
from exact_cover_solver.datastructures.dictmatrix import DictMatrix


class DictX(AlgorithmX):
    """Dictionary based implementation for algorithm X."""

    def __init__(self) -> None:
        super().__init__()

    def solve(self, matrix: AlgorithmX[DictMatrix]) -> List[Solution]:
        """Not implemented."""
        if not isinstance(matrix, DictMatrix):
            raise ValueError("Given matrix can't be processed by DictX algorithm.")
        X = matrix.grid
        Y = {index: elements for index, elements in enumerate(matrix._set_collection)}
        self._search(X, Y)
        return self._solutions

    def _search(self, X, Y, partial: Solution = None) -> None:
        if not partial:
            partial: Solution = []
        if not X:
            self._solutions.append(list(partial))
        else:
            c = min(X, key=lambda c: len(X[c]))
            for r in list(X[c]):
                partial.append(r)
                cols = self._cover(X, Y, r)
                self._search(X, Y, partial)
                self._uncover(X, Y, r, cols)
                partial.pop()

    @staticmethod
    def _cover(X, Y, r):
        cols = []
        for j in Y[r]:
            for i in X[j]:
                for k in Y[i]:
                    if k != j:
                        X[k].remove(i)
            cols.append(X.pop(j))
        return cols

    @staticmethod
    def _uncover(X, Y, r, cols):
        for j in reversed(Y[r]):
            X[j] = cols.pop()
            for i in X[j]:
                for k in Y[i]:
                    if k != j:
                        X[k].add(i)


# Add all private methods to pdoc when generating documentation
__pdoc__ = {
    f"DictX.{func}": True
    for func in dir(DictX)
    if callable(getattr(DictX, func)) and func.startswith("_")
}
