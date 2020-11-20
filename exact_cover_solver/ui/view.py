from typing import Optional, Union
from tkinter import ttk, constants


class View:
    """Base class for UI views."""
    def __init__(self) -> None:
        """Set up frame and type hint."""
        self._frame: Optional[ttk.Frame] = None

    def pack(self, side: Union[constants.LEFT, constants.RIGHT]):
        """Show all components."""
        self._frame.pack(fill=constants.X, side=side)

    def destroy(self):
        """Hide all components."""
        self._frame.destroy()