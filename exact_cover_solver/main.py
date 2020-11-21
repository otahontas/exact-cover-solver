"""Main entrypoint for program."""
from tkinter import Tk

from exact_cover_solver.ui import UI


def main() -> None:
    """Launch UI from main."""
    window = Tk()
    window.title("TkInter example")
    ui = UI(window)
    ui.start()
    window.mainloop()


if __name__ == "__main__":
    main()
