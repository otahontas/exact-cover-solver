"""Package for handling UI-related functionality."""
from tkinter import Tk
from typing import Optional

from .menu import AppMenu
from .nav import Nav
from .view import View
from .welcome_view import WelcomeView
from .pentomino_view import PentominoView


class UI:
    """Main UI class."""

    def __init__(self, root: Tk, solver):
        """Initialize ui components."""
        self.__root = root
        self.__solver = solver
        self.__current_view: Optional[View] = None
        self.__app_menu: Optional[AppMenu] = None
        self.__nav: Optional[Nav] = None

    def start(self):
        """Start UI, set some initial configurations and show default view."""
        self.__app_menu = AppMenu(self.__root, self._quit_app, self._show_about)
        self.__root.config(menu=self.__app_menu.menu)
        self._set_current_nav()
        self._set_current_view()

    def _set_current_view(self):
        """Set view."""
        self._hide_current_view()
        current_problem = self.__solver.problem
        if not current_problem:
            self.__current_view = WelcomeView(self.__root)
        elif current_problem == "pentomino":
            self.__current_view = PentominoView(self.__root, self.__solver)
        self.__current_view.pack()

    def _hide_current_view(self):
        """Destroy and hide current view."""
        if self.__current_view:
            self.__current_view.destroy()
        self.__current_view = None

    def _set_current_nav(self):
        """Set nav."""
        self._hide_current_nav()
        current_problem = self.__solver.problem
        current_algo = self.__solver.algorithm
        self.__nav = Nav(
            self.__root,
            self._change_current_problem,
            self._change_current_algo,
            current_problem,
            current_algo,
        )
        self.__nav.pack()

    def _hide_current_nav(self):
        """Destroy and hide current nav."""
        if self.__nav:
            self.__nav.destroy()
        self.__nav = None

    def _quit_app(self) -> None:
        """Exit the program."""
        self.__root.quit()

    def _show_about(self) -> None:
        """Show about info."""
        raise NotImplementedError

    def _change_current_problem(self, problem: str) -> None:
        """Change current problem in program logic and app."""
        self.__solver.problem = problem
        self._set_current_nav()
        self._set_current_view()

    def _change_current_algo(self, algo: str) -> None:
        """Change current algo in program logic and app."""
        self.__solver.algorithm = algo
        self._set_current_nav()
