"""Service for generating universe and sets for pentomino problems."""

NUMBER_OF_PENTOMINOES = BASE = 12
NUMBER_OF_CELLS = 60


class PentominoGenerator:
    """Universe and set generator for different size pentominoes."""

    def __init__(self, height: int, width: int) -> None:
        """Initialize generator."""
        self.height = height
        self.width = width
        self.universe = [i for i in range(NUMBER_OF_PENTOMINOES + NUMBER_OF_CELLS)]
        self.set_collection = []
        # Different pentominoes as two-dimensional arrays
        # Order: V, U, X, T, Y, I, F, P, W, Z, N, L
        self.pentominoes = [
            [[1, 1, 1], [1, 0, 0], [1, 0, 0]],
            [[1, 0, 1], [1, 1, 1]],
            [[0, 1, 0], [1, 1, 1], [0, 1, 0]],
            [[1, 0, 0], [1, 1, 1], [1, 0, 0]],
            [[1, 1, 1, 1], [0, 1, 0, 0]],
            [[1, 1, 1, 1, 1]],
            [[0, 1, 0], [1, 1, 0], [0, 1, 1]],
            [[1, 1, 1], [1, 1, 0]],
            [[1, 1, 0], [0, 1, 1], [0, 0, 1]],
            [[1, 0, 0], [1, 1, 1], [0, 0, 1]],
            [[1, 1, 0, 0], [0, 1, 1, 1]],
            [[1, 1, 1, 1], [1, 0, 0, 0]],
        ]

    def generate(self):
        """Generate universe and set collection for algo x."""
        self.set_collection.clear()
        set_number = 0
        for pentomino_index, pentomino in enumerate(self.pentominoes):
            for orientation in self.generate_all_orientations(pentomino):
                pentomino_height = len(orientation)
                pentomino_width = len(orientation[0])
                for r in range(self.height + 1 - pentomino_height):
                    for c in range(self.width + 1 - pentomino_width):
                        covered = [
                            pentomino_index,
                            *[
                                (BASE + x)
                                for x in self.solve_covered_cells(orientation, (r, c))
                            ],
                        ]
                        self.set_collection.append((set_number, covered))
                        set_number += 1
        return (
            self.universe,
            self.set_collection,
        )

    def solve_covered_cells(self, pentomino, start):
        """Find which cells this pentomino will cover."""
        y, x = start
        covered = []
        pentomino_height = len(pentomino)
        pentomino_width = len(pentomino[0])
        for r in range(pentomino_height):
            for c in range(pentomino_width):
                if pentomino[r][c] == 1:
                    covered.append((y + r) * self.width + x + c)
        return covered

    def generate_all_orientations(self, pentomino):
        """Generate different orientations for this pentomino."""
        seen = set()
        orientations = []
        for transposed in (pentomino, self.transpose(pentomino)):
            for left_right_flipped in (transposed, self.flip_left_right(transposed)):
                for up_down_flipped in (
                    left_right_flipped,
                    self.flip_up_down(left_right_flipped),
                ):
                    orientation_as_string = str(up_down_flipped)
                    if orientation_as_string not in seen:
                        seen.add(orientation_as_string)
                        orientations.append(up_down_flipped)
        if pentomino == self.pentominoes[10]:
            # Skip duplicates for pentomino number 10
            return orientations[::2]
        return orientations

    @staticmethod
    def flip_up_down(pentomino):
        """Return pentomino with rows reversed."""
        return pentomino[::-1]

    @staticmethod
    def transpose(pentomino):
        """Return pentomino with rows and columns transposed."""
        return [list(x) for x in zip(*pentomino)]

    @staticmethod
    def flip_left_right(pentomino):
        """Return pentomino with each row reversed."""
        return [row[::-1] for row in pentomino]
