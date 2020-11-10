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
        pass

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
        """Return pentomino with rows and columsns transposed."""
        return [list(x) for x in zip(*pentomino)]

    @staticmethod
    def flip_left_right(pentomino):
        """Return pentomino with each row reversed."""
        return [row[::-1] for row in pentomino]
