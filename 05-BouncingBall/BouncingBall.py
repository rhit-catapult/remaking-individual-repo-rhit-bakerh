import pygame
import sys
import random


# You will implement this module ENTIRELY ON YOUR OWN!

# TODO: Create a Ball class.
class Ball:
    def __init__(self, screen, x, y):
        self.screen = screen
        self.screen = screen
        self.x = x
        self.y = y
        self.speedy = random.randint(5, 15)
        self.speedx = random.randint(5, 15)
    def draw(self):
        pygame.draw.circle(self.screen, (247, 128, 219), (self.x, self.y), 10)
    # def change_direction(self):
    #     #print(self.speed)
    #     self.speed = -self.speed
        #print("Changing direction", self.speed)
    # def move(self):

    def bounce(self):
        self.y += self.speedy
        self.x += self.speedx
        self.bottom_border()
        self.top_border()
        self.left_border()
        self.right_border()
    def bottom_border(self):
        if self.y > self.screen.get_height():
            self.speedy = -self.speedy
    def top_border(self):
        if self.y < 0:
            self.speedy = -self.speedy
    def right_border(self):
        if self.x > self.screen.get_width():
            self.speedx = -self.speedx
    def left_border(self):
        if self.x < 0:
            self.speedx = -self.speedx

# TODO: Possible member variables: screen, color, x, y, radius, speed_x, speed_y
WHITE = pygame.Color(255, 255, 255)
BLACK = pygame.Color(0, 0, 0)
PINK = pygame.Color(247, 128, 219)
speed_x = random.randint(5, 15)
speed_y = random.randint(5, 15)


# TODO: Methods: __init__, draw, move

def main():
    pygame.init()
    screen = pygame.display.set_mode((1000, 600))
    pygame.display.set_caption('Bouncing Ball')
    screen.fill(pygame.Color('white'))
    clock = pygame.time.Clock()
    ball = Ball(screen, speed_x, speed_y)
    while True:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        screen.fill(pygame.Color('white'))

    # TODO: Create an instance of the Ball class called ball1
        # TODO: Move the ball
        # TODO: Draw the ball
        #pygame.draw.circle(screen, (PINK), (screen.get_width() // 2, screen.get_height() // 2), 15)

       #test_Ball = Ball(screen, 700, 10)
        ball.draw()
        ball.bounce()
        pygame.display.update()
        #test_Ball.draw()
        #pygame.draw.circle(screen, (247, 128, 219), (500,300), 5)

main()

# Optional challenges (if you finish and want do play a bit more):
#   After you get 1 ball working make a few balls (ball2, ball3, etc) that start in different places.
#   Make each ball a different color
#   Make the screen 1000 x 800 to allow your balls more space (what needs to change?)
#   Make the speed of each ball randomly chosen (1 to 5)
#   After you get that working try making a list of balls to have 100 balls (use a loop)!
#   Use random colors for each ball
