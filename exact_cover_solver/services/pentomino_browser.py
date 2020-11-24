from exact_cover_solver.algos import Solution
from typing import List

from exact_cover_solver.data_creators import SetCollection


class PentominoBoard:
    def __init__(
        self, board_height: int, board_width: int, placements: List[List[int]]
    ):
        self._grid = [[None] * board_width for _ in range(board_height)]
        self._place_pentominoes(placements)

    def _place_pentominoes(self, placements):
        for placement_list in placements:
            pentomino = placement_list[0]
            for cell in placement_list[1:]:
                y = cell // len(self._grid[0])
                x = cell - (y * len(self._grid[0]))
                self._grid[y][x] = pentomino

    @property
    def grid(self):
        return self._grid


class PentominoBoardBrowser:
    def __init__(
        self,
        board_height: int,
        board_width: int,
        solutions: List[Solution],
        set_collection: SetCollection,
    ):
        self._board_width = board_width
        self._board_height = board_height
        self._solutions = solutions
        self._set_collection = set_collection
        self._boards = []
        self._current_board_index = 0
        self._create_board_on_demand(self._current_board_index)

    @property
    def previous_board(self):
        if self._current_board_index <= 0:
            return None
        self._current_board_index -= 1
        return self._boards[self._current_board_index]

    @property
    def current_board(self):
        return self._boards[self._current_board_index]

    @property
    def next_board(self):
        if self._current_board_index >= len(self._set_collection) - 1:
            return None
        self._current_board_index += 1
        if self._current_board_index >= len(self._boards) - 1:
            self._create_board_on_demand(self._current_board_index)
        return self._boards[self._current_board_index]

    def _create_board_on_demand(self, solutions_index: int):
        solution = self._solutions[solutions_index]
        placements = [self._set_collection[row] for row in solution]
        self._boards.append(
            PentominoBoard(self._board_height, self._board_width, placements)
        )
