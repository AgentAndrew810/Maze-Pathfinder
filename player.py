import pygame
from colours import red


class Player:
    def __init__(self, screen, num_rows, num_cols):
        self.screen = screen

        self.num_rows = num_rows
        self.num_cols = num_cols

        self.row = 0
        self.col = 0

        self.past = [(0, 0), (0, 0)]
        self.places = [(0, 0)]

        self.dead_end = False
        self.dead_ends = []

        self.started = False
        self.active = True

    def draw(self):
        # get screen width and height
        screen_width, screen_height = self.screen.get_size()

        # get wall width and height
        width = screen_width // self.num_rows
        height = screen_height // self.num_cols

        pygame.draw.circle(self.screen, red, (self.col * width + width // 2, self.row * height + height // 2), width * 0.4, width // 8)

    def get_moves(self, board):
        # get a list of moves to move
        moves = []
        # check right
        if not self.col == self.num_cols - 1 and not board[self.row][self.col + 1]:
            moves.append((self.row, self.col + 1))
        # check below
        if not self.row == self.num_rows - 1 and not board[self.row + 1][self.col]:
            moves.append((self.row + 1, self.col))
        # check left
        if not self.col == 0 and not board[self.row][self.col - 1]:
            moves.append((self.row, self.col - 1))
        # check above
        if not self.row == 0 and not board[self.row - 1][self.col]:
            moves.append((self.row - 1, self.col))

        return moves

    def update(self, board):
        moves = self.get_moves(board)
        made_move = False
        for move in moves:
            if not move in self.past and move not in self.dead_ends:
                self.row, self.col = move
                self.past.insert(0, move)
                self.places.insert(0, move)
                made_move = True
                break

        if not made_move:
            self.dead_ends.append(self.past[0])
            self.past.pop(0)
            try:
                self.row, self.col = self.past[0]
            except IndexError:
                self.active = False

        # if reached the end, deactive
        if self.active:
            if self.past[0] == (self.num_rows - 1, self.num_cols - 1):
                self.active = False
