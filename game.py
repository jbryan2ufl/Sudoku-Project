from constants import *
import pygame, board

class Label():
    '''
	Creates a label object which can be rendered to the screen
    Should initialize:
    self.font           - the pygame font to be used
    self.rendered_text  - the image of the text using the font
    self.text_rect      - the pygame rect using size and location

	Parameters:
    text is the text contained in the label
    location is the location the text should be displayed at
    font_size is the size of the font in pixels (height)
    color is the RGB color of the text

	Return: None
    '''
    def __init__(self, text, location, font_size=48, color=BLACK):
        pygame.font.init()
        self.font = pygame.font.Font(None, font_size)
        self.rendered_text = self.font.render(text, True, color)
        self.text_rect = self.rendered_text.get_rect(center=location)

    '''
	Draws the text to the screen

	Parameters:
    screen is the pygame surface the text should be rendered on
	Return: None
    '''
    def render(self, screen):
        screen.blit(self.rendered_text, self.text_rect)


class Button(Label):
    '''
	Creates a button that the user can click - contains a label
    Should initialize:
    super()                 - the label contained within the button
    self.background_rect    - the background rectangle
    self.border_rect        - the border rectangle (outline)
    self.background_color   - button color
    self.border_color       - border outline color
    self.text               - text within the button
    self.value              - value of the button (mainly used for difficulty)

	Parameters:
    text, location, font_size, and text_color are used to generate the label
    background_color is the color of the button
    border_color is the color of the outline
	Return: None
    '''
    def __init__(self, text, location, value=0, font_size=36, text_color=BLACK, background_color=WHITE, border_color=BLACK):
        super().__init__(text, location, font_size, text_color)
        self.background_rect = self.text_rect.inflate(BTN_PADDING, BTN_PADDING)
        self.border_rect = self.background_rect.inflate(BTN_BORDER, BTN_BORDER)
        self.background_color = background_color
        self.border_color = border_color
        self.text = text
        self.value = value

    '''
	Draws the button border, background, and text to the screen

	Parameters:
    screen is the pygame surface the text should be rendered on
	Return: None
    '''
    def render(self, screen):
        screen.fill(self.border_color, self.border_rect)
        screen.fill(self.background_color, self.background_rect)
        super().render(screen)

class Scene():
    '''
	Creates a scene which hold and uses buttons and labels

	Parameters:
    tag is the name of the scene
    btns is a list of buttons
    lbls is a list of labels
	Return: None
    '''
    def __init__(self, tag, btns=[], lbls=[]):
        self.tag = tag
        self.btns = btns
        self.lbls = lbls

    '''
	Draws the buttons and labels to the screen

	Parameters:
    screen is the pygame surface the text should be rendered on
	Return: None
    '''
    def render(self, screen):
        for obj in self.btns + self.lbls:
            obj.render(screen)


