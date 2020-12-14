from fastapi import FastAPI
from pydantic import BaseModel
from exact_cover_solver import Solver
from typing import List
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

solver = Solver()


class PentominoBody(BaseModel):
    """Pentomino input model for validation."""
    height: int
    width: int
    algorithm: str


class SudokuBody(BaseModel):
    """Sudoku input model for validation."""
    sudoku_board: List[List[int]]
    algorithm: str


@app.post("/solve/pentomino")
async def solve_pentomino(pentomino_input: PentominoBody):
    """Get boards from solver, return them."""
    boards = solver.solve_pentomino_problem(
        pentomino_input.algorithm,
        pentomino_input.height,
        pentomino_input.width
    )
    return {"boards": boards}


@app.post("/solve/sudoku")
async def solve_sudoku(sudoku_input: SudokuBody):
    """Get boards from solver, return them."""
    boards = solver.solve_sudoku_problem(
        sudoku_input.algorithm,
        sudoku_input.sudoku_board
    )
    return {"boards": boards}
