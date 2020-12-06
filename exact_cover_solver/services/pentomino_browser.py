"""Classes used to browse pentomino solutions."""

from exact_cover_solver.types import Solution
from typing import List, Tuple, Callable

from exact_cover_solver.data_creators import PentominoCreator
from exact_cover_solver.datastructures.pentomino import Pentominoes

Grid = List[List[str]]


class PentominoBoard:
    """Single pentomino board."""

    _pentominoes = Pentominoes()

    def __init__(
        self,
        board_height: int,
        board_width: int,
        placements: List[List[int]],
        convert_cell_num_to_point: Callable,
    ) -> None:
        self._grid = [[""] * board_width for _ in range(board_height)]
        self._place_pentominoes(placements, convert_cell_num_to_point)

    def _place_pentominoes(
        self, placements: List[List[int]], convert_cell_num_to_point: Callable
    ) -> None:
        """Add pentominoes to board based on given cell list."""
        for placement in placements:
            pentomino_index, *cells = placement
            pentomino_name = self._pentominoes.get_name_by_index(pentomino_index)
            for cell in cells:
                y, x = convert_cell_num_to_point(cell)
                self._grid[y][x] = pentomino_name

    @property
    def board(self) -> Grid:
        """Get two dimensional array grid and return it."""
        return self._grid


class PentominoBoardBrowser:
    """Browser for pentomino boards based on created solutions."""

    def __init__(
        self,
        pentomino_creator: PentominoCreator,
        solutions: List[Solution],
    ) -> None:
        self._pentomino_creator = pentomino_creator
        self._solutions = solutions
        self._boards = []
        self._current_board_index = 0
        self._create_board_on_demand(self._current_board_index)

    @property
    def previous_board(self) -> Grid:
        """Generate previous board."""
        if self._current_board_index == 0:
            raise IndexError("Previous board not available")
        self._current_board_index -= 1
        return self._boards[self._current_board_index].board

    @property
    def current_board(self) -> Grid:
        """Generate current board."""
        return self._boards[self._current_board_index].board

    @property
    def next_board(self) -> Grid:
        """Generate next board."""
        if self._current_board_index > len(self._solutions) - 1:
            raise IndexError("Next board not available")
        self._current_board_index += 1
        try:
            return self._boards[self._current_board_index].board
        except IndexError:
            self._create_board_on_demand(self._current_board_index)
            return self._boards[self._current_board_index].board

    @property
    def board_size(self) -> Tuple[int, int]:
        """Get board size."""
        return self._pentomino_creator.board_size

    @property
    def all_solutions(self) -> List[Solution]:
        """Return all solutions."""
        return self._solutions

    @property
    def current_status(self) -> str:
        """Get current index and amount of all solutions as string."""
        return f"{self._current_board_index + 1} / {len(self._solutions)}"

    def has_previous_board(self) -> bool:
        """Check if previous board can be generated."""
        return self._current_board_index > 0

    def has_next_board(self) -> bool:
        """Check if next board can be generated."""
        return self._current_board_index < len(self._solutions) - 1

    def _create_board_on_demand(self, solutions_index: int) -> None:
        """Create next board if needed.

        Args:
            solutions_index: Index of the solution to be turned into board.
        """
        solution = self._solutions[solutions_index]
        _, set_collection = self._pentomino_creator.create_problem_data()
        board_height, board_width = self._pentomino_creator.board_size
        placements = [set_collection[set_number] for set_number in solution]
        self._boards.append(
            PentominoBoard(
                board_height,
                board_width,
                placements,
                self._pentomino_creator.cell_num_to_point,
            )
        )
