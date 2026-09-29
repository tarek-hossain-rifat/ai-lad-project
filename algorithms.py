from collections import deque
import heapq


# ==========================================
# BFS
# ==========================================

def bfs(maze):

    queue = deque([maze.start])

    visited = {maze.start}

    parent = {
        maze.start: None
    }

    visited_order = []

    while queue:

        current = queue.popleft()

        visited_order.append(current)

        if current == maze.goal:
            break

        for neighbor in maze.get_neighbors(current):

            if neighbor in visited:
                continue

            visited.add(neighbor)

            parent[neighbor] = current

            queue.append(neighbor)

    path = build_path(
        parent,
        maze.goal
    )

    return visited_order, path


# ==========================================
# DFS
# ==========================================

def dfs(maze):

    stack = [maze.start]

    visited = {maze.start}

    parent = {
        maze.start: None
    }

    visited_order = []

    while stack:

        current = stack.pop()

        visited_order.append(current)

        if current == maze.goal:
            break

        for neighbor in maze.get_neighbors(current):

            if neighbor in visited:
                continue

            visited.add(neighbor)

            parent[neighbor] = current

            stack.append(neighbor)

    path = build_path(
        parent,
        maze.goal
    )

    return visited_order, path


# ==========================================
# UCS
# ==========================================

def ucs(maze):

    priority_queue = []

    heapq.heappush(
        priority_queue,
        (0, maze.start)
    )

    cost_so_far = {
        maze.start: 0
    }

    parent = {
        maze.start: None
    }

    visited = set()

    visited_order = []

    while priority_queue:

        current_cost, current = heapq.heappop(
            priority_queue
        )

        if current in visited:
            continue

        visited.add(current)

        visited_order.append(current)

        if current == maze.goal:
            break

        for neighbor in maze.get_neighbors(current):

            new_cost = (
                current_cost
                + maze.get_cost(neighbor)
            )

            if (
                neighbor not in cost_so_far
                or new_cost < cost_so_far[neighbor]
            ):

                cost_so_far[neighbor] = new_cost

                parent[neighbor] = current

                heapq.heappush(
                    priority_queue,
                    (
                        new_cost,
                        neighbor
                    )
                )

    path = build_path(
        parent,
        maze.goal
    )

    return visited_order, path


# ==========================================
# MANHATTAN DISTANCE
# ==========================================

def manhattan_distance(
    current,
    goal
):

    return (
        abs(current[0] - goal[0])
        + abs(current[1] - goal[1])
    )


# ==========================================
# GREEDY BEST-FIRST SEARCH
# ==========================================

def greedy(maze):

    priority_queue = []

    heapq.heappush(
        priority_queue,
        (
            manhattan_distance(
                maze.start,
                maze.goal
            ),
            maze.start
        )
    )

    visited = set()

    parent = {
        maze.start: None
    }

    visited_order = []

    while priority_queue:

        _, current = heapq.heappop(
            priority_queue
        )

        if current in visited:
            continue

        visited.add(current)

        visited_order.append(current)

        if current == maze.goal:
            break

        for neighbor in maze.get_neighbors(current):

            if neighbor in visited:
                continue

            if neighbor not in parent:

                parent[neighbor] = current

            priority = manhattan_distance(
                neighbor,
                maze.goal
            )

            heapq.heappush(
                priority_queue,
                (
                    priority,
                    neighbor
                )
            )

    path = build_path(
        parent,
        maze.goal
    )

    return visited_order, path


# ==========================================
# A*
# ==========================================

