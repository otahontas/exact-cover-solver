from tkinter import Tk, ttk, Message

from .view import View


class WelcomeView(View):
    def __init__(self, root: Tk):
        super().__init__(root)

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)
        message = Message(
            master=self._frame,
            text=(
                "Hello! This app can be used to solve different exact cover problems. "
                "Choose the problem you want to solve and algorithm you want to use from the right side of the "
                "screen. "
            ),
        )
        message.grid(row=0, column=0)
