from tkinter import Tk, ttk, constants, messagebox
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
        """initialize nav object."""
        self.__current_problem = current_problem
        self.__current_algo = current_algo
        self.__change_current_problem = change_current_problem
        self.__change_current_algo = change_current_algo
        super().__init__(root)

    def _initialize(self) -> None:
        """Initialize navigation buttons and their functionalities."""
        self._frame = ttk.Frame(master=self._root)

        style = ttk.Style()
        style.configure("W.TButton", background="green")
        pentomino_button_style = (
            "W.TButton" if self.__current_problem == "pentomino" else None
        )
        sudoku_button_style = (
            "W.TButton" if self.__current_problem == "sudoku" else None
        )
        print("current algo", self.__current_algo)
        dlx_button_style = "W.TButton" if self.__current_algo == "dlx" else None
        dictx_button_style = "W.TButton" if self.__current_algo == "dictx" else None

        problem_label = ttk.Label(master=self._frame, text="Select problem to solve")
        pentomino_button = ttk.Button(
            master=self._frame,
            text="Pentomino",
            command=self._set_problem_to_pentomino,
            style=pentomino_button_style,
        )
        sudoku_button = ttk.Button(
            master=self._frame,
            text="Sudoku",
            command=self._set_problem_to_sudoku,
            style=sudoku_button_style,
        )

        algo_label = ttk.Label(master=self._frame, text="Select algorithm to use")
        dlx_button = ttk.Button(
            master=self._frame,
            text="DLX",
            command=self._set_algo_to_dlx,
            style=dlx_button_style,
        )
        dictx_button = ttk.Button(
            master=self._frame,
            text="DictX",
            command=self._set_algo_to_dictx,
            style=dictx_button_style,
        )

        problem_label.grid(row=0, column=0)
        pentomino_button.grid(
            columnspan=2,
            row=1,
            column=0,
            sticky=(constants.E, constants.W),
            padx=5,
            pady=5,
        )
        sudoku_button.grid(
            columnspan=2,
            row=2,
            column=0,
            sticky=(constants.E, constants.W),
            padx=5,
            pady=5,
        )
        algo_label.grid(row=4, column=0)
        dlx_button.grid(
            columnspan=2,
            row=5,
            column=0,
            sticky=(constants.E, constants.W),
            padx=5,
            pady=5,
        )
        dictx_button.grid(
            columnspan=2,
            row=6,
            column=0,
            sticky=(constants.E, constants.W),
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
