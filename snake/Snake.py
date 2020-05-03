"""
@author Weiwei Cao  2020-05-03
This is a class of Snake.
"""

import Food
import InitGame


class Snake:
    def __init__(self):
        """
        initialize a snake
        """
        self.default_length = 5
        self.head_x, self.head_y = [InitGame.WIDTH // 4, InitGame.HEIGHT // 2]
        # self.snake_head = [  # coordinates of head
        #     self.head_x, self.head_y
        # ]
        # self.snake_body = [  # coordinates of body
        #     self.head_x - 1, self.head_y,
        #     self.head_x - 2, self.head_y,
        #     self.head_x - 3, self.head_y,
        #     self.head_x - 4, self.head_y
        # ]
        # self.snake_tail = [  # coordinates of tail
        #     self.head_x - 4, self.head_y
        # ]
        # self.snake = [  # coordinates of snake = head + body + tail
        #     # self.snake_head,
        #     # self.snake_body,
        #     # self.snake_tail
        # ]
        self.snake = [[self.head_x - (i * 20), self.head_y] for i in range(self.default_length)]
        self.current_direction = "right"  # default direction of the snake

    def move(self, next_direction: str) -> None:
        """
        receive signals from keyboard and changing coordinates of the snake
        :param next_direction: next direction string
        :return: None
        """
        # 0. change the direction of next direction is not opposite with current direct
        if self.current_direction == "right" and next_direction != "left" \
                or self.current_direction == "left" and next_direction != "right" \
                or self.current_direction == "up" and next_direction != "down" \
                or self.current_direction == "down" and next_direction != "up":
            self.current_direction = next_direction

        # 0.1 get new head position
        new_head_x, new_head_y = self.head_x, self.head_y
        if self.current_direction == "up":
            new_head_x = self.head_x
            new_head_y -= 20
        elif self.current_direction == "down":
            new_head_x = self.head_x
            new_head_y += 20
        elif self.current_direction == "left":
            new_head_x -= 20
            new_head_y = self.head_y
        elif self.current_direction == "right":
            new_head_x += 20
            new_head_y = self.head_y
        # 0.2 insert new head into the 1st index and update the head position
        self.snake.insert(0, [new_head_x, new_head_y])
        self.head_x, self.head_y = new_head_x, new_head_y
        # 0.3 pop the last coordinate (x, y)
        self.snake.pop()
        print(self.snake)

    def get_position(self) -> list:
        """
        get the coordinates of the snake = head * 1
        :return: a list contains coordinates of a snake
        """
        return self.snake

    def get_length(self) -> int:
        """
        get current length of the snake
        :return: current length of the snake
        """
        return len(self.snake) - self.default_length

    def eat(self, food: Food) -> None:
        """
        After eating a piece of food, updating the coordinates of the snake
        :param food: an instance of Food
        :return: None
        """
        food_pos = food.get_position()  # get the food position
        self.snake.insert(0, [food_pos[0], food_pos[1]])  # add food into the snake
        self.head_x, self.head_y = food_pos[0], food_pos[1]  # update the head of the snale

    def is_alive(self) -> bool:
        """
        Check whether the snake is alive
        :return: True if the snake is alive, otherwise False
        """
        # if the snake head is on the border or has collision with itself, then dead, return False
        if self.head_x in [-InitGame.W_CELL, InitGame.WIDTH] or self.head_y in [-InitGame.H_CELL, InitGame.HEIGHT] \
                or [self.head_x, self.head_y] in self.snake[1:]:
            return False
        else:  # the snake is alive
            return True
