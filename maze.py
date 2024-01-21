from cell import Cell
import random
import time


class Maze:
    """
    A class representing a maze.

    Attributes:
    - _cells (list): A 2D list of Cell objects representing the maze cells.
    - _x1 (float): The x-coordinate of the top-left corner of the maze.
    - _y1 (float): The y-coordinate of the top-left corner of the maze.
    - _num_rows (int): The number of rows in the maze.
    - _num_cols (int): The number of columns in the maze.
    - _cell_size_x (float): The width of each cell in the maze.
    - _cell_size_y (float): The height of each cell in the maze.
    - _window (Window): The Window object associated with the maze.

    Methods:
    - __init__(x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, window, seed=None): Initializes the Maze object.
    - _create_cells(): Creates the initial set of Cell objects for the maze.
    - _draw_cell(i, j): Draws a cell on the window at the specified coordinates.
    - _animate(): Performs animation by redrawing the window and adding a small delay.
    - _break_entrance_and_exit(): Breaks the entrance and exit walls of the maze.
    - _break_walls_r(i, j): Recursively breaks walls to generate the maze layout.
    - _reset_cells_visited(): Resets the 'visited' attribute of all cells in the maze.
    - _solve_r(i, j): Recursively solves the maze and animates the path.
    - solve(): Initiates the maze-solving process.

    Parameters:
    - x1 (float): The x-coordinate of the top-left corner of the maze.
    - y1 (float): The y-coordinate of the top-left corner of the maze.
    - num_rows (int): The number of rows in the maze.
    - num_cols (int): The number of columns in the maze.
    - cell_size_x (float): The width of each cell in the maze.
    - cell_size_y (float): The height of each cell in the maze.
    - window (Window): The Window object associated with the maze.
    - seed (int, optional): Seed for randomization. Default is None.
    """
    def __init__(self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, window, seed=None):
        """
        Initializes the Maze object.

        Args:
        - x1 (float): The x-coordinate of the top-left corner of the maze.
        - y1 (float): The y-coordinate of the top-left corner of the maze.
        - num_rows (int): The number of rows in the maze.
        - num_cols (int): The number of columns in the maze.
        - cell_size_x (float): The width of each cell in the maze.
        - cell_size_y (float): The height of each cell in the maze.
        - window (Window): The Window object associated with the maze.
        - seed (int, optional): Seed for randomization. Default is None.
        """
        self._cells = []
        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._window = window

        if seed:
            random.seed(seed)

        self._create_cells()
        self._break_entrance_and_exit()
        self._break_walls_r(0, 0)
        self._reset_cells_visited()


    def _create_cells(self):
        """
        Creates the initial set of Cell objects for the maze.
        """
        for i in range (self._num_cols):
            col_cells = []
            for j in range(self._num_rows):
                col_cells.append(Cell(self._window))
            self._cells.append(col_cells)
        for i in range(self._num_cols):
            for j in range(self._num_rows):
                self._draw_cell(i, j)


    def _draw_cell(self, i, j):
        """
        Draws a cell on the window at the specified coordinates.

        Args:
        - i (int): The column index of the cell.
        - j (int): The row index of the cell.
        """
        if self._window is None:
            return
        x1 = self._x1 + i * self._cell_size_x
        y1 = self._y1 + j * self._cell_size_y
        x2 = x1 + self._cell_size_x
        y2 = y1 + self._cell_size_y
        self._cells[i][j].draw(x1, y1, x2, y2)
        self._animate()


    def _animate(self):
        """
        Performs animation by redrawing the window and adding a small delay.
        """
        self._window.redraw()
        time.sleep(0.005)


    def _break_entrance_and_exit(self):
        """
        Breaks the entrance and exit walls of the maze.
        """
        self._cells[0][0].has_top_wall = False
        self._draw_cell(0, 0)
        self._cells[self._num_cols - 1][self._num_rows - 1].has_bottom_wall = False
        self._draw_cell(self._num_cols - 1, self._num_rows - 1)


    def _break_walls_r(self, i, j):
        """
        Recursively breaks walls to generate the maze layout.

        Args:
        - i (int): The column index of the current cell.
        - j (int): The row index of the current cell.
        """
        self._cells[i][j].visited = True

        while True:
            next_index_list = []

            if i > 0 and not self._cells[i-1][j].visited:
                next_index_list.append((i-1, j))
            if i < self._num_cols - 1 and not self._cells[i+1][j].visited:
                next_index_list.append((i+1, j))
            if j > 0 and not self._cells[i][j-1].visited:
                next_index_list.append((i, j-1))
            if j < self._num_rows - 1 and not self._cells[i][j+1].visited:
                next_index_list.append((i, j+1))

            if len(next_index_list) == 0:
                self._draw_cell(i, j)
                return
            
            direction_index = random.randrange(len(next_index_list))
            next_index = next_index_list[direction_index]

            if next_index[0] == i + 1:
                self._cells[i][j].has_right_wall = False
                self._cells[i+1][j].has_left_wall = False
            if next_index[0] == i - 1:
                self._cells[i][j].has_left_wall = False
                self._cells[i-1][j].has_right_wall = False
            if next_index[1] == j + 1:
                self._cells[i][j].has_bottom_wall = False
                self._cells[i][j+1].has_top_wall = False
            if next_index[1] == i - 1:
                self._cells[i][j].has_top_wall = False
                self._cells[i][j-1].has_bottom_wall = False

            self._break_walls_r(next_index[0], next_index[1])


    def _reset_cells_visited(self):
        """
        Resets the 'visited' attribute of all cells in the maze.
        """
        for col in self._cells:
            for cell in col:
                cell.visited = False


    def _solve_r(self, i, j):
        """
        Recursively solves the maze and animates the path.

        Args:
        - i (int): The column index of the current cell.
        - j (int): The row index of the current cell.

        Returns:
        - bool: True if the maze is solved, False otherwise.
        """
        self._animate()
        self._cells[i][j].visited = True

        if i == self._num_cols - 1 and j == self._num_rows - 1:
            return True
        
        if i > 0 and not self._cells[i][j].has_left_wall and not self._cells[i-1][j].visited:
            self._cells[i][j].draw_move(self._cells[i-1][j])
            if self._solve_r(i - 1, j):
                return True
            else:
                self._cells[i][j].draw_move(self._cells[i-1][j], True)
        
        if i < self._num_cols - 1 and not self._cells[i][j].has_right_wall and not self._cells[i+1][j].visited:
            self._cells[i][j].draw_move(self._cells[i+1][j])
            if self._solve_r(i + 1, j):
                return True
            else:
                self._cells[i][j].draw_move(self._cells[i+1][j], True)

        if j > 0 and not self._cells[i][j].has_top_wall and not self._cells[i][j-1].visited:
            self._cells[i][j].draw_move(self._cells[i][j-1])
            if self._solve_r(i, j-1):
                return True
            else:
                self._cells[i][j].draw_move(self._cells[i][j-1], True)

        if j < self._num_rows - 1 and not self._cells[i][j].has_bottom_wall and not self._cells[i][j+1].visited:
            self._cells[i][j].draw_move(self._cells[i][j+1])
            if self._solve_r(i, j+1):
                return True
            else:
                self._cells[i][j].draw_move(self._cells[i][j+1], True)

        return False


    def solve(self):
        """
        Initiates the maze-solving process.

        Returns:
        - bool: True if the maze is solved, False otherwise.
        """
        return self._solve_r(0, 0)