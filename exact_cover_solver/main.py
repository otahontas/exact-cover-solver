"""Main entrypoint for program."""
from tkinter import Tk

from exact_cover_solver.ui import UI
from exact_cover_solver.services.solver import Solver


def main() -> None:
    """Launch UI from main, initialize objects program is using."""
    window = Tk()
    window.title("Exact cover solver")

    solver = Solver()

    ui = UI(window, solver)
    ui.start()
    window.mainloop()


if __name__ == "__main__":
    main()
