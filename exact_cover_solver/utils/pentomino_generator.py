"""Service for generating universe and set collection for pentomino problems."""
from typing import Tuple, List, Dict, Set

from exact_cover_solver.custom_types import Universe, SetCollection

NUMBER_OF_PENTOMINOES = 12
NUMBER_OF_CELLS = 60

Pentomino = List[List[int]]
Point = Tuple[int, int]


class PentominoGenerator:
    """Universe and set generator for different size pentominoes."""

    def __init__(self) -> None:
        """Initialize generator.

        Set up returnable universe, initialize set collection, pentomino representations
        and pentomino numbers for consistency.
        """
        self.__universe: Universe = [
            num for num in range(NUMBER_OF_PENTOMINOES + NUMBER_OF_CELLS)
        ]
        self.__set_collection: SetCollection = []
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
        self.__pentomino_indexes: Dict[str, int] = {
            "V": 0,
            "U": 1,
            "X": 2,
            "T": 3,
            "Y": 4,
            "I": 5,
            "F": 6,
            "P": 7,
            "W": 8,
            "Z": 9,
            "N": 10,
            "L": 11,
        }

    def generate(
        self, board_height: int, board_width: int
    ) -> Tuple[Universe, SetCollection]:
        """Generate universe and set collection with given board size."""
        self.__set_collection.clear()
        for pentomino in self.__pentominoes:
            for orientation in self._generate_all_orientations(
                self.__pentominoes[pentomino]
            ):
                pentomino_height = len(orientation)
                pentomino_width = len(orientation[0])
                for r in range(board_height + 1 - pentomino_height):
                    for c in range(board_width + 1 - pentomino_width):
                        covered = self._solve_covered_cells(
                            orientation, (r, c), board_width
                        )
                        self.__set_collection.append(
                            [
                                self.__pentomino_indexes[pentomino],
                                *[(NUMBER_OF_PENTOMINOES + x) for x in covered],
                            ]
                        )
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
        covered: List[int] = []
        pentomino_height = len(pentomino)
        pentomino_width = len(pentomino[0])
        for r in range(pentomino_height):
            for c in range(pentomino_width):
                cell_number = (y + r) * board_width + x + c
                if cell_number > NUMBER_OF_CELLS:
                    return []
                if pentomino[r][c] == 1:
                    covered.append((y + r) * board_width + x + c)
        return covered

    def _generate_all_orientations(self, pentomino: Pentomino) -> List[Pentomino]:
        """Generate different orientations for this pentomino.

        If pentomino is N, prune half of the orientations away. This helps pruning
        algoX branches.
        """
        seen: Set[str] = set()
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
        if pentomino == self.__pentominoes["N"]:
            return orientations[::2]
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
    def pentominoes(self) -> Dict[str, Pentomino]:
        """Return pentominoes."""
        return self.__pentominoes

    @property
    def pentomino_indexes(self) -> Dict[str, int]:
        """Return pentomino indexes."""
        return self.__pentomino_indexes
