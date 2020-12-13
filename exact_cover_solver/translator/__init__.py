""""""

from exact_cover_solver.types import Solution, SubsetCollection
from typing import List

PentominoBoard = List[List[str]]


class Translator:
    """Translator for decoding solutions to understandable output format."""

    @staticmethod
    def to_pentomino_boards(
        solutions: List[Solution],
        board_height: int,
        board_width: int,
        subset_collection: SubsetCollection,
    ) -> List[PentominoBoard]:
        boards: List[PentominoBoard] = []
        for solution in solutions:
            board: PentominoBoard = [[""] * board_width for _ in range(board_height)]
            for subset_id in solution:
                pentomino_name, *points = subset_collection[subset_id]
                for x, y in points:
                    board[y][x] = pentomino_name
            boards.append(board)
        return boards
