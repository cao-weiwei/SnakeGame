"""
References:
https://docs.python.org/3/library/curses.html
https://youtu.be/rbasThWVb-c
https://blog.csdn.net/qq_37553152/article/details/80290278
"""

import curses
import random

""" initialize the screen """
main_scr = curses.initscr()  # initialize a main screen of the game
curses.curs_set(0)  # - setting the visibility of cursor, 0 invisible, 1 normal, 2 strong
height, width = main_scr.getmaxyx()  # - get the height and width of the main screen
board = curses.newwin(height, width, 0, 0)  # - initialize a board for gaming with the maximum size of the main # screen
board.keypad(1)  # ?
board.timeout(100)  # - setting for input, every 100ms the board will get a char from user

""" draw a snake on the board """
snake_y = int(height / 4)  # initial coordinates of a snake with height and width
snake_x = int(width / 2)
snake = [  # draw a snake with coordinates on the board
    [snake_y, snake_x],  # - the coordinates of head
    [snake_y, snake_x - 1],  # - the coordinates of body
    [snake_y, snake_x - 2],
    [snake_y, snake_x - 3],
    [snake_y, snake_x - 4],
    [snake_y, snake_x - 5]  # - the coordinates of tail
]

board.addch(snake[0][0], snake[0][1], '+')
main_scr.refresh()

""" put the first food spot on the board """
food_y = int(height / 2)
food_x = int(width / 2)
food_pos = [food_y, food_x]
board.addch(food_pos[0], food_pos[1], '$')  # initial the first coordinates of food using painting *
main_scr.refresh()
""" main process of the game """
key = curses.KEY_RIGHT  # set the default direction of the snake

while True:
    # 0. get command from user to control the snake
    next_key = board.getch()  # waiting for getting input from keyboard
    if next_key != -1:  # successfully received from keyboard
        if key == curses.KEY_RIGHT and next_key != curses.KEY_LEFT \
                or key == curses.KEY_LEFT and next_key != curses.KEY_RIGHT \
                or key == curses.KEY_UP and next_key != curses.KEY_DOWN \
                or key == curses.KEY_DOWN and next_key != curses.KEY_UP:
            key = next_key

    # 1. check whether the snake is alive
    if snake[0][0] in [0, height] or snake[0][1] in [0, width] or snake[0] in snake[1:]:  # cases for ending game
        main_scr.keypad(0)  # reset the terminal
        curses.echo()
        curses.nocbreak()
        curses.endwin()     # close the terminal
        quit()

    # 2. draw a new head of the snake and concatenate it into the previous snake body
    snake_y = snake[0][0]
    snake_x = snake[0][1]
    if key == curses.KEY_RIGHT:  # move to right
        snake_x += 1
    if key == curses.KEY_LEFT:  # move to left
        snake_x -= 1
    if key == curses.KEY_UP:  # move to up
        snake_y -= 1
    if key == curses.KEY_DOWN:  # move to down
        snake_y += 1
    snake.insert(0, [snake_y, snake_x])  # put the new head of snake in the list

    # 3. check whether the food is eaten by the snake
    if snake[0] == food_pos:    # 3.1 eat the food
        food_pos = None
        while not food_pos:     # create a new food randomly
            food_y = random.randint(1, height - 1)
            food_x = random.randint(1, width - 1)
            food_pos = [food_y, food_x]
            if food_pos not in snake:   # in case of the new coordinate is not in the snake body
                board.addch(food_pos[0], food_pos[1], '$')
            else:
                food_pos = None
    else:   # 3.2 not eat the food, pop the old tail since we insert a new head in the header
        tail = snake.pop()
        board.addch(tail[0], tail[1], ' ')

    # 4. draw the new head on screen
    board.addch(snake[0][0], snake[0][1], '+')
    main_scr.refresh()