"""Universe and set collection creator for generic problems."""

from exact_cover_solver.types import ProblemData, SubsetCollection, Universe


class ParsingError(Exception):
    """Exception raised when board size not initialized.

    Attributes:
        message -- explanation of the error
    """

    def __init__(self, message: str, given_input: str) -> None:
        """Initialize error with message."""
        self.message = (
            f"Parsing failed with following input:" f" {given_input}\n{message}"
        )
        super().__init__(self.message)


class GenericCreator:
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
        self._parse_universe(universe)
        self._parse_set_collection(set_collection)

    def create_problem_data(self) -> ProblemData:
        """Create data representing the pentomino problem in certain board size.

        Returns:
            Tuple containing universe and set collection.

        Raises:
            BoardSizeNotInitializedError: Raised if current height or width is None.
        """
        return self._universe, self._set_collection

    def _parse_universe(self, universe: Universe) -> None:
        """Parse universe into correct format."""
        try:
            parsed_universe = [int(x.strip()) for x in universe.split(",")]
        except ValueError:
            message = (
                "For universe you should give a list of elements separated by "
                "commas, e.g '1,2,3,4'"
            )
            raise ParsingError(message, universe)

        if len(parsed_universe) != len(set(parsed_universe)):
            raise ParsingError("Only unique elements are allowed.", universe)

        self._universe = parsed_universe

    def _parse_set_collection(self, set_collection: SubsetCollection) -> None:
        """Parse set collection into correct format."""
        universe_as_set = set(self._universe)
        self._set_collection = []
        for single_set in set_collection.split(";"):
            try:
                parsed_set = [int(x.strip()) for x in single_set.split(",")]
            except ValueError:
                message = (
                    "For set collection you should give each set as list of commas and "
                    "sets separated by semicolons, e.g '1,3;2,4'."
                )
                raise ParsingError(message, set_collection)
            for element in parsed_set:
                if element not in universe_as_set:
                    raise ParsingError(
                        "Set includes elements not in universe.",
                        f"universe: {self._universe}, set_collection: {set_collection}",
                    )
            self._set_collection.append(parsed_set)
