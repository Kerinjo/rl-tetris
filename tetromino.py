# tetromino.py
import random

SHAPES = {
    'I': [[1, 1, 1, 1]],
    'O': [[1, 1], [1, 1]],
    'T': [[0, 1, 0], [1, 1, 1]],
    'S': [[0, 1, 1], [1, 1, 0]],
    'Z': [[1, 1, 0], [0, 1, 1]],
    'J': [[1, 0, 0], [1, 1, 1]],
    'L': [[0, 0, 1], [1, 1, 1]],
}

class Tetromino:
    def __init__(self, x, y):
        self.shape_type = random.choice(list(SHAPES.keys()))
        self.shape = SHAPES[self.shape_type]
        self.color = self.shape_type
        self.x = x
        self.y = y

    def rotate_clockwise(self):
        self.shape = [list(row) for row in zip(*self.shape[::-1])]

    def rotate_counterclockwise(self):
        self.shape = [list(row) for row in zip(*self.shape)][::-1]

