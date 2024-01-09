from graphics import Window, Line, Point
from maze import Maze
from cell import Cell
import sys

def main():
    screen_size_x = 800
    screen_size_y = 600

    sys.setrecursionlimit(10000)
    window = Window(screen_size_x, screen_size_y)
    num_rows = 12
    num_cols = 16
    margin = 50
    cell_size_x = (screen_size_x - 2 * margin) / num_cols
    cell_size_y = (screen_size_y - 2 * margin) / num_rows

    maze = Maze(margin, margin, num_rows, num_cols, cell_size_x, cell_size_y, window)
    print("maze created")
    is_solveable = maze.solve()

    if is_solveable:
        print("maze solved!")
    else:
        print("maze cannot be solved!")
    window.wait_for_close()

if __name__ == "__main__":
    main()