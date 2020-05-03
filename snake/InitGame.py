"""
Snake Game v1.0
@author Weiwei Cao  2020-04-28

"""
import pygame
from pygame.mixer import Sound

import Snake
import Food
import Button

# Define the colors in RGB format
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
BLUE_BUTTON = (80, 118, 249)
GREEN = (80, 255, 120)
GREEN_BG = (142, 204, 57)
BRI_GREEN = (200, 255, 200)
DARK_GREEN = (50, 150, 50)
RED = (200, 0, 0)
RED_BUTTON = (255, 50, 50)
BRI_RED = (255, 200, 200)
DARK_RED = (150, 50, 50)
BLOODY = (100, 0, 0)
GREY = (100, 100, 100)

# Define the size of the window and cell
WIDTH, HEIGHT = 800, 600
ROWS, COLS = 30, 40
W_CELL, H_CELL = WIDTH // COLS, HEIGHT // ROWS

# Background songs and images
BGM = "bgm_1.wav"
BG_PIC = "page_1.png"

# Speed
EASY = 10
MEDIUM = 20
HARD = 50

# Captions
WELCOME_TXT = "Welcome to Play Snake!"
GAME_OVER_TXT = "Game Over!"
START_BUTTON_TXT = "Start"
QUIT_BUTTON_TXT = "Quit"

# Fonts
ARIAL = "arial"
GEORGIA = "georgiaboldttf"


