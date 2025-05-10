# game.py
import pygame
from config import *
from tetromino import Tetromino

class Game:
    def __init__(self):
        self.grid = [[None for _ in range(GRID_WIDTH)] for _ in range(GRID_HEIGHT)]
        self.current_piece = Tetromino(GRID_WIDTH // 2 - 2, 0)
        self.game_over = False
        self.score = 0

    def valid_position(self, shape, offset_x, offset_y):
        for y, row in enumerate(shape):
            for x, cell in enumerate(row):
                if cell:
                    new_x = x + offset_x
                    new_y = y + offset_y
                    if new_x < 0 or new_x >= GRID_WIDTH or new_y >= GRID_HEIGHT:
                        return False
                    if new_y >= 0 and self.grid[new_y][new_x]:
                        return False
        return True

    def lock_piece(self):
        for y, row in enumerate(self.current_piece.shape):
            for x, cell in enumerate(row):
                if cell:
                    gx = self.current_piece.x + x
                    gy = self.current_piece.y + y
                    if 0 <= gy < GRID_HEIGHT:
                        self.grid[gy][gx] = self.current_piece.color
        self.clear_lines()
        self.current_piece = Tetromino(GRID_WIDTH // 2 - 2, 0)
        if not self.valid_position(self.current_piece.shape, self.current_piece.x, self.current_piece.y):
            self.game_over = True

    def clear_lines(self):
        new_grid = []
        lines_cleared = 0
        for row in self.grid:
            if all(cell is not None for cell in row):
                lines_cleared += 1
            else:
                new_grid.append(row)

        while len(new_grid) < GRID_HEIGHT:
            new_grid.insert(0, [None for _ in range(GRID_WIDTH)])
        
        self.grid = new_grid
        self.score += scores.get(lines_cleared, 0)

    # def clear_lines(self):
        # self.grid = [row for row in self.grid if any(cell is None for cell in row)]
        # while len(self.grid) < GRID_HEIGHT:
        #     self.grid.insert(0, [None for _ in range(GRID_WIDTH)])

    def move(self, dx, dy):
        if self.valid_position(self.current_piece.shape, self.current_piece.x + dx, self.current_piece.y + dy):
            self.current_piece.x += dx
            self.current_piece.y += dy
            return True
        elif dy == 1:
            self.lock_piece()
        return False

    def rotate(self, direction='right'):
        original = self.current_piece.shape
        if direction == 'right':
            self.current_piece.rotate_clockwise()
        elif direction == 'left':
            self.current_piece.rotate_counterclockwise()

        if not self.valid_position(self.current_piece.shape, self.current_piece.x, self.current_piece.y):
            self.current_piece.shape = original  # revert if invalid

    def update(self):
        self.move(0, 1)

    def draw(self, screen):
        screen.fill(COLORS['BG'])
        # Draw grid
        for y in range(GRID_HEIGHT):
            for x in range(GRID_WIDTH):
                cell = self.grid[y][x]
                color = COLORS[cell] if cell else COLORS['G']
                pygame.draw.rect(screen, color, (x*CELL_SIZE, y*CELL_SIZE, CELL_SIZE, CELL_SIZE), 0)
        # Draw current piece
        for y, row in enumerate(self.current_piece.shape):
            for x, cell in enumerate(row):
                if cell:
                    pygame.draw.rect(
                        screen,
                        COLORS[self.current_piece.color],
                        ((self.current_piece.x + x)*CELL_SIZE, (self.current_piece.y + y)*CELL_SIZE, CELL_SIZE, CELL_SIZE),
                    )

