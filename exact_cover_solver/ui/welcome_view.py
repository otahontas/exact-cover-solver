from tkinter import Tk, Frame, Message

from .view import View


class WelcomeView(View):
    def __init__(self, root: Tk):
        """Initialize object."""
        super().__init__(root)

    def _initialize(self):
        """Initialize welcome text."""
        self._frame = Frame(master=self._root)
        message = Message(
            master=self._frame,
            text=(
                "Hello! This app can be used to solve different exact cover problems. "
                "Choose the problem you want to solve and algorithm you want to use "
                "from the right side of the screen. "
            ),
        )
        message.grid(row=0, column=0)
