import pygame
from maze import Maze
from player import Player

# constants
width = 600
height = 600
FPS = 30
num_rows = 15
num_cols = 15

# setup window
pygame.init()
screen = pygame.display.set_mode((width, height), pygame.RESIZABLE)
pygame.display.set_caption("Maze Solver")

# setup clock
clock = pygame.time.Clock()

# create maze and player
maze = Maze(screen, num_rows, num_cols)
player = Player(screen, num_rows, num_cols)

running = True
while running:
    for event in pygame.event.get():
        # exit on "X"
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()

        # # update player on space
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if not player.started:
                    player.started = True
                else:
                    player = Player(screen, num_rows, num_cols)

    if player.active and player.started:
        player.update(maze.board)
    else:
        maze.update()

    # draw the screen
    maze.draw(player.past, player.places)
    player.draw()
    pygame.display.update()

    clock.tick(30)