# a class initialize the game
class Board(object):
    def __init__(self):
        """
        Initialize all related modules and the screen
        """
        # 0. initialize all modules and music
        pygame.init()
        pygame.mixer.init()
        # 1. set a screen
        self.window_size = WIDTH, HEIGHT
        self.window = pygame.display.set_mode(self.window_size)
        pygame.display.set_caption("Snake v1.0")
        self.window.fill(GREY)
        self.clock = pygame.time.Clock()
        # 2. set game status
        self.is_quit = False
        self.is_start = False
        # 3. set font and image
        self.title_font = pygame.font.SysFont(GEORGIA, 55)
        self.button_font = pygame.font.SysFont(GEORGIA, 20)
        self.normal_font = pygame.font.SysFont(GEORGIA, 30)
        self.bg_pic = pygame.image.load(BG_PIC)
        self.btn_start = Button.Button((220, 450), (110, 40), (250, 457), START_BUTTON_TXT)
        self.btn_quit = Button.Button((520, 450), (110, 40), (550, 457), QUIT_BUTTON_TXT)

    def draw_objects(self, obj: object, color: tuple) -> None:
        """
        Draw objects on the screen
        :param color: the color of objects
        :param obj: instance of an object that should be drawn on the screen
        :return: None
        """
        if isinstance(obj, Food.Food):  # case 1: draw food
            food_pos = obj.get_position()
            pygame.draw.rect(self.window, color,
                             (food_pos[0], food_pos[1], W_CELL, H_CELL))
        elif isinstance(obj, Snake.Snake):  # case 2: draw a snake
            snake_pos = obj.get_position()
            for left, top in snake_pos:
                pygame.draw.rect(self.window, color,
                                 (left, top, W_CELL, H_CELL), 2)  # rect=(left,top,w_cell,h_cell), border of snake
        elif isinstance(obj, Button.Button):  # case 3: draw a button
            button_pos = obj.get_position()
            button_size = obj.get_size()
            button_txt = obj.get_text()
            pygame.draw.rect(self.window, color,
                             (button_pos[0], button_pos[1], button_size[0], button_size[1]))  # button
            pygame.draw.rect(self.window, WHITE,
                             (button_pos[0], button_pos[1], button_size[0], button_size[1]), 2)  # border
            text_font = self.button_font.render(button_txt[0], True, WHITE)  # text
            self.window.blit(text_font, button_txt[1])

    def end_game(self, score: int) -> None:
        """
        End the current running game it will give options to user to choose a new round or exit the game
        :param score: current game scores
        :return: None
        """
        # 0. set a game over screen, including text and its color position
        self.window.fill(GREEN_BG)
        text = self.title_font.render(GAME_OVER_TXT, True, WHITE)
        self.window.blit(text, (240, 200))
        total_score = self.normal_font.render("Total Scores: " + str(score), True, WHITE)
        self.window.blit(total_score, (290, 290))
        pygame.display.update()

        while not self.is_quit:
            for event in pygame.event.get():  # wait for clicking to close the window
                if event.type == pygame.QUIT:
                    self.is_quit = True
                    break
            # draw buttons including 'start' and 'quit' and listening mouse actions
            mouse_pos = pygame.mouse.get_pos()  # get current moust status
            mouse_click = pygame.mouse.get_pressed()
            self.draw_objects(self.btn_start, BLUE_BUTTON)  # draw buttons
            self.draw_objects(self.btn_quit, RED_BUTTON)
            if self.btn_start.is_hover(mouse_pos):  # if click 'start'
                if self.btn_start.is_click(mouse_click):
                    self.is_start = True
                    break
            else:
                self.draw_objects(self.btn_start, BLUE)
            if self.btn_quit.is_hover(mouse_pos):  # if click 'quit
                if self.btn_quit.is_click(mouse_click):
                    self.is_quit = True
                    break
            else:
                self.draw_objects(self.btn_quit, RED)
            # update the screen
            pygame.display.update()  # update objects on the screen

        if self.is_start: self.play_game()
        if self.is_quit: pygame.quit()

    def play_game(self) -> None:
        """
        The main part for starting a game
        :return: None
        """
        # 0. play background music
        bgm_obj = pygame.mixer.Sound(BGM)
        bgm_obj.play(-1)
        # 1. get food and snake coordinates and draw objects on the screen
        food = Food.Food()
        snake = Snake.Snake()
        self.draw_objects(food, RED_BUTTON)
        self.draw_objects(snake, BLUE_BUTTON)
        # 2. others settings
        direction = "right"  # default next direction of the snake
        score = snake.get_length()  # get current length of the snake
        clock = pygame.time.Clock()  # generate a Clock Object for setting the speed of snake
        # 3. Main loop until the user lose or close the game.
        while not self.is_quit:
            # 3.0 This limits the while loop to a max of HARD times per second.
            clock.tick(HARD)
            # 3.1 Draw current scores on the left top of the screen
            self.window.fill(GREEN_BG)
            score = snake.get_length()
            total_score = self.button_font.render("Scores: " + str(score), True, WHITE)
            self.window.blit(total_score, (5, 0))
            # 3.2 Listen to the event,
            # to determine the game whether is still working or getting keys from users
            for event in pygame.event.get():
                if event.type == pygame.QUIT:  # close the game
                    print(f"event.type = {event.type}")
                    self.is_quit = True
                    break

                if event.type == pygame.KEYDOWN:  # receive command
                    if event.key == pygame.K_RIGHT:
                        print("*" * 30 + "right" + "*" * 30)
                        direction = "right"
                    elif event.key == pygame.K_LEFT:
                        print("*" * 30 + "left" + "*" * 30)
                        direction = "left"
                    elif event.key == pygame.K_UP:
                        print("*" * 30 + "up" + "*" * 30)
                        direction = "up"
                    elif event.key == pygame.K_DOWN:
                        print("*" * 30 + "down" + "*" * 30)
                        direction = "down"
            # 3.3 update coordinates of the snake after receiving command from user
            print('-' * 70)
            snake.move(direction)
            if not snake.is_alive():  # check whether the snake is sill alive
                break
            if food.is_eaten(snake):  # check whether the food is still exists
                snake.eat(food)
                food.update_position()
                while food.is_eaten(snake): food.update_position()  # put another food except the range of snake
            # 3.4 all is good then draw the snake and food
            self.draw_objects(snake, BLUE_BUTTON)
            self.draw_objects(food, RED_BUTTON)
            # 3.5 update the screen with what we've drawn
            pygame.display.update()

        # 4. close the game
        if self.is_quit:
            pygame.quit()
        else:
            bgm_obj.stop()
            self.end_game(score)

    def intro_game(self) -> None:
        """
        An interface the before user starting the game.
        If user click start, it will call the play_game() method
        If user click quit, it will close the window
        :return: None
        """
        # 0. to check which buttons are clicked
        while not self.is_start:
            # 0.1. draw welcome screen
            self.clock.tick(HARD)
            text = self.title_font.render(WELCOME_TXT, True, WHITE)
            self.window.blit(self.bg_pic, (0, 0))
            self.window.blit(text, (60, 110))
            # 0.2 listen to the events
            for event in pygame.event.get():# set background font and put it on the screen
                print(event)
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

            # draw buttons including 'start' and 'quit' and listening mouse actions
            mouse_pos = pygame.mouse.get_pos()
            mouse_click = pygame.mouse.get_pressed()
            self.draw_objects(self.btn_start, BLUE_BUTTON)
            self.draw_objects(self.btn_quit, RED_BUTTON)
            if self.btn_start.is_hover(mouse_pos):
                if self.btn_start.is_click(mouse_click):
                    self.is_start = True
                    break
            else:
                self.draw_objects(self.btn_start, BLUE)
            if self.btn_quit.is_hover(mouse_pos):
                if self.btn_quit.is_click(mouse_click):
                    self.is_quit = True
                    break
            else:
                self.draw_objects(self.btn_quit, RED)
            # update the screen
            pygame.display.update()

        if self.is_start:
            self.play_game()
            self.is_start = False
        if self.is_quit: pygame.quit()


if __name__ == '__main__':
    new_game = Board()
    new_game.intro_game()
