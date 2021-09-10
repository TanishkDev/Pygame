# Importing Modules
import pygame
import time
import sys
import random

# FPS FOR THE GAME
FPS = 30

# Width and height for the game
WIDTH, HEIGHT = 600, 600

# Colors for the game
LIME = (0, 245, 8)
BLUE = (7, 111, 230)
RED = (255, 0, 0)
WHITE = (200, 200, 200)
BLACK = (0, 0, 0)

# Snake Class


class Snake():
    def __init__(self, parent_screen):  # Ask for the parent screen or the main screen
        self.parent_screen = parent_screen  # intializing the screen
        self.snake_x = WIDTH / 2
        self.snake_y = HEIGHT / 2
        self.score = 0
        self.snake_velocity_x = 0
        self.snake_velocity_y = 0
        self.speed = 5
        self.snake_pixels = []
        self.size = 10
        self.snake_length = 1
        self.score_font = pygame.font.SysFont('Fira_Code', 20)
        # Draw the snake rectangle
        # Call the food class and the make food obj
        self.food = Food(self.parent_screen)
        self.draw()
        # Return the foods postion in term of x and y
        self.food_x, self.food_y = self.food.returnFood()

    # Draw Fucntion()
    def draw(self):  # FIXME maybe here
        # Fill the background to lime again but don't know why
        self.parent_screen.fill((LIME))
        self.showScore()
        self.drawSnake()
        self.food.draw()  # Draw the food
        pygame.display.update()  # Uptades display

    def drawSnake(self):  # FIXME Problem is here fix it
        for pixel in self.snake_pixels:
            pygame.draw.rect(self.parent_screen, BLUE, [
                             pixel[0], pixel[1], self.size, self.size])

    def walk(self):  # walk function

        self.snake_x += self.snake_velocity_x  # snake vel_x
        self.snake_y += self.snake_velocity_y  # snake vel_y

        self.snake_pixels.append([self.snake_x, self.snake_y])
        if len(self.snake_pixels) > self.snake_length:
            del self.snake_pixels[0]

        self.draw()  # draw snake wiht new x and y

    def isCollision(self):  # check the collison
        if self.snake_x >= WIDTH or self.snake_x < 0 or self.snake_y >= HEIGHT or self.snake_y < 0:
            sys.exit()
        if self.food_x == self.snake_x or self.food_y == self.snake_y:
            self.food.changeXY()
            self.food_x, self.food_y = self.food.returnFood()
            self.snake_length += 1
            self.score += 1

        # Food class
    def showScore(self):
        self.show = self.score_font.render(
            "Score"+str(self.score), True, BLACK)
        self.parent_screen.blit(self.show, [0, 0])


class Food:
    def __init__(self, parent_screen):  # Ask for the parent screen or the main screen
        # randomly deceise food x
        self.food_x = round(random.randrange(0, WIDTH - 10) / 10.0) * 10.0
        self.food_y = round(random.randrange(
            0, HEIGHT-10) / 10.0) * 10.0  # and food y
        self.parent_screen = parent_screen

    def draw(self):  # draw function
        pygame.draw.rect(self.parent_screen, (RED), [
            self.food_x, self.food_y, 10, 10])  # Draw a rectangle of red col and size of 20 and 20 pix.

    def changeXY(self):  # change xy
        self.food_x = round(random.randrange(0, WIDTH - 10) / 10.0) * 10.0
        self.food_y = round(random.randrange(0, HEIGHT-10) /
                            10.0) * 10.0  # change between 0 to 600

    def returnFood(self):  # return the food
        return self.food_x, self.food_y  # returns snake class x and y

    def placeFood(self):
        self.draw()


# Main game class controls the game fundamentals and loops
class Game:

    def __init__(self):
        pygame.init()
        # Initialize a clock in game allows you to control you fps
        self.clock = pygame.time.Clock()
        self.surface = pygame.display.set_mode(
            (WIDTH, HEIGHT))  # Set the display
        self.surface.fill((LIME))  # Set the background to lime
        pygame.display.set_caption("Snake")  # Set the game title to snake
        # Call the snake class and make the snake objects
        self.snake = Snake(self.surface)
        # self.snake.drawGrid()
        # self.snake.draw()  # Call the draw function that draws the snake on the screen

    def run(self):  # main loop run the games
        running = True
        while running:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:  # Quits
                    pygame.quit()
                    running = False
                    sys.exit()

                if event.type == pygame.KEYDOWN:  # Trigers the keypress
                    if event.key == pygame.K_UP:  # If up function from snake class

                        self.snake.snake_velocity_y -= 2
                        self.snake.snake_velocity_x = 0

                    if event.key == pygame.K_DOWN:  # If down function from snake class

                        self.snake.snake_velocity_y += 2
                        self.snake.snake_velocity_x = 0
                    if event.key == pygame.K_RIGHT:  # If right
                        self.snake.snake_velocity_x += 2
                        self.snake.snake_velocity_y = 0

                    if event.key == pygame.K_LEFT:  # If left

                        self.snake.snake_velocity_x -= 2
                        self.snake.snake_velocity_y = 0
                    if event.key == pygame.K_ESCAPE:  # If escape , quits the game
                        pygame.quit()
                        running = False
                        sys.exit()
            self.snake.isCollision()
            self.snake.walk()  # Calls the walk from snake class
            self.clock.tick(FPS)  # FPS = 30


# Main run game
# Using Game() class and run the game using game.run()
if __name__ == '__main__':
    game = Game()
    game.run()
 # Problem is that snake is not extending or snake isn't drawing as I was expected
