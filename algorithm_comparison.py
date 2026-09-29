import time

from algorithms import (
    bfs,
    dfs,
    ucs,
    greedy,
    a_star,
    bidirectional_bfs
)


def compare_algorithms(maze):

    algorithms = [
        ("BFS", bfs),
        ("DFS", dfs),
        ("UCS", ucs),
        ("Greedy Best-First", greedy),
        ("A*", a_star),
        ("Bidirectional BFS", bidirectional_bfs)
    ]

    results = []

    for name, algorithm in algorithms:

        start_time = time.perf_counter()

        visited_order, path = algorithm(
            maze
        )

        end_time = time.perf_counter()

        execution_time = (
            end_time - start_time
        ) * 1000

        # ----------------------------------
        # PATH LENGTH
        # ----------------------------------

        if path:

            path_length = len(path) - 1

        else:

            path_length = 0

        # ----------------------------------
        # PATH COST
        # ----------------------------------

        path_cost = 0

        if path:

            for cell in path[1:]:

                path_cost += maze.get_cost(
                    cell
                )

        # ----------------------------------
        # RESULT
        # ----------------------------------

        result = {
            "algorithm": name,
            "visited": len(visited_order),
            "path_length": path_length,
            "path_cost": path_cost,
            "execution_time": execution_time,
            "found": bool(path)
        }

        results.append(
            result
        )

    return results