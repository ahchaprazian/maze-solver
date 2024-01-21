from graphics import Line, Point


class Cell:
    """
    A class representing a cell in a maze.

    Attributes:
    - has_left_wall (bool): Indicates if the cell has a left wall.
    - has_right_wall (bool): Indicates if the cell has a right wall.
    - has_top_wall (bool): Indicates if the cell has a top wall.
    - has_bottom_wall (bool): Indicates if the cell has a bottom wall.
    - visited (bool): Indicates if the cell has been visited.
    - _x1 (float): The x-coordinate of the top-left corner of the cell.
    - _x2 (float): The x-coordinate of the bottom-right corner of the cell.
    - _y1 (float): The y-coordinate of the top-left corner of the cell.
    - _y2 (float): The y-coordinate of the bottom-right corner of the cell.
    - _win: The Window object associated with the cell.

    Methods:
    - draw(x1, y1, x2, y2): Draws the cell on the window with specified coordinates.
    - draw_move(to_cell, undo=False): Draws the movement of the cell to another cell.

    Parameters:
    - win: The Window object to draw on.
    """
    def __init__(self, win=None):
        """
        Initializes the Cell object.

        Args:
        - win (Window): The Window object to draw on.
        """
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self.visited = False
        self._x1 = None
        self._x2 = None
        self._y1 = None
        self._y2 = None
        self._win = win


    def draw(self, x1, y1, x2, y2):
        """
        Draws the cell on the window with specified coordinates.

        Args:
        - x1 (float): The x-coordinate of the top-left corner of the cell.
        - y1 (float): The y-coordinate of the top-left corner of the cell.
        - x2 (float): The x-coordinate of the bottom-right corner of the cell.
        - y2 (float): The y-coordinate of the bottom-right corner of the cell.
        """
        if self._win is None:
            return
        self._x1 = x1
        self._x2 = x2
        self._y1 = y1
        self._y2 = y2
        if self.has_left_wall:
            line = Line(Point(x1, y1), Point(x1, y2))
            self._win.draw_line(line)
        else:
            line = Line(Point(x1, y1), Point(x1, y2))
            self._win.draw_line(line, "white")
        if self.has_top_wall:
            line = Line(Point(x1, y1), Point(x2, y1))
            self._win.draw_line(line)
        else:
            line = Line(Point(x1, y1), Point(x2, y1))
            self._win.draw_line(line, "white")
        if self.has_right_wall:
            line = Line(Point(x2, y1), Point(x2, y2))
            self._win.draw_line(line)
        else:
            line = Line(Point(x2, y1), Point(x2, y2))
            self._win.draw_line(line, "white")
        if self.has_bottom_wall:
            line = Line(Point(x1, y2), Point(x2, y2))
            self._win.draw_line(line)
        else:
            line = Line(Point(x1, y2), Point(x2, y2))
            self._win.draw_line(line, "white")


    def draw_move(self, to_cell, undo=False):
        """
        Draws the movement of the cell to another cell.

        Args:
        - to_cell (Cell): The target cell to move to.
        - undo (bool): If True, the movement is drawn in gray (undo mode). Default is False.
        """
        if self._win is None:
            return
        x_mid = (self._x1 + self._x2) / 2
        y_mid = (self._y1 + self._y2) / 2

        to_x_mid = (to_cell._x1 + to_cell._x2) / 2
        to_y_mid = (to_cell._y1 + to_cell._y2) / 2

        fill_color = "red"
        if undo:
            fill_color = "gray"

        # moving left
        if self._x1 > to_cell._x1:
            line = Line(Point(self._x1, y_mid), Point(x_mid, y_mid))
            self._win.draw_line(line, fill_color)
            line = Line(Point(to_x_mid, to_y_mid), Point(to_cell._x2, to_y_mid))
            self._win.draw_line(line, fill_color)

        # moving right
        elif self._x1 < to_cell._x1:
            line = Line(Point(x_mid, y_mid), Point(self._x2, y_mid))
            self._win.draw_line(line, fill_color)
            line = Line(Point(to_cell._x1, to_y_mid), Point(to_x_mid, to_y_mid))
            self._win.draw_line(line, fill_color)

        # moving up
        elif self._y1 > to_cell._y1:
            line = Line(Point(x_mid, y_mid), Point(x_mid, self._y1))
            self._win.draw_line(line, fill_color)
            line = Line(Point(to_x_mid, to_cell._y2), Point(to_x_mid, to_y_mid))
            self._win.draw_line(line, fill_color)

        # moving down
        elif self._y1 < to_cell._y1:
            line = Line(Point(x_mid, y_mid), Point(x_mid, self._y2))
            self._win.draw_line(line, fill_color)
            line = Line(Point(to_x_mid, to_y_mid), Point(to_x_mid, to_cell._y1))
            self._win.draw_line(line, fill_color)