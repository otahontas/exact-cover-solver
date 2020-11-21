"""Service for generating universe and set collection for pentomino problems."""
from typing import Tuple, List, Dict
from exact_cover_solver.types import Universe, SetCollection

NUMBER_OF_PENTOMINOES = 12
NUMBER_OF_CELLS = 60

Pentomino = List[List[int]]
Point = Tuple[int, int]


class PentominoGenerator:
    """Universe and set generator for different size pentominoes."""

    def __init__(self) -> None:
        """Initialize generator."""
        self.__universe: Universe = [
            num for num in range(NUMBER_OF_PENTOMINOES + NUMBER_OF_CELLS)
        ]
        self.__set_collection: SetCollection = []
        # TODO turn into tuples so these can be hashed
        self.__pentominoes: Dict[str, Pentomino] = {
            "V": [[1, 1, 1], [1, 0, 0], [1, 0, 0]],
            "U": [[1, 0, 1], [1, 1, 1]],
            "X": [[0, 1, 0], [1, 1, 1], [0, 1, 0]],
            "T": [[1, 0, 0], [1, 1, 1], [1, 0, 0]],
            "Y": [[1, 1, 1, 1], [0, 1, 0, 0]],
            "I": [[1, 1, 1, 1, 1]],
            "F": [[0, 1, 0], [1, 1, 0], [0, 1, 1]],
            "P": [[1, 1, 1], [1, 1, 0]],
            "W": [[1, 1, 0], [0, 1, 1], [0, 0, 1]],
            "Z": [[1, 0, 0], [1, 1, 1], [0, 0, 1]],
            "N": [[1, 1, 0, 0], [0, 1, 1, 1]],
            "L": [[1, 1, 1, 1], [1, 0, 0, 0]],
        }

    def generate(
        self, board_height: int, board_width: int
    ) -> Tuple[Universe, SetCollection]:
        """Generate universe and set collection with given board size."""
        self.__set_collection.clear()
        set_number = 0  # TODO: do we even need this?
        for pentomino_index, pentomino in enumerate(self.__pentominoes.values()):
            for orientation in self._generate_all_orientations(pentomino):
                pentomino_height = len(orientation)
                pentomino_width = len(orientation[0])
                for r in range(board_height + 1 - pentomino_height):
                    for c in range(board_width + 1 - pentomino_width):
                        covered = [
                            pentomino_index,
                            *[
                                (NUMBER_OF_PENTOMINOES + x)
                                for x in self._solve_covered_cells(
                                    orientation, (r, c), board_width
                                )
                            ],
                        ]
                        self.__set_collection.append((str(set_number), covered))
                        set_number += 1
        return (
            self.__universe,
            self.__set_collection,
        )

    @staticmethod
    def _solve_covered_cells(
        pentomino: Pentomino, start: Point, board_width: int
    ) -> List[int]:
        """Find which cells this pentomino will cover."""
        y, x = start
        covered = []
        pentomino_height = len(pentomino)
        pentomino_width = len(pentomino[0])
        for r in range(pentomino_height):
            for c in range(pentomino_width):
                if pentomino[r][c] == 1:
                    covered.append((y + r) * board_width + x + c)
        return covered

    def _generate_all_orientations(self, pentomino: Pentomino) -> List[Pentomino]:
        """Generate different orientations for this pentomino."""
        seen = set()
        orientations = []
        for transposed in (pentomino, self._transpose(pentomino)):
            for left_right_flipped in (transposed, self._flip_left_right(transposed)):
                for up_down_flipped in (
                    left_right_flipped,
                    self._flip_up_down(left_right_flipped),
                ):
                    orientation_as_string = str(up_down_flipped)
                    if orientation_as_string not in seen:
                        seen.add(orientation_as_string)
                        orientations.append(up_down_flipped)
        return orientations

    @staticmethod
    def _flip_up_down(pentomino: Pentomino) -> Pentomino:
        """Return pentomino with rows reversed."""
        return pentomino[::-1]

    @staticmethod
    def _transpose(pentomino: Pentomino) -> Pentomino:
        """Return pentomino with rows and columns transposed."""
        return [list(x) for x in zip(*pentomino)]

    @staticmethod
    def _flip_left_right(pentomino: Pentomino) -> Pentomino:
        """Return pentomino with each row reversed."""
        return [row[::-1] for row in pentomino]

    @property
    def pentominoes(self) -> List[Pentomino]:
        return [pentomino for pentomino in self.__pentominoes.values()]
