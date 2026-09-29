import tkinter as tk
import time

from maze import Maze
from algorithms import (
    bfs,
    dfs,
    ucs,
    greedy,
    a_star,
    bidirectional_bfs
)
from statistics import calculate_statistics
from algorithm_comparison import compare_algorithms


class MazeGUI:

    def __init__(self, root):

        self.root = root

        self.root.title(
            "AI Maze Solver & Intelligent Pathfinding"
        )

        self.root.resizable(False, False)

        # ======================================
        # CREATE MAZE
        # ======================================

        self.maze = Maze(15, 15)

        # ======================================
        # CELL SIZE
        # ======================================

        self.cell_size = 35

        # ======================================
        # CANVAS SIZE
        # ======================================

        self.canvas_width = (
            self.maze.cols * self.cell_size
        )

        self.canvas_height = (
            self.maze.rows * self.cell_size
        )

        # ======================================
        # SEARCH STATUS
        # ======================================

        self.is_solving = False

        # ======================================
        # COMPARISON STATUS
        # ======================================

        self.is_comparing = False

        # ======================================
        # SELECTED ALGORITHM
        # ======================================

        self.selected_algorithm = tk.StringVar()

        self.selected_algorithm.set("BFS")

        # ======================================
        # STATISTICS
        # ======================================

        self.last_statistics = None

        # ======================================
        # CREATE GUI
        # ======================================

        self.create_widgets()

        # ======================================
        # DRAW MAZE
        # ======================================

        self.draw_maze()

    # ==========================================
    # CREATE GUI WIDGETS
    # ==========================================

    def create_widgets(self):

        # --------------------------------------
        # TITLE
        # --------------------------------------

        self.title_label = tk.Label(
            self.root,
            text="AI Maze Solver & Intelligent Pathfinding",
            font=("Arial", 20, "bold")
        )

        self.title_label.pack(
            pady=10
        )

        # --------------------------------------
        # MAIN CONTENT FRAME
        # --------------------------------------

        self.main_frame = tk.Frame(
            self.root
        )

        self.main_frame.pack(
            padx=10,
            pady=5
        )

        # ======================================
        # LEFT SIDE - MAZE
        # ======================================

        self.maze_frame = tk.Frame(
            self.main_frame
        )

        self.maze_frame.pack(
            side=tk.LEFT
        )

        # --------------------------------------
        # ALGORITHM SELECTION
        # --------------------------------------

        self.algorithm_frame = tk.Frame(
            self.maze_frame
        )

        self.algorithm_frame.pack(
            pady=5
        )

        self.algorithm_label = tk.Label(
            self.algorithm_frame,
            text="Algorithm:",
            font=("Arial", 11)
        )

        self.algorithm_label.pack(
            side=tk.LEFT,
            padx=5
        )

        self.algorithm_menu = tk.OptionMenu(
            self.algorithm_frame,
            self.selected_algorithm,
            "BFS",
            "DFS",
            "UCS",
            "Greedy Best-First",
            "A*",
            "Bidirectional BFS"
        )

        self.algorithm_menu.config(
            width=15
        )

        self.algorithm_menu.pack(
            side=tk.LEFT,
            padx=5
        )

        # --------------------------------------
        # MAZE CANVAS
        # --------------------------------------

        self.canvas = tk.Canvas(
            self.maze_frame,
            width=self.canvas_width,
            height=self.canvas_height,
            bg="white"
        )

        self.canvas.pack(
            padx=5,
            pady=10
        )

        # --------------------------------------
        # LEFT CLICK
        # --------------------------------------

        self.canvas.bind(
            "<Button-1>",
            self.handle_click
        )

        # --------------------------------------
        # RIGHT CLICK
        # --------------------------------------

        self.canvas.bind(
            "<Button-3>",
            self.handle_weight_click
        )

        # ======================================
        # RIGHT SIDE - CONTROL PANEL
        # ======================================

        self.control_frame = tk.Frame(
            self.main_frame,
            width=220
        )

        self.control_frame.pack(
            side=tk.RIGHT,
            fill=tk.Y,
            padx=(15, 5)
        )

        # --------------------------------------
        # CONTROL TITLE
        # --------------------------------------

        self.control_title = tk.Label(
            self.control_frame,
            text="Controls",
            font=("Arial", 15, "bold")
        )

        self.control_title.pack(
            pady=(5, 10)
        )

        # --------------------------------------
        # SOLVE BUTTON
        # --------------------------------------

        self.solve_button = tk.Button(
            self.control_frame,
            text="Solve",
            command=self.solve,
            width=18,
            font=("Arial", 10, "bold")
        )

        self.solve_button.pack(
            pady=4
        )

        # --------------------------------------
        # COMPARE BUTTON
        # --------------------------------------

        self.compare_button = tk.Button(
            self.control_frame,
            text="Compare All",
            command=self.compare_all,
            width=18,
            font=("Arial", 10, "bold")
        )

        self.compare_button.pack(
            pady=4
        )

        # --------------------------------------
        # RESET BUTTON
        # --------------------------------------

        self.reset_button = tk.Button(
            self.control_frame,
            text="Reset Maze",
            command=self.reset_maze,
            width=18
        )

        self.reset_button.pack(
            pady=4
        )

        # --------------------------------------
        # RANDOM MAZE BUTTON
        # --------------------------------------

        self.random_button = tk.Button(
            self.control_frame,
            text="Random Maze",
            command=self.generate_random_maze,
            width=18
        )

        self.random_button.pack(
            pady=4
        )

        # ======================================
        # STATISTICS SECTION
        # ======================================

        self.statistics_frame = tk.LabelFrame(
            self.control_frame,
            text="Statistics",
            font=("Arial", 11, "bold"),
            padx=10,
            pady=10
        )

        self.statistics_frame.pack(
            fill=tk.X,
            pady=(20, 5)
        )

        self.stats_algorithm = tk.Label(
            self.statistics_frame,
            text="Algorithm: --",
            anchor="w",
            font=("Arial", 10)
        )

        self.stats_algorithm.pack(
            fill=tk.X,
            pady=2
        )

        self.stats_status = tk.Label(
            self.statistics_frame,
            text="Status: Ready",
            anchor="w",
            font=("Arial", 10)
        )

        self.stats_status.pack(
            fill=tk.X,
            pady=2
        )

        self.stats_visited = tk.Label(
            self.statistics_frame,
            text="Visited Nodes: --",
            anchor="w",
            font=("Arial", 10)
        )

        self.stats_visited.pack(
            fill=tk.X,
            pady=2
        )

        self.stats_path_length = tk.Label(
            self.statistics_frame,
            text="Path Length: --",
            anchor="w",
            font=("Arial", 10)
        )

        self.stats_path_length.pack(
            fill=tk.X,
            pady=2
        )

        self.stats_path_cost = tk.Label(
            self.statistics_frame,
            text="Path Cost: --",
            anchor="w",
            font=("Arial", 10)
        )

        self.stats_path_cost.pack(
            fill=tk.X,
            pady=2
        )

        self.stats_time = tk.Label(
            self.statistics_frame,
            text="Execution Time: --",
            anchor="w",
            font=("Arial", 10)
        )

        self.stats_time.pack(
            fill=tk.X,
            pady=2
        )

        # ======================================
        # LEGEND
        # ======================================

        self.legend_frame = tk.LabelFrame(
            self.control_frame,
            text="Legend",
            font=("Arial", 11, "bold"),
            padx=10,
            pady=8
        )

        self.legend_frame.pack(
            fill=tk.X,
            pady=(15, 5)
        )

        self.create_legend_item(
            "green",
            "Start"
        )

        self.create_legend_item(
            "red",
            "Goal"
        )

        self.create_legend_item(
            "black",
            "Wall"
        )

        self.create_legend_item(
            "lightblue",
            "Visited"
        )

        self.create_legend_item(
            "yellow",
            "Final Path"
        )

        # --------------------------------------
        # WEIGHT INFORMATION
        # --------------------------------------

        self.weight_label = tk.Label(
            self.control_frame,
            text=(
                "Right Click:\n"
                "1 → 2 → 5 → 10 → 1"
            ),
            font=("Arial", 9),
            justify=tk.LEFT
        )

        self.weight_label.pack(
            pady=10
        )

    # ==========================================
    # CREATE LEGEND ITEM
    # ==========================================

    def create_legend_item(
        self,
        color,
        text
    ):

        frame = tk.Frame(
            self.legend_frame
        )

        frame.pack(
            fill=tk.X,
            pady=2
        )

        color_box = tk.Label(
            frame,
            bg=color,
            width=2,
            height=1,
            relief=tk.SOLID,
            borderwidth=1
        )

        color_box.pack(
            side=tk.LEFT,
            padx=(0, 8)
        )

        label = tk.Label(
            frame,
            text=text,
            anchor="w"
        )

        label.pack(
            side=tk.LEFT
        )

    # ==========================================
    # DRAW COMPLETE MAZE
    # ==========================================

    def draw_maze(self):

        self.canvas.delete("all")

        for row in range(self.maze.rows):

            for col in range(self.maze.cols):

                x1 = col * self.cell_size
                y1 = row * self.cell_size

                x2 = x1 + self.cell_size
                y2 = y1 + self.cell_size

                cell = self.maze.grid[row][col]

                if cell == "S":

                    fill = "green"

                elif cell == "G":

                    fill = "red"

                elif cell == "#":

                    fill = "black"

                else:

                    fill = "white"

                    weight = self.maze.weights[row][col]

                    if weight == 2:

                        fill = "lightyellow"

                    elif weight == 5:

                        fill = "orange"

                    elif weight == 10:

                        fill = "pink"

                self.canvas.create_rectangle(
                    x1,
                    y1,
                    x2,
                    y2,
                    fill=fill,
                    outline="gray"
                )

                if (
                    cell != "#"
                    and cell != "S"
                    and cell != "G"
                ):

                    weight = self.maze.weights[row][col]

                    if weight > 1:

                        self.canvas.create_text(
                            x1 + self.cell_size // 2,
                            y1 + self.cell_size // 2,
                            text=str(weight),
                            font=("Arial", 10, "bold")
                        )

    # ==========================================
    # LEFT CLICK
    # ==========================================

    def handle_click(self, event):

        if self.is_solving or self.is_comparing:
            return

        col = event.x // self.cell_size
        row = event.y // self.cell_size

        if row < 0 or row >= self.maze.rows:
            return

        if col < 0 or col >= self.maze.cols:
            return

        if (row, col) == self.maze.start:
            return

        if (row, col) == self.maze.goal:
            return

        if self.maze.grid[row][col] == "#":

            self.maze.remove_wall(
                row,
                col
            )

        else:

            self.maze.add_wall(
                row,
                col
            )

        self.draw_maze()

    # ==========================================
    # RIGHT CLICK
    # ==========================================

    def handle_weight_click(self, event):

        if self.is_solving or self.is_comparing:
            return

        col = event.x // self.cell_size
        row = event.y // self.cell_size

        if row < 0 or row >= self.maze.rows:
            return

        if col < 0 or col >= self.maze.cols:
            return

        if (row, col) == self.maze.start:
            return

        if (row, col) == self.maze.goal:
            return

        if self.maze.grid[row][col] == "#":
            return

        weights = [1, 2, 5, 10]

        current_weight = (
            self.maze.weights[row][col]
        )

        current_index = weights.index(
            current_weight
        )

        next_index = (
            current_index + 1
        ) % len(weights)

        next_weight = weights[next_index]

        self.maze.set_weight(
            row,
            col,
            next_weight
        )

        self.draw_maze()

    # ==========================================
    # RESET MAZE
    # ==========================================

    def reset_maze(self):

        if self.is_solving or self.is_comparing:
            return

        self.maze = Maze(15, 15)

        self.clear_statistics()

        self.draw_maze()

    # ==========================================
    # GENERATE RANDOM MAZE
    # ==========================================

    def generate_random_maze(self):

        if self.is_solving or self.is_comparing:
            return

        # --------------------------------------
        # CREATE NEW MAZE
        # --------------------------------------

        self.maze = Maze(15, 15)

        # --------------------------------------
        # GENERATE RANDOM MAZE
        # --------------------------------------

        self.maze.generate_random_maze(
            wall_probability=0.25
        )

        # --------------------------------------
        # CLEAR OLD STATISTICS
        # --------------------------------------

        self.clear_statistics()

        # --------------------------------------
        # DRAW NEW MAZE
        # --------------------------------------

        self.draw_maze()

    # ==========================================
    # CLEAR STATISTICS
    # ==========================================

    def clear_statistics(self):

        self.stats_algorithm.config(
            text="Algorithm: --"
        )

        self.stats_status.config(
            text="Status: Ready"
        )

        self.stats_visited.config(
            text="Visited Nodes: --"
        )

        self.stats_path_length.config(
            text="Path Length: --"
        )

        self.stats_path_cost.config(
            text="Path Cost: --"
        )

        self.stats_time.config(
            text="Execution Time: --"
        )

        self.last_statistics = None

    # ==========================================
    # UPDATE STATISTICS
    # ==========================================

    def update_statistics(
        self,
        statistics
    ):

        self.last_statistics = statistics

        self.stats_algorithm.config(
            text=(
                f"Algorithm: "
                f"{statistics['algorithm']}"
            )
        )

        if statistics["found"]:

            self.stats_status.config(
                text="Status: Path Found"
            )

        else:

            self.stats_status.config(
                text="Status: No Path Found"
            )

        self.stats_visited.config(
            text=(
                f"Visited Nodes: "
                f"{statistics['visited']}"
            )
        )

        self.stats_path_length.config(
            text=(
                f"Path Length: "
                f"{statistics['path_length']}"
            )
        )

        self.stats_path_cost.config(
            text=(
                f"Path Cost: "
                f"{statistics['path_cost']}"
            )
        )

        self.stats_time.config(
            text=(
                f"Execution Time: "
                f"{statistics['execution_time']:.3f} ms"
            )
        )

    # ==========================================
    # DISABLE CONTROLS
    # ==========================================

    def disable_controls(self):

        self.solve_button.config(
            state=tk.DISABLED
        )

        self.compare_button.config(
            state=tk.DISABLED
        )

        self.reset_button.config(
            state=tk.DISABLED
        )

        self.random_button.config(
            state=tk.DISABLED
        )

    # ==========================================
    # ENABLE CONTROLS
    # ==========================================

    def enable_controls(self):

        self.solve_button.config(
            state=tk.NORMAL
        )

        self.compare_button.config(
            state=tk.NORMAL
        )

        self.reset_button.config(
            state=tk.NORMAL
        )

        self.random_button.config(
            state=tk.NORMAL
        )

    # ==========================================
    # SOLVE
    # ==========================================

    def solve(self):

        if self.is_solving or self.is_comparing:
            return

        self.is_solving = True

        self.disable_controls()

        algorithm = (
            self.selected_algorithm.get()
        )

        start_time = time.perf_counter()

        # --------------------------------------
        # BFS
        # --------------------------------------

        if algorithm == "BFS":

            visited_order, path = bfs(
                self.maze
            )

        # --------------------------------------
        # DFS
        # --------------------------------------

        elif algorithm == "DFS":

            visited_order, path = dfs(
                self.maze
            )

        # --------------------------------------
        # UCS
        # --------------------------------------

        elif algorithm == "UCS":

            visited_order, path = ucs(
                self.maze
            )

        # --------------------------------------
        # GREEDY
        # --------------------------------------

        elif algorithm == "Greedy Best-First":

            visited_order, path = greedy(
                self.maze
            )

        # --------------------------------------
        # A*
        # --------------------------------------

        elif algorithm == "A*":

            visited_order, path = a_star(
                self.maze
            )

        # --------------------------------------
        # BIDIRECTIONAL BFS
        # --------------------------------------

        elif algorithm == "Bidirectional BFS":

            visited_order, path = bidirectional_bfs(
                self.maze
            )

        # --------------------------------------
        # FALLBACK
        # --------------------------------------

        else:

            visited_order = []

            path = []

        # --------------------------------------
        # CALCULATE STATISTICS
        # --------------------------------------

        statistics = calculate_statistics(
            self.maze,
            algorithm,
            visited_order,
            path,
            start_time
        )

        self.update_statistics(
            statistics
        )

        # --------------------------------------
        # ANIMATE
        # --------------------------------------

        self.animate_visited(
            visited_order,
            path,
            0
        )

    # ==========================================
    # COMPARE ALL ALGORITHMS
    # ==========================================

    def compare_all(self):

        if self.is_solving or self.is_comparing:
            return

        self.is_comparing = True

        # --------------------------------------
        # DISABLE CONTROLS
        # --------------------------------------

        self.disable_controls()

        # --------------------------------------
        # RUN COMPARISON
        # --------------------------------------

        results = compare_algorithms(
            self.maze
        )

        # --------------------------------------
        # SHOW RESULTS
        # --------------------------------------

        self.show_comparison_window(
            results
        )

        # --------------------------------------
        # ENABLE CONTROLS
        # --------------------------------------

        self.is_comparing = False

        self.enable_controls()

    # ==========================================
    # COMPARISON WINDOW
    # ==========================================

    def show_comparison_window(
        self,
        results
    ):

        comparison_window = tk.Toplevel(
            self.root
        )

        comparison_window.title(
            "Algorithm Comparison"
        )

        comparison_window.resizable(
            False,
            False
        )

        # --------------------------------------
        # TITLE
        # --------------------------------------

        title = tk.Label(
            comparison_window,
            text="Algorithm Comparison",
            font=("Arial", 16, "bold")
        )

        title.pack(
            pady=(15, 5)
        )

        # --------------------------------------
        # SUBTITLE
        # --------------------------------------

        subtitle = tk.Label(
            comparison_window,
            text=(
                "All algorithms were tested "
                "on the same maze and weights."
            ),
            font=("Arial", 9)
        )

        subtitle.pack(
            pady=(0, 10)
        )

        # --------------------------------------
        # TABLE
        # --------------------------------------

        table = tk.Frame(
            comparison_window,
            padx=15,
            pady=10
        )

        table.pack()

        headers = [
            "Algorithm",
            "Visited",
            "Path Length",
            "Cost",
            "Time (ms)"
        ]

        # --------------------------------------
        # TABLE HEADERS
        # --------------------------------------

        for column, header in enumerate(headers):

            label = tk.Label(
                table,
                text=header,
                font=("Arial", 10, "bold"),
                borderwidth=1,
                relief="solid",
                padx=8,
                pady=6
            )

            label.grid(
                row=0,
                column=column,
                sticky="nsew"
            )

        # --------------------------------------
        # TABLE DATA
        # --------------------------------------

        for row, result in enumerate(
            results,
            start=1
        ):

            values = [
                result["algorithm"],
                result["visited"],
                result["path_length"],
                result["path_cost"],
                f"{result['execution_time']:.3f}"
            ]

            for column, value in enumerate(values):

                label = tk.Label(
                    table,
                    text=str(value),
                    font=("Arial", 10),
                    borderwidth=1,
                    relief="solid",
                    padx=8,
                    pady=6
                )

                label.grid(
                    row=row,
                    column=column,
                    sticky="nsew"
                )

        # --------------------------------------
        # CLOSE BUTTON
        # --------------------------------------

        close_button = tk.Button(
            comparison_window,
            text="Close",
            width=15,
            command=comparison_window.destroy
        )

        close_button.pack(
            pady=(5, 15)
        )

    # ==========================================
    # ANIMATE VISITED CELLS
    # ==========================================

    def animate_visited(
        self,
        visited_order,
        path,
        index
    ):

        if index >= len(visited_order):

            self.animate_path(
                path,
                0
            )

            return

        row, col = (
            visited_order[index]
        )

        if (
            (row, col) != self.maze.start
            and
            (row, col) != self.maze.goal
        ):

            self.draw_cell(
                row,
                col,
                "lightblue"
            )

        self.root.after(
            40,
            lambda: self.animate_visited(
                visited_order,
                path,
                index + 1
            )
        )

    # ==========================================
    # ANIMATE FINAL PATH
    # ==========================================

    def animate_path(
        self,
        path,
        index
    ):

        if index >= len(path):

            self.is_solving = False

            self.enable_controls()

            return

        row, col = path[index]

        if (
            (row, col) != self.maze.start
            and
            (row, col) != self.maze.goal
        ):

            self.draw_cell(
                row,
                col,
                "yellow"
            )

        self.root.after(
            80,
            lambda: self.animate_path(
                path,
                index + 1
            )
        )

    # ==========================================
    # DRAW ONE CELL WITHOUT LOSING WEIGHT
    # ==========================================

    def draw_cell(
        self,
        row,
        col,
        color
    ):

        x1 = col * self.cell_size
        y1 = row * self.cell_size

        x2 = x1 + self.cell_size
        y2 = y1 + self.cell_size

        self.canvas.create_rectangle(
            x1,
            y1,
            x2,
            y2,
            fill=color,
            outline="gray"
        )

        # --------------------------------------
        # KEEP WEIGHT VISIBLE
        # --------------------------------------

        weight = self.maze.weights[row][col]

        if weight > 1:

            self.canvas.create_text(
                x1 + self.cell_size // 2,
                y1 + self.cell_size // 2,
                text=str(weight),
                font=("Arial", 10, "bold")
            )