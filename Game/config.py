"""
This is the file upon which the specifications of the game are based.
From the look and colours of the game window, to the actual physics of the 
game. Reader can change this to experiment with the NEAT Algorithm part.

Look under 'Bird Physics' and 'Pipe Physics'.
"""

import pygame

# COLO(U)RS
BLUE = (0, 0, 255)
DARK_BLUE = (0, 0, 127)
LIGHT_BLUE = (127, 127, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# SCREEN
FPS = 30
pygame.time.Clock().tick(FPS)
SCREEN_HEIGHT = 720
SCREEN_WIDTH = 450
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Flapi Birb')
pygame.font.init()
font = pygame.font.Font('freesansbold.ttf', 32) 

# BIRD PHYSICS
GRAVITY = 0.00005
BIRD_SIZE = 15
BIRD_COLOR = YELLOW
BIRD_INITIAL_VELOCITY = 0.0001
BIRD_TERMINAL_VELOCITY = 0.0003
BIRD_UPWARD_VELOCITY = -0.05
BIRD_JUMP_HEIGHT = -1.2

# PIPE PHYSICS
PIPE_VELOCITY = -0.25
PIPE_WIDTH = 100
PIPE_RANGE_FROM_BOTTOM = 150
PIPE_RANGE_FROM_TOP = 200
PIPE_GAP = 150
PIPE_SPACER = 200

# DESIGN
BIRD_X_INIT = 100
BIRD_SPACER_INIT = 100
GROUND_HEIGHT = 45
SKY_HEIGHT = 10
BIRD_DEATH_TIME = 1
