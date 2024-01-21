from tkinter import Tk, BOTH, Canvas


class Window:
    """
    A class representing a graphical window for a maze solver.

    Parameters:
    - width (int): The width of the window.
    - height (int): The height of the window.
    """

    def __init__(self, width, height):
        """
        Initializes the Window object.

        Args:
        - width (int): The width of the window.
        - height (int): The height of the window.
        """
        self.__root = Tk()
        self.__root.title("Maze Solver")
        self.__root.protocol("WM_DELETE_WINDOW", self.close)
        self.__canvas = Canvas(self.__root, bg="white", height=height, width=width)
        self.__canvas.pack(fill=BOTH, expand=1)
        self.__running = False


    def redraw(self):
        """
        Redraws the window to reflect any changes.
        """
        self.__root.update_idletasks()
        self.__root.update()


    def wait_for_close(self):
        """
        Waits for the window to be closed.

        This method enters a loop, continuously redrawing the window until it is closed.
        """
        self.__running = True
        while self.__running:
            self.redraw()
        print("window closed...")


    def draw_line(self, line, fill_color="black"):
        """
        Draws a line on the canvas.

        Args:
        - line (Line): The Line object to be drawn.
        - fill_color (str): The fill color of the line. Default is "black".
        """
        line.draw(self.__canvas, fill_color)


    def close(self):
        """
        Closes the window.
        """
        self.__running = False


class Point:
    """
    A class representing a 2D point with x and y coordinates.

    Parameters:
    - x (float): The x-coordinate of the point.
    - y (float): The y-coordinate of the point.
    """
    def __init__(self, x, y):
        """
        Initializes the Point object.

        Args:
        - x (float): The x-coordinate of the point.
        - y (float): The y-coordinate of the point.
        """
        self.x = x
        self.y = y


class Line:
    """
    A class representing a line connecting two points.

    Parameters:
    - p1 (Point): The starting point of the line.
    - p2 (Point): The ending point of the line.
    """
    def __init__(self, p1, p2):
        """
        Initializes the Line object.

        Args:
        - p1 (Point): The starting point of the line.
        - p2 (Point): The ending point of the line.
        """

        self.p1 = p1
        self.p2 = p2


    def draw(self, canvas, fill_color="black"):
        """
        Draws the line on the given canvas.

        Args:
        - canvas: The canvas on which to draw the line.
        - fill_color (str): The fill color of the line. Default is "black".
        """
        canvas.create_line(
            self.p1.x, self.p1.y, self.p2.x, self.p2.y, fill=fill_color, width=2
        )
        canvas.pack(fill=BOTH, expand=1)