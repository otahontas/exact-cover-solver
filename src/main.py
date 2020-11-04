import time
from services.solver import Solver

# answer = 0
#
#
# def solve(table: np.array) -> None:
#     if table.shape == (0, 0):
#         global answer
#         answer += 1
#         return
#     col_u = table.sum(axis=0).argmin()
#     for row_u in np.where(table[:, col_u] == 1)[0]:
#         r_col = set()
#         r_row = set()
#         for kol_s in np.where(table[row_u, :] == 1)[0]:
#             r_col.add(kol_s)
#             for riv_s in np.where(table[:, kol_s] == 1)[0]:
#                 r_row.add(riv_s)
#         solve(np.delete(np.delete(table, list(r_row), 0), list(r_col), 1))


def main():

    set_collection = [
        ("A", [1, 4, 7]),
        ("B", [1, 4]),
        ("C", [4, 5, 7]),
        ("D", [3, 5, 6]),
        ("E", [2, 3, 6, 7]),
        ("F", [2, 7]),
    ]

    universe = [i for i in range(1, 8)]

    solver = Solver()

    root = solver.solve(universe, set_collection)

    # Create columns

    node = root.right
    while node != root:
        print("=== col", node.id, "===")
        cell = node.down
        while cell != node:
            print(cell)
            cell = cell.down
        node = node.right


if __name__ == "__main__":
    main()
