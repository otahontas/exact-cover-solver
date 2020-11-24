"""Main entrypoint for program."""
from exact_cover_solver.ui import UI
from exact_cover_solver.services.solver import Solver


def main() -> None:
    """Launch UI from main, initialize solver service that UI is using."""
    solver = Solver()
    ui = UI(solver)
    ui.run()


if __name__ == "__main__":
    main()
