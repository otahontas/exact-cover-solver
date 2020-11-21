from abc import abstractmethod
from tkinter import Tk, Frame, constants
from typing import Optional, Union


class View:
    """Base class for UI views."""

    def __init__(self, root: Tk) -> None:
        """Set up frame and type hint."""
        self._root = root
        self._frame: Optional[Frame] = None
        self._initialize()

    def pack(
        self, fill: Optional[Union[constants.X, constants.BOTH]] = constants.X
    ) -> None:
        """Show all components."""
        self._frame.pack(fill=fill, expand=True)

    def destroy(self) -> None:
        """Hide all components."""
        self._frame.destroy()

    @abstractmethod
    def _initialize(self) -> None:
        pass
