"""Package for handling UI-related functionality."""
from tkinter import Tk, ttk, constants
from typing import Optional
from .menu import AppMenu
from .nav import Nav
from .view import View


class UI:
    """Main UI class."""

    def __init__(self, root: Tk):
        """Initialize ui components"""
        self.__root = root
        self.__current_view: Optional[View] = None
        self.__app_menu: Optional[AppMenu] = None
        self.__nav: Optional[Nav] = None

    def hide_current_view(self):
        """Destroy and hide current view."""
        if self.__current_view:
            self.__current_view.destroy()
        self.__current_view = None

    def start(self):
        """Starts UI, sets some initial configurations and shows default view."""
        self.__app_menu = AppMenu(self.__root, self.quit_app, self.show_about)
        self.__root.config(menu=self.__app_menu.menu)
        self.__nav = Nav(
            self.__root, self.change_current_problem, self.change_current_algo
        )

        vasen = ttk.Frame(master=self.__root)
        heading_label = ttk.Label(master=vasen, text="Login")
        username_label = ttk.Label(master=vasen, text="Username")
        username_entry = ttk.Entry(master=vasen)
        password_label = ttk.Label(master=vasen, text="Password")
        password_entry = ttk.Entry(master=vasen)
        button = ttk.Button(master=vasen, text="Button")
        heading_label.grid(columnspan=2, sticky=constants.W, padx=5, pady=5)
        username_label.grid(padx=5, pady=5)
        username_entry.grid(
            row=1, column=1, sticky=(constants.E, constants.W), padx=5, pady=5
        )
        password_label.grid(padx=5, pady=5)
        password_entry.grid(
            row=2, column=1, sticky=(constants.E, constants.W), padx=5, pady=5
        )
        button.grid(columnspan=2, sticky=(constants.E, constants.W), padx=5, pady=5)
        vasen.grid_columnconfigure(1, weight=1)

        vasen.pack(fill=constants.X, side=constants.LEFT)
        self.__nav.pack(side=constants.RIGHT)

    def quit_app(self) -> None:
        """Exit the program."""
        self.__root.quit()

    def show_about(self) -> None:
        """Show about info."""
        raise NotImplementedError

    def change_current_problem(self, problem: str) -> None:
        print("Problem will be", problem)

    def change_current_algo(self, algo: str) -> None:
        print("Algo will be", algo)