def a_star(maze):

    priority_queue = []

    heapq.heappush(
        priority_queue,
        (
            0,
            0,
            maze.start
        )
    )

    g_cost = {
        maze.start: 0
    }

    parent = {
        maze.start: None
    }

    visited = set()

    visited_order = []

    while priority_queue:

        _, current_g, current = heapq.heappop(
            priority_queue
        )

        if current in visited:
            continue

        visited.add(current)

        visited_order.append(current)

        if current == maze.goal:
            break

        for neighbor in maze.get_neighbors(current):

            new_g_cost = (
                current_g
                + maze.get_cost(neighbor)
            )

            if (
                neighbor not in g_cost
                or new_g_cost < g_cost[neighbor]
            ):

                g_cost[neighbor] = new_g_cost

                parent[neighbor] = current

                h_cost = manhattan_distance(
                    neighbor,
                    maze.goal
                )

                f_cost = (
                    new_g_cost
                    + h_cost
                )

                heapq.heappush(
                    priority_queue,
                    (
                        f_cost,
                        new_g_cost,
                        neighbor
                    )
                )

    path = build_path(
        parent,
        maze.goal
    )

    return visited_order, path


# ==========================================
# BIDIRECTIONAL BFS
# ==========================================

def bidirectional_bfs(maze):

    start = maze.start
    goal = maze.goal

    # --------------------------------------
    # SPECIAL CASE
    # --------------------------------------

    if start == goal:

        return [start], [start]

    # --------------------------------------
    # FRONTIER FROM START
    # --------------------------------------

    start_queue = deque([start])

    start_parent = {
        start: None
    }

    start_visited = {
        start
    }

    # --------------------------------------
    # FRONTIER FROM GOAL
    # --------------------------------------

    goal_queue = deque([goal])

    goal_parent = {
        goal: None
    }

    goal_visited = {
        goal
    }

    # --------------------------------------
    # VISITED ORDER
    # --------------------------------------

    visited_order = []

    meeting_node = None

    # ======================================
    # SEARCH
    # ======================================

    while start_queue and goal_queue:

        # ----------------------------------
        # EXPAND FROM START
        # ----------------------------------

        level_size = len(start_queue)

        for _ in range(level_size):

            current = start_queue.popleft()

            if current not in visited_order:

                visited_order.append(current)

            for neighbor in maze.get_neighbors(
                current
            ):

                if neighbor in start_visited:
                    continue

                start_visited.add(
                    neighbor
                )

                start_parent[neighbor] = current

                # --------------------------
                # FRONTIERS MEET
                # --------------------------

                if neighbor in goal_visited:

                    meeting_node = neighbor

                    break

                start_queue.append(
                    neighbor
                )

            if meeting_node is not None:
                break

        if meeting_node is not None:
            break

        # ----------------------------------
        # EXPAND FROM GOAL
        # ----------------------------------

        level_size = len(goal_queue)

        for _ in range(level_size):

            current = goal_queue.popleft()

            if current not in visited_order:

                visited_order.append(current)

            for neighbor in maze.get_neighbors(
                current
            ):

                if neighbor in goal_visited:
                    continue

                goal_visited.add(
                    neighbor
                )

                goal_parent[neighbor] = current

                # --------------------------
                # FRONTIERS MEET
                # --------------------------

                if neighbor in start_visited:

                    meeting_node = neighbor

                    break

                goal_queue.append(
                    neighbor
                )

            if meeting_node is not None:
                break

        if meeting_node is not None:
            break

    # ======================================
    # NO PATH
    # ======================================

    if meeting_node is None:

        return visited_order, []

    # ======================================
    # BUILD START -> MEETING PATH
    # ======================================

    path_from_start = []

    current = meeting_node

    while current is not None:

        path_from_start.append(
            current
        )

        current = start_parent.get(
            current
        )

    path_from_start.reverse()

    # ======================================
    # BUILD MEETING -> GOAL PATH
    # ======================================

    path_to_goal = []

    current = goal_parent.get(
        meeting_node
    )

    while current is not None:

        path_to_goal.append(
            current
        )

        current = goal_parent.get(
            current
        )

    # ======================================
    # COMPLETE PATH
    # ======================================

    path = (
        path_from_start
        + path_to_goal
    )

    return visited_order, path


# ==========================================
# BUILD PATH
# ==========================================

def build_path(
    parent,
    goal
):

    if goal not in parent:

        return []

    path = []

    current = goal

    while current is not None:

        path.append(current)

        current = parent[current]

    path.reverse()

    return path