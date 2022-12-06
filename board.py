<<<<<<< HEAD
from constants import *
import pygame
from cell import Cell
from sudoku_generator import generate_sudoku

class Board():
    '''
	create a sudoku board - initialize class variables and set up the 2D board
	This should initialize:
	self.width          - the width of the board in pixels
	self.height         - the height of the board in pixels
	self.screen         - the pygame surface to render to
	self.board          - a 2D list representing the values
    self.count          - the number of nonzero cells
    self.cells          - a 2D list of cell objects
    self.orig_board     - a 2D list representing the original board with cells removed
    self.selected_cell  - the current cell object

	Parameters:
    width is the board width in pixels
    height is the board height in pixels
    screen is the pygame surface to render to
    difficulty is the number of board values to be removed

	Return:	None
    '''
    def __init__(self, width, height, screen, difficulty):
        self.width = width
        self.height = height
        self.screen = screen
        self.difficulty = difficulty

        self.board = generate_sudoku(ROW_LENGTH, difficulty)
        self.count = ROW_LENGTH ** 2 - difficulty
        self.cells = []
        temp = []
        for i in range(ROW_LENGTH):
            for j in range(ROW_LENGTH):
                temp.append(Cell(self.board[i][j], i, j, screen))
            self.cells.append(temp)
            temp = []
        self.orig_board = [row[:] for row in self.board]
        self.selected_cell = None

    '''
	Draws the board lines, cells, and selected outline

	Parameters: None
	Return: None
    '''
    def draw(self):
        # draws the lines for the board
        for i in range(ROW_LENGTH+1):
            # thicker lines for line 0, 3, 6, and 9
            board_line_width = 3 if i % BOX_LENGTH == 0 else 1
            pygame.draw.line(self.screen, BLACK, (0, self.width/ROW_LENGTH*i), (self.width, self.width/ROW_LENGTH*i), board_line_width)
            pygame.draw.line(self.screen, BLACK, (self.height/ROW_LENGTH*i, 0), (self.height/ROW_LENGTH*i, self.height), board_line_width)
        
        # draws cells
        for i in range(ROW_LENGTH):
            for j in range(ROW_LENGTH):
                # determines whether user entered
                if self.orig_board[i][j] == 0:
                    self.cells[i][j].draw(True)
                else:
                    self.cells[i][j].draw()
        
        # draws selected cell outline
        if self.selected_cell != None:
            pygame.draw.rect(self.screen, RED, self.selected_cell.rect, SELECT_LINE_WIDTH)

    '''
	Sets the selected cell to one in the cells 2D list

	Parameters:
    row is the cell row
    col is the cell column
	Return: None
    '''
    def select(self, row, col):
        self.selected_cell = self.cells[row][col]

    '''
	Uses click position to determine which cell was selected

	Parameters:
    x is the horizontal pixel position
    y is the vertical pixel position
	Return: tuple(x, y) or None
    '''
    def click(self, x, y):
        if x > 0 and x < self.width and y > 0 and y < self.height:
            row = int(y//(self.height/ROW_LENGTH))
            col = int(x//(self.width/ROW_LENGTH))
            self.select(row, col)
            return (int(y//(self.height/ROW_LENGTH)), int(x//(self.width/ROW_LENGTH)))
        else:
            return None

    '''
	Clears the currently selected cell (if possible)

	Parameters: None
	Return: None
    '''
    def clear(self):
        if self.orig_board[self.selected_cell.row][self.selected_cell.col] == 0 and (self.selected_cell.value != 0 or self.selected_cell.sketch_value != 0):
            self.selected_cell.value = 0
            self.selected_cell.sketch_value = 0
            self.count -= 1
            self.update_board()

    '''
	Sets the currently selected cell's sketch value

	Parameters:
    value is the number input by the keyboard to be sketched
	Return: None
    '''
    def sketch(self, value):
        if self.selected_cell.value == 0:
            self.selected_cell.set_sketched_value(value)

    '''
	Places the currently selected cell's sketch value as the main value and
    clears the selected cell's sketch value

	Parameters: None
	Return: None
    '''
    def place_number(self):
        if self.selected_cell.sketch_value != 0:
            self.selected_cell.value = self.selected_cell.sketch_value
            self.selected_cell.sketch_value = 0
            self.count += 1
            self.update_board()

    '''
	Copies values from the original board to the current board

	Parameters: None
	Return: None
    '''
    def reset_to_original(self):
        self.board = [row[:] for row in self.orig_board]
        for i in range(ROW_LENGTH):
            for j in range(ROW_LENGTH):
                self.cells[i][j].value = self.board[i][j]
                self.cells[i][j].sketch_value = 0
        self.count = ROW_LENGTH ** 2 - self.difficulty

    '''
	Determines if the board is full (no 0s left)

	Parameters: None
	Return: boolean
    '''
    def is_full(self):
        if self.count == ROW_LENGTH ** 2:
            return True
        return False

    '''
	Updates the board with the selected cell's value
    Should only be used after changing a cell value

	Parameters: None
	Return: None
    '''
    def update_board(self):
        row = self.selected_cell.row
        col = self.selected_cell.col
        self.board[row][col] = self.selected_cell.value

    '''
	Checks if the board is full and all values are correct
    Uses sets to determine if each of one number 1-9 is in each row, col, and box

	Parameters: None
	Return: boolean
    '''
    def check_board(self):       
        # check row and col
        temp_row = []
        temp_col = []
        for i in range (ROW_LENGTH):
            temp_row = []
            temp_col = []
            for j in range(ROW_LENGTH):
                temp_col.append(self.board[i][j])
                temp_row.append(self.board[j][i])
            if len(set(temp_col)) != ROW_LENGTH or len(set(temp_row)) != ROW_LENGTH:
                return False
        
        # check box
        for i in range(BOX_LENGTH):
            for j in range(BOX_LENGTH):
                temp_box = []
                for k in range(BOX_LENGTH):
                    for l in range(BOX_LENGTH):
                        temp_box.append(self.board[i*BOX_LENGTH+k][j*BOX_LENGTH+l])
                if len(set(temp_box)) != ROW_LENGTH:
                    return False
        return True
=======
from constants import *
import pygame
from cell import Cell
from sudoku_generator import generate_sudoku

class Board():
    '''
	create a sudoku board - initialize class variables and set up the 2D board
	This should initialize:
	self.width          - the width of the board in pixels
	self.height         - the height of the board in pixels
	self.screen         - the pygame surface to render to
	self.board          - a 2D list representing the values
    self.count          - the number of nonzero cells
    self.cells          - a 2D list of cell objects
    self.orig_board     - a 2D list representing the original board with cells removed
    self.selected_cell  - the current cell object

	Parameters:
    width is the board width in pixels
    height is the board height in pixels
    screen is the pygame surface to render to
    difficulty is the number of board values to be removed

	Return:	None
    '''
    def __init__(self, width, height, screen, difficulty):
        self.width = width
        self.height = height
        self.screen = screen
        self.difficulty = difficulty

        self.board = generate_sudoku(ROW_LENGTH, difficulty)
        self.count = ROW_LENGTH ** 2 - difficulty
        self.cells = []
        temp = []
        for i in range(ROW_LENGTH):
            for j in range(ROW_LENGTH):
                temp.append(Cell(self.board[i][j], i, j, screen))
            self.cells.append(temp)
            temp = []
        self.orig_board = [row[:] for row in self.board]
        self.selected_cell = None

    '''
	Draws the board lines, cells, and selected outline

	Parameters: None
	Return: None
    '''
    def draw(self):
        # draws the lines for the board
        for i in range(ROW_LENGTH+1):
            # thicker lines for line 0, 3, 6, and 9
            board_line_width = 3 if i % BOX_LENGTH == 0 else 1
            pygame.draw.line(self.screen, BLACK, (0, self.width/ROW_LENGTH*i), (self.width, self.width/ROW_LENGTH*i), board_line_width)
            pygame.draw.line(self.screen, BLACK, (self.height/ROW_LENGTH*i, 0), (self.height/ROW_LENGTH*i, self.height), board_line_width)
        
        # draws cells
        for i in range(ROW_LENGTH):
            for j in range(ROW_LENGTH):
                # determines whether user entered
                if self.orig_board[i][j] == 0:
                    self.cells[i][j].draw(True)
                else:
                    self.cells[i][j].draw()
        
        # draws selected cell outline
        if self.selected_cell != None:
            pygame.draw.rect(self.screen, RED, self.selected_cell.rect, SELECT_LINE_WIDTH)

    '''
	Sets the selected cell to one in the cells 2D list

	Parameters:
    row is the cell row
    col is the cell column
	Return: None
    '''
    def select(self, row, col):
        self.selected_cell = self.cells[row][col]

    '''
	Uses click position to determine which cell was selected

	Parameters:
    x is the horizontal pixel position
    y is the vertical pixel position
	Return: tuple(x, y) or None
    '''
    def click(self, x, y):
        if x > 0 and x < self.width and y > 0 and y < self.height:
            row = int(y//(self.height/ROW_LENGTH))
            col = int(x//(self.width/ROW_LENGTH))
            self.select(row, col)
            return (int(y//(self.height/ROW_LENGTH)), int(x//(self.width/ROW_LENGTH)))
        else:
            return None

    '''
	Clears the currently selected cell (if possible)

	Parameters: None
	Return: None
    '''
    def clear(self):
        if self.orig_board[self.selected_cell.row][self.selected_cell.col] == 0 and (self.selected_cell.value != 0 or self.selected_cell.sketch_value != 0):
            self.selected_cell.value = 0
            self.selected_cell.sketch_value = 0
            self.count -= 1
            self.update_board()

    '''
	Sets the currently selected cell's sketch value

	Parameters:
    value is the number input by the keyboard to be sketched
	Return: None
    '''
    def sketch(self, value):
        if self.selected_cell.value == 0:
            self.selected_cell.set_sketched_value(value)

    '''
	Places the currently selected cell's sketch value as the main value and
    clears the selected cell's sketch value

	Parameters: None
	Return: None
    '''
    def place_number(self):
        if self.selected_cell.sketch_value != 0:
            self.selected_cell.value = self.selected_cell.sketch_value
            self.selected_cell.sketch_value = 0
            self.count += 1
            self.update_board()

    '''
	Copies values from the original board to the current board

	Parameters: None
	Return: None
    '''
    def reset_to_original(self):
        self.board = [row[:] for row in self.orig_board]
        for i in range(ROW_LENGTH):
            for j in range(ROW_LENGTH):
                self.cells[i][j].value = self.board[i][j]
                self.cells[i][j].sketch_value = 0
        self.count = ROW_LENGTH ** 2 - self.difficulty

    '''
	Determines if the board is full (no 0s left)

	Parameters: None
	Return: boolean
    '''
    def is_full(self):
        if self.count == ROW_LENGTH ** 2:
            return True
        return False

    '''
	Updates the board with the selected cell's value
    Should only be used after changing a cell value

	Parameters: None
	Return: None
    '''
    def update_board(self):
        row = self.selected_cell.row
        col = self.selected_cell.col
        self.board[row][col] = self.selected_cell.value

    '''
	Checks if the board is full and all values are correct
    Uses sets to determine if each of one number 1-9 is in each row, col, and box

	Parameters: None
	Return: boolean
    '''
    def check_board(self):       
        # check row and col
        temp_row = []
        temp_col = []
        for i in range (ROW_LENGTH):
            temp_row = []
            temp_col = []
            for j in range(ROW_LENGTH):
                temp_col.append(self.board[i][j])
                temp_row.append(self.board[j][i])
            if len(set(temp_col)) != ROW_LENGTH or len(set(temp_row)) != ROW_LENGTH:
                return False
        
        # check box
        for i in range(BOX_LENGTH):
            for j in range(BOX_LENGTH):
                temp_box = []
                for k in range(BOX_LENGTH):
                    for l in range(BOX_LENGTH):
                        temp_box.append(self.board[i*BOX_LENGTH+k][j*BOX_LENGTH+l])
                if len(set(temp_box)) != ROW_LENGTH:
                    return False
        return True
>>>>>>> 083443b951a53aef0996982bb9339b196c9f9192
