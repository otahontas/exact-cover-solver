"""Package for handling UI-related functionality."""
from tkinter import Tk, ttk, constants, Menu
from abc import ABC, abstractmethod
from typing import Optional


class View(ABC):
    """Abstract base class for UI views."""

    @abstractmethod
    def destroy(self):
        """Abstract solving method that should be implemented by subclasses."""


class UI:
    """Main UI class."""

    def __init__(self, root: Tk):
        """Initialize ui components"""
        self.__root = root
        self.__current_view: Optional[View] = None

    def hide_current_view(self):
        """Destroy and hide current view."""
        if self.__current_view:
            self.__current_view.destroy()
        self.__current_view = None

    def start(self):
        """Starts UI with greeting view set as default."""
        menu = Menu(self.__root)
        self.__root.config(menu=menu)

        file_menu = Menu(menu)
        menu.add_cascade(label="File", menu=file_menu)
        file_menu.add_command(label="Exit", command=self.exit)

        help_menu = Menu(menu)
        menu.add_cascade(label="Help", menu=help_menu)
        help_menu.add_command(label="About")

        vasen = ttk.Frame(master=self.__root)
        heading_label = ttk.Label(master=vasen, text="Login")
        username_label = ttk.Label(master=vasen, text="Username")
        username_entry = ttk.Entry(master=vasen)
        password_label = ttk.Label(master=vasen, text="Password")
        password_entry = ttk.Entry(master=vasen)
        button = ttk.Button(master=vasen, text="Button")
        heading_label.grid(columnspan=2, sticky=constants.W, padx=5, pady=5)
        username_label.grid(padx=5, pady=5)
        username_entry.grid(row=1, column=1, sticky=(constants.E, constants.W), padx=5, pady=5)
        password_label.grid(padx=5, pady=5)
        password_entry.grid(row=2, column=1, sticky=(constants.E, constants.W), padx=5, pady=5)
        button.grid(columnspan=2, sticky=(constants.E, constants.W), padx=5, pady=5)
        vasen.grid_columnconfigure(1, weight=1)

        oikea = ttk.Frame(master=self.__root)
        heading_label_oik = ttk.Label(master=oikea, text="Login")
        username_label_oik = ttk.Label(master=oikea, text="Username")
        username_entry_oik = ttk.Entry(master=oikea)
        password_label_oik = ttk.Label(master=oikea, text="Password")
        password_entry_oik = ttk.Entry(master=oikea)
        button_oik = ttk.Button(master=oikea, text="Button")
        heading_label_oik.grid(columnspan=2, sticky=constants.W, padx=5, pady=5)
        username_label_oik.grid(padx=5, pady=5)
        username_entry_oik.grid(row=1, column=1, sticky=(constants.E, constants.W), padx=5, pady=5)
        password_label_oik.grid(padx=5, pady=5)
        password_entry_oik.grid(row=2, column=1, sticky=(constants.E, constants.W), padx=5, pady=5)
        button_oik.grid(columnspan=2, sticky=(constants.E, constants.W), padx=5, pady=5)
        oikea.grid_columnconfigure(1, weight=1)

        vasen.pack(fill=constants.X, side=constants.LEFT)
        oikea.pack(fill=constants.X, side=constants.RIGHT)

    def exit(self):
        """Exit the program."""
        self.__root.quit()
