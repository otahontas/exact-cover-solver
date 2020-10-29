import numpy as np

answer = 0


def solve(table: np.array) -> None:
    if table.shape == (0, 0):
        global answer
        answer += 1
        return
    col_u = table.sum(axis=0).argmin()
    for row_u in np.where(table[:, col_u] == 1)[0]:
        r_col = set()
        r_row = set()
        for kol_s in np.where(table[row_u, :] == 1)[0]:
            r_col.add(kol_s)
            for riv_s in np.where(table[:, kol_s] == 1)[0]:
                r_row.add(riv_s)
        solve(np.delete(np.delete(table, list(r_row), 0), list(r_col), 1))


def main():
    wikipedia_example = np.array(
        [
            [1, 0, 0, 1, 0, 0, 1],
            [1, 0, 0, 1, 0, 0, 0],
            [0, 0, 0, 1, 1, 0, 1],
            [0, 0, 1, 0, 1, 1, 0],
            [0, 1, 1, 0, 0, 1, 1],
            [0, 1, 0, 0, 0, 0, 1],
        ]
    )
    solve(wikipedia_example)
    print(answer)


if __name__ == "__main__":
    main()
