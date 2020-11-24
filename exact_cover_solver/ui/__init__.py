"""Package for handling UI-related functionality."""
from typing import Optional

import PySimpleGUI as sg

from ..services.solver import Solver, AlgorithmNotChosenError
from .pentomino_view import create_pentomino_view


class UI:
    """Main UI class."""

    def __init__(self, solver: Solver) -> None:
        """Initialize ui components."""
        self._title = "Exact cover solver"
        self._solver = solver
        self._window: Optional[sg.Window] = None
        self._pentomino_browser = None
        self._update_view()

    def run(self) -> None:
        """Start event Loop to process "events" and get the "values" of the inputs."""
        while True:
            event, values = self._window.read()
            if event == sg.WIN_CLOSED or event == "Exit program":
                break
            if event == "DLX":
                self._change_current_algo("DLX")
            if event == "DictX":
                sg.popup("Not implemented yet.")
            if event == "Pentomino":
                self._update_view("Pentomino")
            if event == "Generic":
                sg.popup("Not implemented yet.")
            if event == "Sudoku":
                sg.popup("Not implemented yet.")
            if event == "Next":
                grid = self._pentomino_browser.next_board
                self._generate_board(grid)
            if event == "Previous":
                grid = self._pentomino_browser.previous_board
                self._generate_board(grid)
            if event == "3x20":
                self._generate_solutions(3, 20)
            if event == "4x15":
                self._generate_solutions(4, 15)
            if event == "5x12":
                self._generate_solutions(5, 12)
            if event == "6x10":
                self._generate_solutions(6, 10)
        self._window.close()

    def _generate_board(self, grid):
        prev = self._pentomino_browser.has_previous_board
        next = self._pentomino_browser.has_next_board
        size = self._pentomino_browser.size
        self._update_view("Pentomino", size, grid, prev, next)

    def _generate_solutions(self, height, width):
        try:
            self._pentomino_browser = self._solver.solve_pentomino_problem(
                height, width
            )
        except AlgorithmNotChosenError:
            sg.popup("Please select which algorithm to use.")
            return
        grid = self._pentomino_browser.current_board
        self._generate_board(grid)

    def _update_view(
        self, problem=None, size=None, grid=None, prev=None, next=None
    ) -> None:
        """Create view based on current selections."""
        if self._window:
            self._window.close()
        try:
            algo_name = self._solver.algorithm
        except AlgorithmNotChosenError:
            algo_name = ""
        algos = [
            [sg.Text("Select algo to use")],
            [sg.Button("DLX"), sg.Button("DictX")],
            [
                sg.Text("Algorithm currently in use: "),
                sg.Text(algo_name, size=(15, 1), key="-CURRENT_ALGO-"),
            ],
        ]
        problems = [
            [sg.Text("Select problem to solve")],
            [sg.Button("Generic"), sg.Button("Pentomino"), sg.Button("Sudoku")],
        ]
        separator = [sg.Canvas(size=(500, 20))]
        main = self._create_main_view(problem, size, grid, prev, next)
        footer = [sg.Button("Exit program"), sg.Text(size=(15, 1), key="-ERROR-")]
        layout = [*algos, *problems, separator, *main, footer]
        self._window = sg.Window(self._title, layout)

    def _change_current_algo(self, algo_name: str) -> None:
        self._solver.algorithm = algo_name
        self._window["-CURRENT_ALGO-"].update(self._solver.algorithm)

    def _create_main_view(self, problem, size, grid, prev, next):
        if not problem:
            return [[sg.Canvas(size=(500, 300))]]
        if problem == "Pentomino":
            if not size:
                return create_pentomino_view(size, grid, prev, next)
            return create_pentomino_view(size, grid, prev, next)
