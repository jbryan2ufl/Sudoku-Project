import pygame
from constants import *

pygame.font.init()
value_font = pygame.font.Font(None, 48)
sketch_font = pygame.font.Font(None, 36)
# rendered images of numbers 1-9
rendered_values = [value_font.render(str(i), True, BLACK) for i in range(1, 10)]
rendered_values_user = [value_font.render(str(i), True, BLUE) for i in range(1, 10)]
rendered_sketches = [sketch_font.render(str(i), True, LIGHT_BLUE) for i in range(1, 10)]

class Cell():
    '''
	Creates a cell object within the board
    Should initialize:
    self.value          - confirmed cell value
    self.sketch_value   - value for the user to stage before locking in
    self.row            - row on the board
    self.col            - col on the board
    self.screen         - pygame surface for rendering
    self.rect           - pygame rect 

	Parameters:
    value is the cell's number
    row is the row on the board
    col is the col on the board
    screen is the pygame surface
	Return: None
    '''
    def __init__(self, value, row, col, screen):
        self.value = value
        self.sketch_value = 0
        self.row = row
        self.col = col
        self.screen = screen
        self.rect = pygame.Rect((SCREEN_RES[0]-GAME_BORDER[0])/ROW_LENGTH*col, (SCREEN_RES[1]-GAME_BORDER[1])/ROW_LENGTH*row, (SCREEN_RES[0]-GAME_BORDER[0])/ROW_LENGTH, (SCREEN_RES[1]-GAME_BORDER[1])/ROW_LENGTH)

    '''
    Changes the cells value

    Parameters:
    value is the new value for the cell
    Return: None
    '''
    def set_cell_value(self, value):
        self.value = value

    '''
    Changes the sketch value

    Parameters:
    value is the new sketch value
    Return: None
    '''
    def set_sketched_value(self, value):
        self.sketch_value = value

    '''
    Generates the game layout with labels, buttons, and scenes

    Parameters:
    user is a boolean representing whether the cell is user entered or a static board cell
    Return: None
    '''
    def draw(self, user=False):
        if self.sketch_value != 0:
            self.screen.blit(rendered_sketches[self.sketch_value-1], self.rect.move(SKETCH_OFFSET, SKETCH_OFFSET))
        if self.value != 0:
            cell_center_offset = (SCREEN_RES[0]-GAME_BORDER[0])/ROW_LENGTH*self.col+(SCREEN_RES[0]-GAME_BORDER[0])/(ROW_LENGTH*2), (SCREEN_RES[1]-GAME_BORDER[1])/ROW_LENGTH*self.row+(SCREEN_RES[1]-GAME_BORDER[1])/(ROW_LENGTH*2)
            if user:
                self.screen.blit(rendered_values_user[self.value-1], rendered_values_user[self.value-1].get_rect(center=(cell_center_offset)))
            else:
                self.screen.blit(rendered_values[self.value-1], rendered_values[self.value-1].get_rect(center=(cell_center_offset)))
