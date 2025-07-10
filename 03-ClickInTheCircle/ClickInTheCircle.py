import pygame, sys
import math


def distance(point1, point2):
    point1_x = point1[0]
    point2_x = point2[0]
    point1_y = point1[1]
    point2_y = point2[1]

    # TODO 4: Return the actual distance between point 1 and point 2.
    #  Hint: you will need the math library for the sqrt function.
    #       distance = sqrt(   (delta x) ** 2 + (delta y) ** 2  )
    distance = math.sqrt((point1_x - point2_x)**2 + (point1_y - point2_y)**2)
    return distance


def main():
    pygame.init()
    screen = pygame.display.set_mode((400, 400))
    pygame.display.set_caption("Mouse click positions")
    font = pygame.font.Font(None, 25)
    WHITE = pygame.Color(250, 250, 250)

    # TODO 8: Load the "drums.wav" file into the pygame music mixer
    pygame.mixer.music.load("drums.wav")

    instruction_text = 'Click in the circle'
    text_color = (222, 222, 0)
    instructions_image = font.render(instruction_text, True, text_color)

    circle1_color = (247, 128, 219)
    circle1_center = (screen.get_width() // 2, screen.get_height() // 2)
    circle2_center = (screen.get_width() // 4, screen.get_height() // 4)
    circle_radius = 50
    circle_border_width = 3
    # rect_color = (204, 108, 231)
    # rect_center = (screen.get_width() // 2, screen.get_height() // 2)
    # rect_radius = screen.get_width() // 2
    # rect_border_width = 3

    message_text = ''

    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            # TODO 2: For a MOUSEBUTTONDOWN event get the click position.
            if event.type == pygame.MOUSEBUTTONDOWN:
                # TODO 3: Determine the distance between the click position and the circle_center using the distance
                click_position = event.pos
                distance_from_circle = distance(click_position, circle1_center)
                distance_from_circle = distance(click_position, circle2_center)
                # distance_from_rect = distance(click_position, rect_center)
                # print(distance_from_circle)
                # TODO 3:   function and save the result into a variable called distance_from_circle
                if distance_from_circle < circle_radius:
                    message_text = "Bullseye!"
                    # pygame.mixer.music.play(-1)
                else:
                    message_text = "You missed!"
                    # pygame.mixer.music.stop()
                # TODO 5: If distance_from_circle is less than or equal to circle_radius, set message_text to 'Bullseye!'
                # TODO 5: If distance_from_circle is greater than the circle_radius, set the message_text to 'You missed!'
                # TODO 9: Start playing the music mixer looping forever if the click is within the circle
                # TODO 10: Stop playing the music if the click is outside the circle

        screen.fill(pygame.Color("Black"))

        # TODO 1: Draw the circle using the screen, circle_color, circle_center, circle_radius, and circle_border_width
        pygame.draw.circle(screen, circle1_color, circle1_center, circle_radius, circle_border_width)
        pygame.draw.circle(screen, (125, 218, 88), (333,95), circle_radius, circle_border_width)
        # pygame.draw.rect(screen, rect_color, rect_center, rect_radius, rect_border_width)

        # TODO 6: Create a text image (render the text) based on the message_text with the color (122, 237, 201)
        font2 = pygame.font.SysFont("Comic Sans MS", 45)
        caption2 = font2.render(message_text, True, text_color)

        screen.blit(instructions_image, (25, 25))
        # TODO 7: Draw (blit) the message to the user that says 'Bullseye!' or 'You missed!'
        screen.blit(caption2, (100, 40))
        pygame.display.update()


main()
