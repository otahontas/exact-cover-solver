from tkinter import Tk, Frame, Button, Label, messagebox
from typing import Callable, Optional

from .view import View


class Nav(View):
    def __init__(
        self,
        root: Tk,
        change_current_problem: Callable,
        change_current_algo: Callable,
        current_problem: Optional[str],
        current_algo: Optional[str],
    ) -> None:
        """Initialize nav object."""
        self.__current_problem = current_problem
        self.__current_algo = current_algo
        self.__change_current_problem = change_current_problem
        self.__change_current_algo = change_current_algo
        super().__init__(root)

    def _initialize(self) -> None:
        """Initialize navigation buttons and their functionalities."""
        self._frame = Frame(master=self._root)

        pentomino_button_background = (
            "green" if self.__current_problem == "pentomino" else None
        )
        sudoku_button_background = (
            "green" if self.__current_problem == "sudoku" else None
        )
        dlx_button_background = "green" if self.__current_algo == "dlx" else None
        dictx_button_background = "green" if self.__current_algo == "dictx" else None

        problem_label = Label(master=self._frame, text="Select problem to solve")
        pentomino_button = Button(
            master=self._frame,
            text="Pentomino",
            command=self._set_problem_to_pentomino,
            background=pentomino_button_background,
        )
        sudoku_button = Button(
            master=self._frame,
            text="Sudoku",
            command=self._set_problem_to_sudoku,
            background=sudoku_button_background,
        )

        algo_label = Label(master=self._frame, text="Select algorithm to use")
        dlx_button = Button(
            master=self._frame,
            text="DLX",
            command=self._set_algo_to_dlx,
            background=dlx_button_background,
        )
        dictx_button = Button(
            master=self._frame,
            text="DictX",
            command=self._set_algo_to_dictx,
            background=dictx_button_background,
        )

        problem_label.grid(row=0, column=0)
        pentomino_button.grid(
            row=0,
            column=1,
            padx=5,
            pady=5,
        )
        sudoku_button.grid(
            row=0,
            column=2,
            padx=5,
            pady=5,
        )
        algo_label.grid(row=0, column=3)
        dlx_button.grid(
            row=0,
            column=4,
            padx=5,
            pady=5,
        )
        dictx_button.grid(
            row=0,
            column=5,
            padx=5,
            pady=5,
        )

    def _set_problem_to_pentomino(self):
        self.__change_current_problem("pentomino")

    @staticmethod
    def _set_problem_to_sudoku():
        messagebox.showerror("Error", "Sudoku solver not implemented yet!")

    def _set_algo_to_dlx(self):
        self.__change_current_algo("dlx")

    @staticmethod
    def _set_algo_to_dictx():
        messagebox.showerror("Error", "Dictionary based algoX not implemented yet!")
