# Import a library of functions called 'pygame'
import time

import pygame

# Initialize the game engine
pygame.init()

# Define the colors we will use in RGB format
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 200)
GREEN = (0, 200, 0)
BRI_GREEN = (100, 255, 100)
RED = (255, 0, 0)
BRI_RED = (255, 100, 100)
GREY = (100, 100, 100)
# Set the height and width of the screen
size = height, width = 800, 600
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Example code for the draw module")
pygame.display.update()

pygame.mixer.init()
bgm = pygame.mixer.Sound("bgm_2.wav")


def play_bgm():
    bgm.play(-1)


def stop_bgm():
    bgm.stop()


def game_intro(play=None, stop=None):
    intro = True
    refreshing = pygame.time.Clock()
    while intro:
        refreshing.tick(10)
        screen.fill(WHITE)
        for event in pygame.event.get():
            print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        # set background font and put it on the screen
        font = pygame.font.SysFont("arial", 36)
        text = font.render("Hello", True, BLACK)
        screen.blit(text, (170, 270))

        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        if 150 <= mouse[0] <= 250 and 450 <= mouse[1] <= 500:
            pygame.draw.rect(screen, BRI_GREEN, (150, 450, 100, 50))
            pygame.draw.rect(screen, GREY, (150, 450, 100, 50), 2)

            if click[0] == 1 and play:
                print("click the play button")
                play()
        else:
            pygame.draw.rect(screen, GREEN, (150, 450, 100, 50))
            pygame.draw.rect(screen, GREY, (150, 450, 100, 50), 2)

        if 550 <= mouse[0] <= 650 and 450 <= mouse[1] <= 500:
            pygame.draw.rect(screen, BRI_RED, (550, 450, 100, 50))
            pygame.draw.rect(screen, GREY, (550, 450, 100, 50), 2)

            if click[0] == 1 and stop:
                print("click the stop button")
                stop()
        else:
            pygame.draw.rect(screen, RED, (550, 450, 100, 50))
            pygame.draw.rect(screen, GREY, (550, 450, 100, 50), 2)

        start_font = font.render("Play", True, WHITE)
        quit_font = font.render("Pause", True, BLACK)
        screen.blit(start_font, (175, 463))
        screen.blit(quit_font, (575, 463))
        # update the screen
        pygame.display.update()


def main_part():
    # Loop until the user clicks the close button.
    done = False
    clock = pygame.time.Clock()
    # bgm_file = "background.wav"
    # pygame.mixer.init()
    # bgm = pygame.mixer.Sound(bgm_file)
    # bgm.play()
    #     # pygame.mixer_music.load(bgm)
    #     # pygame.mixer_music.play()
    while not done:

        # This limits the while loop to a max of 10 times per second.
        # Leave this out and we will use all CPU we can.
        clock.tick(1)

        for event in pygame.event.get():  # User did something
            if event.type == pygame.QUIT:  # If user clicked close
                done = True  # Flag that we are done so we exit this loop

        # All drawing code happens after the for loop and but
        # inside the main while done==False loop.

        # Clear the screen and set the screen background
        screen.fill(WHITE)

        # Draw on the screen a GREEN line from (0,0) to (50.75)
        # 5 pixels wide.
        pygame.draw.line(screen, GREEN, [0, 0], [50, 30], 5)

        # Draw on the screen a GREEN line from (0,0) to (50.75)
        # 5 pixels wide.
        pygame.draw.lines(screen, BLACK, False, [[0, 80], [50, 90], [200, 80], [220, 30]], 5)

        # Draw on the screen a GREEN line from (0,0) to (50.75)
        # 5 pixels wide.
        pygame.draw.aaline(screen, GREEN, [0, 50], [50, 80], True)

        # Draw a rectangle outline
        pygame.draw.rect(screen, BLACK, [75, 10, 50, 20], 2)

        # Draw a solid rectangle
        pygame.draw.rect(screen, BLACK, [150, 10, 50, 20])

        # Draw an ellipse outline, using a rectangle as the outside boundaries
        pygame.draw.ellipse(screen, RED, [225, 10, 50, 20], 2)

        # Draw an solid ellipse, using a rectangle as the outside boundaries
        pygame.draw.ellipse(screen, RED, [300, 10, 50, 20])

        # This draws a triangle using the polygon command
        pygame.draw.polygon(screen, BLACK, [[100, 100], [0, 200], [200, 200]], 5)

        # Draw an arc as part of an ellipse.
        # Use radians to determine what angle to draw.
        # pygame.draw.arc(screen, BLACK, [210, 75, 150, 125], 0, pi / 2, 2)
        # pygame.draw.arc(screen, GREEN, [210, 75, 150, 125], pi / 2, pi, 2)
        # pygame.draw.arc(screen, BLUE, [210, 75, 150, 125], pi, 3 * pi / 2, 2)
        # pygame.draw.arc(screen, RED, [210, 75, 150, 125], 3 * pi / 2, 2 * pi, 2)

        # Draw a circle
        pygame.draw.circle(screen, BLUE, [60, 250], 40)

        # Go ahead and update the screen with what we've drawn.
        # This MUST happen after all the other drawing commands.
        pygame.display.flip()

    # Be IDLE friendly
    pygame.quit()


if __name__ == '__main__':
    game_intro(play_bgm, stop_bgm)
    # main_part()
