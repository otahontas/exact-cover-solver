"""Main entrypoint for program."""
from exact_cover_solver.ui import UI
from tkinter import Tk


def main() -> None:
    """Launch UI from main."""
    window = Tk()
    window.title("TkInter example")
    ui = UI(window)
    ui.start()
    window.mainloop()


if __name__ == "__main__":
    main()
