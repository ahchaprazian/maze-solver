import unittest
from maze import Maze
from graphics import Window

class Tests(unittest.TestCase):
    def test_create_maze_cells(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10, Window(800, 600))
        self.assertEqual(len(m1._cells), num_cols) 
        self.assertEqual(len(m1._cells[0]), num_rows)

    def test_create_large_maze_cells(self):
        num_cols = 16
        num_rows = 12
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10, Window(800, 600))
        self.assertEqual(len(m1._cells), num_cols)
        self.assertEqual(len(m1._cells[0]), num_rows)


if __name__ == "__main__":
    unittest.main()