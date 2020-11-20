from tkinter import Tk, ttk, constants
from typing import Callable
from .view import View


class Nav(View):
    def __init__(
        self, root: Tk, change_current_problem: Callable, change_current_algo: Callable
    ) -> None:
        """initialize nav object."""
        super().__init__(root)
        self.__change_current_problem = change_current_problem
        self.__change_current_algo = change_current_algo

    def _initialize(self) -> None:
        """Initialize navigation buttons and their functionalities."""
        self._frame = ttk.Frame(master=self._root)
        problem_label = ttk.Label(master=self._frame, text="Select problem to solve")
        pentomino_button = ttk.Button(
            master=self._frame, text="Pentomino", command=self._set_problem_to_pentomino
        )
        sudoku_button = ttk.Button(
            master=self._frame, text="Sudoku", command=self._set_problem_to_sudoku
        )
        algo_label = ttk.Label(master=self._frame, text="Select algorithm to use")
        dlx_button = ttk.Button(
            master=self._frame, text="DLX", command=self._set_algo_to_dlx
        )
        dictx_button = ttk.Button(
            master=self._frame, text="DictX", command=self._set_algo_to_dictx
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

    def _set_problem_to_sudoku(self):
        raise NotImplementedError

    def _set_algo_to_dlx(self):
        self.__change_current_problem("dlx")

    def _set_algo_to_dictx(self):
        raise NotImplementedError
