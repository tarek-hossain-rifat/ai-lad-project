import time


def calculate_path_cost(maze, path):
    """
    Calculate the total cost of a path.

    The starting cell has cost 0.
    Every cell after the start contributes its weight.
    """

    if not path:
        return 0

    total_cost = 0

    for cell in path[1:]:
        total_cost += maze.get_cost(cell)

    return total_cost


def calculate_path_length(path):
    """
    Number of movements required to reach the goal.
    """

    if not path:
        return 0

    return len(path) - 1


def calculate_statistics(maze, algorithm_name, visited_order, path, start_time):
    """
    Generate statistics for the selected algorithm.
    """

    end_time = time.perf_counter()

    execution_time = (end_time - start_time) * 1000

    path_length = calculate_path_length(path)

    path_cost = calculate_path_cost(
        maze,
        path
    )

    statistics = {
        "algorithm": algorithm_name,
        "visited": len(visited_order),
        "path_length": path_length,
        "path_cost": path_cost,
        "execution_time": execution_time,
        "found": bool(path)
    }

    return statistics