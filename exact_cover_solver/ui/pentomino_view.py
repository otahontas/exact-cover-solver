from tkinter import Frame, Tk, ttk, Label, Button, constants

from .view import View
from exact_cover_solver.services.solver import Solver
from typing import Optional, Dict, Tuple


class PentominoView(View):
    def __init__(self, root: Tk, solver: Solver) -> None:
        """Initialize needed variables."""
        self.__cells: Dict[Tuple[int, int], ttk.Frame] = {}
        self.__width: Optional[int] = None
        self.__height: Optional[int] = None
        self.__solver = solver
        self.__solutions = None
        super().__init__(root)

    def _initialize(self) -> None:
        """Show board selection buttons."""
        self._frame = Frame(master=self._root)
        self._draw_buttons()

    def _draw_grid(self) -> None:
        """Draw grid with solution (not yet ready)."""
        self.destroy()
        self._frame = Frame(master=self._root)
        for row in range(self.__height):
            for column in range(self.__width):
                cell = Frame(
                    master=self._frame, width=50, height=50, background="white"
                )
                cell.grid(row=row, column=column, padx=3, pady=3)
                self.__cells[(row, column)] = cell
        label = Label(
            master=self._frame, text=f"Found {len(self.__solutions)} solutions."
        )
        label.grid(columnspan=3, row=self.__height + 1, column=0)
        self.pack()

    def _draw_buttons(self) -> None:
        """Draw selection buttons."""
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

    def _draw_loader(self):
        """Draw loader while calculating solutions."""
        self.destroy()
        self._frame = Frame(master=self._root)
        label = Label(
            master=self._frame,
            text="Hang on, calculating solutions. This might take a while.",
        )
        label.grid(row=1, column=0, padx=5, pady=5)
        progress = ttk.Progressbar(
            self._frame, orient=constants.HORIZONTAL, length=100, mode="indeterminate"
        )
        progress.grid(row=2, column=0, padx=5, pady=5)
        self.pack()

    def _solve_for_pentomino_board_3_20(self):
        """Run event from 3x20 button."""
        self.__height = 3
        self.__width = 20
        self._solve()

    def _solve_for_pentomino_board_4_15(self):
        """Run event from 4x15 button."""
        self.__height = 4
        self.__width = 15
        self._solve()

    def _solve_for_pentomino_board_5_12(self):
        """Run event from 5x12 button."""
        self.__height = 5
        self.__width = 12
        self._solve()

    def _solve_for_pentomino_board_6_10(self):
        """Run event from 6x10 button."""
        self.__height = 6
        self.__width = 10
        self._solve()

    def _solve(self):
        """Solve with set board size."""
        self._draw_loader()
        self.__solutions = self.__solver.solve(self.__height, self.__width)
        self._draw_grid()
