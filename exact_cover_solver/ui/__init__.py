"""Package for handling UI-related functionality."""
from tkinter import Tk, ttk, constants
from typing import Optional
from .menu import AppMenu
from .nav import Nav
from .view import View
from .welcome_view import WelcomeView


class UI:
    """Main UI class."""

    def __init__(self, root: Tk):
        """Initialize ui components"""
        self.__root = root
        self.__current_view: Optional[View] = None
        self.__app_menu: Optional[AppMenu] = None
        self.__nav: Optional[Nav] = None

    def start(self):
        """Starts UI, sets some initial configurations and shows default view."""
        self.__app_menu = AppMenu(self.__root, self._quit_app, self._show_about)
        self.__root.config(menu=self.__app_menu.menu)
        self.__nav = Nav(
            self.__root, self._change_current_problem, self._change_current_algo
        )
        self.__nav.pack(side=constants.RIGHT)
        self._set_current_view()

    def _set_current_view(self, problem: str = ""):
        self._hide_current_view()
        if not problem:
            self.__current_view = WelcomeView(self.__root)
        elif problem == "pentomino":
            pass
        elif problem == "sudoku":
            pass
        else:
            # TODO: should really show error, not raise errors
            raise ValueError("Unknown problem type.")
        print(self.__current_view)
        self.__current_view.pack(side=constants.LEFT)

    def _hide_current_view(self):
        """Destroy and hide current view."""
        if self.__current_view:
            self.__current_view.destroy()
        self.__current_view = None

    def _quit_app(self) -> None:
        """Exit the program."""
        self.__root.quit()

    def _show_about(self) -> None:
        """Show about info."""
        raise NotImplementedError

    def _change_current_problem(self, problem: str) -> None:
        print("Problem will be", problem)

    def _change_current_algo(self, algo: str) -> None:
        print("Algo will be", algo)
