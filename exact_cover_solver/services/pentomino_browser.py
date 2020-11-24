from exact_cover_solver.algos import Solution
from typing import List, Dict

from exact_cover_solver.data_creators import SetCollection


class PentominoBoard:
    _pentomino_names: Dict[str, int] = {
        0: "V",
        1: "U",
        2: "X",
        3: "T",
        4: "Y",
        5: "I",
        6: "F",
        7: "P",
        8: "W",
        9: "Z",
        10: "N",
        11: "L",
    }

    def __init__(
        self, board_height: int, board_width: int, placements: List[List[int]]
    ):
        self._grid = [[None] * board_width for _ in range(board_height)]
        self._place_pentominoes(placements)

    def _place_pentominoes(self, placements):
        for placement_list in placements:
            pentomino = self._pentomino_names[placement_list[0]]
            for cell in placement_list[1:]:
                cell -= 12
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
        return self._boards[self._current_board_index].grid

    @property
    def current_board(self):
        return self._boards[self._current_board_index].grid

    @property
    def next_board(self):
        if self._current_board_index >= len(self._solutions) - 1:
            return None
        self._current_board_index += 1
        if self._current_board_index >= len(self._boards) - 1:
            self._create_board_on_demand(self._current_board_index)
        return self._boards[self._current_board_index].grid

    @property
    def has_previous_board(self):
        return self._current_board_index > 0

    @property
    def has_next_board(self):
        return self._current_board_index < len(self._solutions) - 1

    @property
    def size(self):
        return self._board_height, self._board_width


    def _create_board_on_demand(self, solutions_index: int):
        solution = self._solutions[solutions_index]
        placements = [self._set_collection[row] for row in solution]
        self._boards.append(
            PentominoBoard(self._board_height, self._board_width, placements)
        )
