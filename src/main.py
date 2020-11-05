from services.solver import Solver


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
    solver.solve(universe, set_collection)


if __name__ == "__main__":
    main()
