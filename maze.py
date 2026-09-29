
import random


class Maze:
    def __init__(self, rows=10, cols=10):

        self.rows = rows
        self.cols = cols

        # Start and Goal
        self.start = (0, 0)
        self.goal = (rows - 1, cols - 1)

        # Maze cells
        self.grid = []

        # Cost/weight of every cell
        self.weights = []

        self.create_empty_maze()

    # ==========================================
    # CREATE EMPTY MAZE
    # ==========================================

    def create_empty_maze(self):

        self.grid = []
        self.weights = []

        for row in range(self.rows):

            current_row = []
            current_weights = []

            for col in range(self.cols):

                # "." = normal walkable cell
                current_row.append(".")

                # Every cell starts with weight 1
                current_weights.append(1)

            self.grid.append(current_row)
            self.weights.append(current_weights)

        # Start
        start_row, start_col = self.start

        self.grid[start_row][start_col] = "S"

        # Goal
        goal_row, goal_col = self.goal

        self.grid[goal_row][goal_col] = "G"

    # ==========================================
    # ADD WALL
    # ==========================================

    def add_wall(self, row, col):

        # Don't allow wall on Start
        if (row, col) == self.start:
            return

        # Don't allow wall on Goal
        if (row, col) == self.goal:
            return

        # Make cell a wall
        self.grid[row][col] = "#"

        # IMPORTANT:
        # We DON'T change the weight here.
        #
        # If this cell had weight 5,
        # it will still have weight 5 internally.
        #
        # If the wall is removed later,
        # the weight 5 will come back.

    # ==========================================
    # REMOVE WALL
    # ==========================================

    def remove_wall(self, row, col):

        if self.grid[row][col] == "#":

            self.grid[row][col] = "."

    # ==========================================
    # SET CELL WEIGHT
    # ==========================================

    def set_weight(self, row, col, weight):

        # Don't change Start
        if (row, col) == self.start:
            return

        # Don't change Goal
        if (row, col) == self.goal:
            return

        # Don't put weight on a wall
        if self.grid[row][col] == "#":
            return

        self.weights[row][col] = weight

    # ==========================================
    # GET CELL COST
    # ==========================================

    def get_cost(self, position):

        row, col = position

        return self.weights[row][col]

    # ==========================================
    # GET NEIGHBORS
    # ==========================================

    def get_neighbors(self, position):

        row, col = position

        directions = [
            (-1, 0),  # Up
            (1, 0),   # Down
            (0, -1),  # Left
            (0, 1)    # Right
        ]

        neighbors = []

        for row_change, col_change in directions:

            new_row = row + row_change
            new_col = col + col_change

            # Check boundary
            if (
                0 <= new_row < self.rows
                and
                0 <= new_col < self.cols
            ):

                # Don't go through walls
                if self.grid[new_row][new_col] != "#":

                    neighbors.append(
                        (new_row, new_col)
                    )

        return neighbors

    # ==========================================
    # DISPLAY MAZE
    # ==========================================

    def display(self):

        for row in self.grid:

            print(" ".join(row))
            
    def generate_random_maze(
        self,
        wall_probability=0.25
    ):
   

        weights = [1, 2, 5, 10]

        for row in range(self.rows):

            for col in range(self.cols):

                # ------------------------------
                # Keep Start and Goal
                # ------------------------------

                if (row, col) == self.start:

                    self.grid[row][col] = "S"
                    self.weights[row][col] = 1

                    continue

                if (row, col) == self.goal:

                    self.grid[row][col] = "G"
                    self.weights[row][col] = 1

                    continue

                # ------------------------------
                # Random Wall
                # ------------------------------

                if random.random() < wall_probability:

                    self.grid[row][col] = "#"

                    # Walls don't need a weight
                    self.weights[row][col] = 1

                else:

                    self.grid[row][col] = "."

                    # --------------------------
                    # Random Weight
                    # --------------------------

                    self.weights[row][col] = random.choice(
                        weights
                    )