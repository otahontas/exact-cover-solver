"""Universe and set collection creator for pentomino problem."""

from exact_cover_solver.data_creators import (
    DataCreator,
    Constrains,
)


class ParsingError(Exception):
    """Exception raised when board size not initialized.

    Attributes:
        message -- explanation of the error
    """

    def __init__(self, constrain: str, given_input: str):
        """Initialize error with message."""
        if constrain == "universe":
            message = "You should give a list of elements separated by commas."
        else:
            message = (
                "You should give each set as list of commas and sets separated "
                "by semicolons."
            )
        self.message = (
            f"Parsing {constrain} failed with following input:"
            f" {given_input}\n{message}"
        )
        super().__init__(self.message)


class GenericCreator(DataCreator):
    """Universe and set collection creator for pentomino problem.

    Problem has always same amount of pentominoes, cells on board and same universe,
    but the board size varies.
    """

    def __init__(self, universe: str, set_collection: str) -> None:
        """Initialize and try to parse string input.

        Args:
            universe: elements as string, separated by commas
            set_collection: sets as string, elements separated by commas and sets
                separated by semicolons.
        """
        self._universe = [int(x.strip()) for x in universe.split(",")]
        self._universe_as_set = set(self._universe)
        parsed_sets = set_collection.split(";")
        self._set_collection = []
        for parsed_set in parsed_sets:
            self._set_collection.append([int(x.strip()) for x in parsed_set.split()])

    def create_constrains(self) -> Constrains:
        """Create data representing the pentomino problem in certain board size.

        Returns:
            Tuple containing universe and set collection.

        Raises:
            BoardSizeNotInitializedError: Raised if current height or width is None.
        """
        return self._universe, self._set_collection
