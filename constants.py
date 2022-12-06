import pygame
from math import sqrt

# screen size
SCREEN_RES = (720, 770)
GAME_BORDER = (0, 50)

# pygame
NUMBERS = [pygame.K_1, pygame.K_2, pygame.K_3, pygame.K_4, pygame.K_5, pygame.K_6, pygame.K_7, pygame.K_8, pygame.K_9]

# rendering
BTN_PADDING = 10
BTN_BORDER = 2
SKETCH_OFFSET = 4
SELECT_LINE_WIDTH = 3

# board
ROW_LENGTH = 9
BOX_LENGTH = int(sqrt(ROW_LENGTH))

# game
EASY = 30
MEDIUM = 40
HARD = 50

# colors
BLACK = (0, 0, 0)
GRAY = (128, 128, 128)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
LIGHT_BLUE = (128, 128, 255)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
