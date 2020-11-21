from tkinter import Frame, Tk, ttk, Label, Button, messagebox

from .view import View
from exact_cover_solver.services.solver import Solver
from typing import Optional, Dict, Tuple, Callable


class PentominoView(View):
    def __init__(self, root: Tk, solver: Solver) -> None:
        self.__cells: Dict[Tuple[int, int], ttk.Frame] = {}
        self.__width: Optional[int] = None
        self.__height: Optional[int] = None
        super().__init__(root)

    def _initialize(self) -> None:
        self._frame = Frame(master=self._root)
        self._draw_buttons()

    def _draw_grid(self) -> None:
        for row in range(self.__height):
            for column in range(self.__width):
                cell = Frame(
                    master=self._frame, width=50, height=50, background="white"
                )
                cell.grid(row=row, column=column, padx=3, pady=3)
                self.__cells[(row, column)] = cell

    def _draw_buttons(self) -> None:
        label = Label(
            master=self._frame, text="Select which pentomino board solutions to solve"
        )
        button_3_20 = Button(
            master=self._frame,
            text="3x20",
            command=self._solve_for_pentomino_board_3_20,
        )
        button_4_15 = Button(
            master=self._frame,
            text="4x15",
            command=self._solve_for_pentomino_board_4_15,
        )
        button_5_12 = Button(
            master=self._frame,
            text="5x12",
            command=self._solve_for_pentomino_board_5_12,
        )
        button_6_10 = Button(
            master=self._frame,
            text="6x10",
            command=self._solve_for_pentomino_board_6_10,
        )
        label.grid(row=1, column=0, padx=5, pady=5)
        button_3_20.grid(row=2, column=0, padx=5, pady=5)
        button_4_15.grid(row=2, column=1, padx=5, pady=5)
        button_5_12.grid(row=2, column=2, padx=5, pady=5)
        button_6_10.grid(row=2, column=3, padx=5, pady=5)

    @staticmethod
    def _solve_for_pentomino_board_3_20():
        messagebox.showerror("Error", "not implemented yet!")

    @staticmethod
    def _solve_for_pentomino_board_4_15():
        messagebox.showerror("Error", "not implemented yet!")

    @staticmethod
    def _solve_for_pentomino_board_5_12():
        messagebox.showerror("Error", "not implemented yet!")

    def _solve_for_pentomino_board_6_10(self):
        self.__height = 6
        self.__width = 10
        self._frame = Frame(master=self._root)
        self._draw_grid()
        self.pack()
