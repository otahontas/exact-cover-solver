"""Pentomino view function and helper functions."""
import PySimpleGUI as sg

pentomino_colors = {
    "V": "yellow",
    "U": "slate blue",
    "X": "forest green",
    "T": "medium orchid",
    "Y": "cyan",
    "I": "light blue",
    "F": "red",
    "P": "orange",
    "W": "misty rose",
    "Z": "purple",
    "N": "dark blue",
    "L": "dark gray",
}


def create_pentomino_view(size, grid, prev, next):
    if not size:
        return [
            [sg.Text("Select which pentomino board size you want to use. ")],
            [
                sg.Text(
                    "Program will generate all the solutions for selected "
                    "size and let's you browse solutions one by one. This is a "
                    "blocking operation that might take a while to perform.",
                    auto_size_text=True,
                    size=(50, 5),
                )
            ],
            [
                sg.Button("3x20"),
                sg.Button("4x15"),
                sg.Button("5x12"),
                sg.Button("6x10"),
            ],
        ]
    grid = create_grid(grid)
    buttons = []
    if prev:
        buttons.append(sg.Button("Previous"))
    if next:
        buttons.append(sg.Button("Next"))
    return [[sg.Text("Solution:")], *grid, buttons]


def create_grid(grid):
    return [
        [
            sg.Canvas(
                background_color=pentomino_colors[grid[row][col]],
                size=(20, 20),
                border_width=1,
            )
            for col in range(len(grid[0]))
        ]
        for row in range(len(grid))
    ]
