from abc import abstractmethod
from tkinter import Tk, ttk, constants
from typing import Optional, Union


class View:
    """Base class for UI views."""

    def __init__(self, root: Tk) -> None:
        """Set up frame and type hint."""
        self._root = root
        self._frame: Optional[ttk.Frame] = None
        self._initialize()

    def pack(self, side: Union[constants.LEFT, constants.RIGHT]) -> None:
        """Show all components."""
        self._frame.pack(fill=constants.X, side=side)

    def destroy(self) -> None:
        """Hide all components."""
        self._frame.destroy()

    @abstractmethod
    def _initialize(self) -> None:
        pass
