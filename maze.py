import pygame
from colours import black, white, blue, pink, green, yellow

class Maze:
    def __init__(self, screen, num_rows, num_cols):
        self.screen = screen

        self.num_rows = num_rows
        self.num_cols = num_cols
        # uncomment this for prebuilt board
        # self.board = [
        #     [0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        #     [1, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1],
        #     [1, 1, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 1, 0, 1],
        #     [1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 1, 1],
        #     [1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 1],
        #     [1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1],
        #     [0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 0, 1],
        #     [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
        #     [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0],
        #     [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1],
        #     [1, 0, 1, 1, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0],
        #     [1, 0, 0, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 0],
        #     [1, 1, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 1, 0],
        #     [1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 1, 0],
        #     [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
        # ]
        self.board = [[0 for _ in range(self.num_cols)] for _ in range(self.num_cols)]

    def update(self):
        left, _, right = pygame.mouse.get_pressed()
        if not left and not right:
            return

        # get mouse position and screen size
        x, y = pygame.mouse.get_pos()
        screen_width, screen_height = self.screen.get_size()

        # get wall width and height
        width = screen_width // self.num_cols
        height = screen_height // self.num_rows

        if x < 0 or y < 0 or x >= width * self.num_cols or y >= height * self.num_rows:
            return

        # add or remove a wall
        if left:
            self.board[y // height][x // width] = 1
        elif right:
            self.board[y // height][x // width] = 0

    def draw(self, player_past, player_places):
        # get screen width and height
        screen_width, screen_height = self.screen.get_size()

        # get wall width and height
        width = screen_width // self.num_cols
        height = screen_height // self.num_rows

        for row in range(self.num_rows):
            for col in range(self.num_cols):
                if self.board[row][col]:
                    # draw blue square
                    pygame.draw.rect(self.screen, blue, (col * width, row * height, width, height))
                else:
                    # draw white square
                    pygame.draw.rect(self.screen, white, (col * width, row * height, width, height))

        for row, col in player_places:
            # draw pink squares
            pygame.draw.rect(self.screen, pink, (col * width, row * height, width, height))

        for row, col in player_past:
            # draw green square
            pygame.draw.rect(self.screen, green, (col * width, row * height, width, height))

        # draw yellow squares
        pygame.draw.rect(self.screen, yellow, (0, 0, width, height))
        pygame.draw.rect(self.screen, yellow, ((self.num_cols - 1) * width, (self.num_rows - 1) * height, width, height))

        for row in range(self.num_rows):
            for col in range(self.num_cols):
                # draw black outline
                pygame.draw.rect(self.screen, black, (col * width, row * height, width, height), 1)
