from tkinter import Menu, Tk

from typing import Callable


class AppMenu:
    def __init__(self, root: Tk, quit_app: Callable, show_about: Callable) -> None:
        """initialize menu object."""
        self.__menu = Menu(root)
        self.__quit_app = quit_app
        self.__show_about = show_about
        self._initialize()

    def _initialize(self) -> None:
        """Initialize needed menus and their functionalities."""
        file_menu = Menu(self.__menu)
        self.__menu.add_cascade(label="File", menu=file_menu)
        file_menu.add_command(label="Exit", command=self.__quit_app)

        help_menu = Menu(self.__menu)
        self.__menu.add_cascade(label="Help", menu=help_menu)
        help_menu.add_command(label="About", command=self.__show_about)

    @property
    def menu(self) -> Menu:
        """Return menu object"""
        return self.__menu
