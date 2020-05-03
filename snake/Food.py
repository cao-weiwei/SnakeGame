"""
@author Weiwei Cao  2020-05-03
This is a class of Food.
"""

import random
import InitGame
import Snake


class Food:
    def __init__(self):
        """
        Initialize the first pair of coordinate of food
        """
        self.food_x = random.randint(5, InitGame.COLS - 5) * InitGame.W_CELL
        self.food_y = random.randint(5, InitGame.ROWS - 5) * InitGame.H_CELL
        self.food_pos = [self.food_x, self.food_y]

    def update_position(self) -> None:
        """
        Randomly generate a new pair of coordinate for putting food
        :return: None
        """
        self.food_x = random.randint(5, InitGame.COLS - 5) * InitGame.W_CELL
        self.food_y = random.randint(5, InitGame.ROWS - 5) * InitGame.H_CELL
        self.food_pos = [self.food_x, self.food_y]

    def get_position(self) -> list:
        """
        Get the food position
        :return: a list contains the food coordinate in x-axis and y-axis
        """
        return self.food_pos

    def is_eaten(self, snake: Snake) -> bool:
        """
        To check the food is whether eaten by the snake
        :param snake: an instance of Snake
        :return: True if the food is eaten by the snake else return False
        """
        if self.food_pos in snake.get_position():
            return True
        else:
            return False
