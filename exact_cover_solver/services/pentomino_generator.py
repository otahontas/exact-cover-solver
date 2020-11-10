"""Service for generating universe and sets for pentomino problems."""

NUMBER_OF_PENTOMINOES = 12
NUMBER_OF_CELLS = 60


class PentominoGenerator:
    """Universe and set generator for different size pentominoes."""

    def __init__(self, height: int, width: int) -> None:
        self.height = height
        self.width = width
        self.universe = [i for i in range(NUMBER_OF_PENTOMINOES + NUMBER_OF_CELLS)]
        self.set_collection = []
        # Different pentominoes as two-dimensional arrays
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
            [[1, 1, 1, 1], [1, 0, 0, 0]]
        ]

    def generate(self):
        pass

    def generate_all_orientations(self, pentomino, pentomino_index):
        seen = set()
        orientations = []
        for transposed in (pentomino, self.transpose(pentomino)):
            for left_right_flipped in (transposed, self.flip_left_right(transposed)):
                for up_down_flipped in (left_right_flipped, self.flip_up_down(left_right_flipped)):
                    orientation_as_string = str(up_down_flipped)
                    if orientation_as_string not in seen:
                        seen.add(orientation_as_string)
                        orientations.append(up_down_flipped)
        if pentomino_index == 10:
            # Skip duplicates for pentomino number 10
            return orientations[::2]
        return orientations

    def flip_up_down(self, pentomino):
        return self.transpose(self.flip_left_right(self.transpose(pentomino)))

    @staticmethod
    def transpose(pentomino):
        return [list(x) for x in zip(*pentomino)]

    @staticmethod
    def flip_left_right(pentomino):
        return [row[::-1] for row in pentomino]