class Game():
    '''
	Creates a game instance - manages pygame rendering code and maintains the board
    Should initialize:
    self.screen         - the pygame surface everything is rendered on
    self.clock          - the pygame clock
    self.running        - boolean controlling the main game loop
    self.board          - a board object
    self.scene_list     - a list holding all scenes
    self.current_scnee  - the current scene with all buttons and labels that should be shown

	Parameters:
    scenes is a list of scenes the game will use
	Return: None
    '''
    def __init__(self, scenes):
        pygame.init()
        self.screen = pygame.display.set_mode(SCREEN_RES)
        pygame.display.set_caption("Sudoku")
        self.clock = pygame.time.Clock()
        self.running = True
        self.board = None
        self.scene_list = scenes
        self.current_scene = scenes[0]

    '''
	Finds a scene using a given tag

	Parameters:
    tag is the scene name ot be searched for
	Return: Scene or none
    '''
    def get_scene(self, tag):
        for scene in self.scene_list:
            if scene.tag == tag:
                return scene
        return None

    '''
	Changes the scene

	Parameters:
    scene is the scenes to be shown
	Return: None
    '''
    def change_scene(self, scene):
        self.current_scene = scene

    '''
	Gives the game a new board

	Parameters:
    difficulty is the number of cells to be removed
	Return: None
    '''
    def gen_board(self, difficulty):
        self.board = board.Board(SCREEN_RES[0] - GAME_BORDER[0], SCREEN_RES[1] - GAME_BORDER[1], self.screen, difficulty)

    '''
	Handles exit, keyboard, and mouse operations

	Parameters: None
	Return: None
    '''
    def handle_events(self):
        for event in pygame.event.get():
            # when the X button is clicked
            if event.type == pygame.QUIT:
                self.running = False

            # handles key presses
            if event.type == pygame.KEYDOWN:
                # all keyboard operations only happen if a board exists and a cell is selected
                if self.board:
                    if self.board.selected_cell:

                        # enter key places values if sketched, checks for win/loss
                        if event.key == pygame.K_RETURN:
                            self.board.place_number()
                            if self.board.is_full():
                                if self.board.check_board():
                                    scene = self.get_scene("WIN")
                                else:
                                    scene = self.get_scene("LOSE")
                                self.change_scene(scene)

                        # backspace clears the current cell
                        if event.key == pygame.K_BACKSPACE:
                            self.board.clear()

                        # searches all keypresses for 1-9 to be placed as a sketch
                        if event.key in NUMBERS:
                            self.board.sketch(NUMBERS.index(event.key)+1)

                        # arrow keys move the selected cell around
                        row = self.board.selected_cell.row
                        col = self.board.selected_cell.col

                        if event.key == pygame.K_UP:
                            # up doesn't go out of bounds because -1 resets to end
                            self.board.selected_cell = self.board.cells[row-1][col]

                        if event.key == pygame.K_LEFT:
                            # left doesn't go out of bounds because -1 resets to end
                            self.board.selected_cell = self.board.cells[row][col-1]

                        if event.key == pygame.K_DOWN:
                            # down can reach row 9 (doesn't exist), so we have to reset to 0
                            if row == ROW_LENGTH - 1:
                                self.board.selected_cell = self.board.cells[0][col]
                            else:
                                self.board.selected_cell = self.board.cells[row+1][col]

                        if event.key == pygame.K_RIGHT:
                            # right can reach col 9 (doesn't exist), so we have to reset to 0
                            if col == ROW_LENGTH - 1:
                                self.board.selected_cell = self.board.cells[row][0]
                            else:
                                self.board.selected_cell = self.board.cells[row][col+1]

            # handles clicks
            if event.type == pygame.MOUSEBUTTONDOWN:
                # finds the clicked button
                clicked_btn = None
                for obj in self.current_scene.btns:
                    if obj.border_rect.collidepoint(event.pos):
                        clicked_btn = obj
                
                if clicked_btn:
                    # difficulty buttons change scene to game and generate a board using value
                    if self.current_scene.tag == "MENU":
                        self.gen_board(clicked_btn.value)
                        self.change_scene(self.get_scene("GAME"))
                    # closes sudoku
                    if clicked_btn.text == "EXIT":
                        self.running = False
                    # resets the board to its original state
                    elif clicked_btn.text == "RESET":
                        self.board.reset_to_original()
                    # sends the user back to the menu
                    elif clicked_btn.text == "RESTART":
                        self.change_scene(self.get_scene("MENU"))
                else:
                    # allows the user to select a cell with their mouse
                    if self.board:
                        self.board.click(event.pos[0], event.pos[1])

    '''
	Draws the current scene to the screen

	Parameters: None
	Return: None
    '''
    def render(self):
        for obj in self.current_scene.btns + self.current_scene.lbls:
            obj.render(self.screen)
        if self.current_scene.tag == "GAME":
            self.board.draw()

    '''
	Main game loop for events and rendering

	Parameters: None
	Return: None
    '''
    def loop(self):
        while self.running:
            # sets the background of the game to white
            self.screen.fill(WHITE)

            self.handle_events()

            self.render()

            pygame.display.update()
            self.clock.tick()

'''
Generates the game layout with labels, buttons, and scenes

Parameters: None
Return: Game
'''
def generate_game():
    width = SCREEN_RES[0]
    height = SCREEN_RES[1]
    # menu elements
    lbl_menu = Label("Welcome to Sudoku", (width / 2, height / 3))
    lbl_mode = Label("Select Game Mode:", (width / 2, height * 1 / 2))
    btn_easy = Button("EASY", (width / 3, height * 2 / 3), EASY, background_color=GREEN)
    btn_medium = Button("MEDIUM", (width / 2, height * 2 / 3), MEDIUM, background_color=YELLOW)
    btn_hard = Button("HARD", (width * 2 / 3, height * 2 / 3), HARD, background_color=RED)
    scn_menu = Scene("MENU", [btn_easy, btn_medium, btn_hard], [lbl_menu, lbl_mode])

    # game elements
    btn_game_reset = Button("RESET", (width / 3, (height * 2 - GAME_BORDER[1]) / 2), background_color=LIGHT_BLUE)
    btn_game_restart = Button("RESTART", (width / 2, (height * 2 - GAME_BORDER[1]) / 2), background_color=LIGHT_BLUE)
    btn_game_exit = Button("EXIT", (width * 2 / 3, (height * 2 - GAME_BORDER[1]) / 2), background_color=LIGHT_BLUE)
    scn_game = Scene("GAME", [btn_game_reset, btn_game_restart, btn_game_exit])

    # win screen elements
    lbl_win = Label("Game Won!", (width / 2, height / 3))
    btn_win_exit = Button("EXIT", (width / 2, height * 2 / 3), font_size=48, background_color=LIGHT_BLUE)
    scn_win = Scene("WIN", [btn_win_exit], [lbl_win])

    # lose screen elements
    lbl_lose = Label("Game Over :(", (width / 2, height / 3))
    btn_lose_restart = Button("RESTART", (width / 2, height * 2 / 3), font_size=48, background_color=LIGHT_BLUE)
    scn_lose = Scene("LOSE", [btn_lose_restart], [lbl_lose])

    # create the game with the scenes
    return Game([scn_menu, scn_game, scn_win, scn_lose])
