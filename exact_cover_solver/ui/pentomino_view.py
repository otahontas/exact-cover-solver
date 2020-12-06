"""Pentomino view function and helper functions."""
import PySimpleGUI

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


def create_pentomino_view(pentomino_browser=None, board_to_get="current"):
    if not pentomino_browser:
        return [
            [PySimpleGUI.Text("Select which pentomino board size you want to use. ")],
            [
                PySimpleGUI.Text(
                    "Program will generate all the solutions for selected "
                    "size and let's you browse solutions one by one. This is a "
                    "blocking operation that might take a while to perform.",
                    auto_size_text=True,
                    size=(50, 5),
                )
            ],
            [
                PySimpleGUI.Button("3x20"),
                PySimpleGUI.Button("4x15"),
                PySimpleGUI.Button("5x12"),
                PySimpleGUI.Button("6x10"),
            ],
        ]
    if board_to_get == "next":
        grid = create_grid(pentomino_browser.next_board)
    elif board_to_get == "previous":
        grid = create_grid(pentomino_browser.previous_board)
    else:
        grid = create_grid(pentomino_browser.current_board)
    header = [PySimpleGUI.Text(f"Solution {pentomino_browser.current_status}")]
    buttons = []
    if pentomino_browser.has_previous_board():
        buttons.append(PySimpleGUI.Button("Previous"))
    if pentomino_browser.has_next_board():
        buttons.append(PySimpleGUI.Button("Next"))
    return [header, *grid, buttons]


def create_grid(grid):
    return [
        [
            PySimpleGUI.Canvas(
                background_color=pentomino_colors[grid[row][col]],
                size=(15, 15),
                border_width=1,
            )
            for col in range(len(grid[0]))
        ]
        for row in range(len(grid))
    ]
