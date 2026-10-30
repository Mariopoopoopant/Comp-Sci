import pygame
import math
import random
pygame.init()

WIDTH = 1000
HEIGHT = 600
SIZE = (WIDTH, HEIGHT)

screen = pygame.display.set_mode(SIZE)
clock = pygame.time.Clock()

# ---------------------------
# Initialize global variables

cloud_color1 = (240, 240, 240)
cloud_color2 = (220, 223, 230)

moon_x = 0
moon_y = 0

# First Cloud Base Coords
cloud_x1 = 135
cloud_y1 = 90

# Second Cloud Base Coords
cloud_x2 = 701
cloud_y2 = 150

# Day and Night Colour

day_sky = (135, 206, 235)
night_sky = (20, 24, 82)

# Star Cords Random Integer


# stars_list = [] # Create the star list
# for n in range(1, 20):
#      x = random.randint(10, 976)
#      y = random.randint(10, 210)

#      stars_list.append((x,y))

# print(stars_list) 

# Star 1
star_points1 = [(60, 30), (63, 37), (70, 40), (63, 43), (60, 50), (57, 43), (50, 40), (57, 37)]

# Star 2
star_points2 = [(180, 140), (183, 147), (190, 150), (183, 153), (180, 160), (177, 153), (170, 150), (177, 147)]

# Star 3
star_points3 = [(290, 50), (293, 57), (300, 60), (293, 63), (290, 70), (287, 63), (280, 60), (287, 57)]

# Star 4
star_points4 = [(380, 170), (383, 177), (390, 180), (383, 183), (380, 190), (377, 183), (370, 180), (377, 177)]

# Star 5
star_points5 = [(620, 30), (623, 37), (630, 40), (623, 43), (620, 50), (617, 43), (610, 40), (617, 37)]

# Star 6
star_points6 = [(700, 160), (703, 167), (710, 170), (703, 173), (700, 180), (697, 173), (690, 170), (697, 167)]

# Star 7
star_points7 = [(850, 60), (853, 67), (860, 70), (853, 73), (850, 80), (847, 73), (840, 70), (847, 67)]

# Star 8
star_points8 = [(940, 180), (943, 187), (950, 190), (943, 193), (940, 200), (937, 193), (930, 190), (937, 187)]

# Initial cords for the rocket

rocket_x = -60
rocket_y = 300



# ---------------------------

running = True
while running:
    # EVENT HANDLING
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            print(event.pos)

    # GAME STATE UPDATES


    # Moon Distance from Sun

    distance = abs((moon_x - 30) - WIDTH / 2)
    percentage = distance / 120

    
    if percentage > 1:
        percentage = 1

    r = 20 + 115 * percentage # Adds the night sky R to the (Blue Sky R multiplied by the percentage)
    g = 24 + 182 * percentage # Adds the night sky G to the (Blue Sky G multiplied by the percentage)
    b = 82 + 153 * percentage # Adds the night sky B to the (Blue Sky B multiplied by the percentage)


    # Offset Cloud speeds to make it look cooler
    cloud_x1 += 6
    cloud_x2 += 4

    # All game math and comparisons happen here

    # Offset clouds to make it look even cooler

    if cloud_x1 > WIDTH + 30:
        cloud_x1 = 0 - 400

    if cloud_x2 > WIDTH + 30:
        cloud_x2 = 0 - 200
    


    # DRAWING


    screen.fill((int(r), int(g), int(b)))

    # Draw stars in the sky
    if percentage <= 1:

        star_r = int(255 - 120 * percentage)
        star_g = int(255 - 49 * percentage)
        star_b = int(200 + 35 * percentage)

        pygame.draw.polygon(screen, (star_r, star_g, star_b), star_points1)
        pygame.draw.polygon(screen, (star_r, star_g, star_b), star_points2)
        pygame.draw.polygon(screen, (star_r, star_g, star_b), star_points3)
        pygame.draw.polygon(screen, (star_r, star_g, star_b), star_points4)
        pygame.draw.polygon(screen, (star_r, star_g, star_b), star_points5)
        pygame.draw.polygon(screen, (star_r, star_g, star_b), star_points6)
        pygame.draw.polygon(screen, (star_r, star_g, star_b), star_points7)
        pygame.draw.polygon(screen, (star_r, star_g, star_b), star_points8)


    # Draw Moon and Sun

    pygame.draw.circle(screen, (237, 92, 78), (500, 90), 60)  # Draw the Sun
    pygame.draw.circle(screen, (144, 144, 144), (moon_x - 30, moon_y), 60) # Draw the Moon
    pygame.draw.circle(screen, (110, 110, 110), (moon_x - 30, moon_y), 60, 2)





    
    # Parabolic Motion for the Eclipse

    moon_x += 2
    moon_y = 0.000694 * (moon_x - 500) ** 2 + 90

    # print(moon_x, moon_y)

    # Resets the moon's position once it goes out of screen

    if  moon_x - 200 > WIDTH:
        moon_x = -50


    # Moon Holes/Craters

    pygame.draw.circle(screen, (115, 115, 115), (moon_x - 50, moon_y - 15), 12)
    pygame.draw.circle(screen, (115, 115, 115), (moon_x - 15, moon_y + 20), 9)
    pygame.draw.circle(screen, (115, 115, 115), (moon_x - 5, moon_y - 25), 7)
    pygame.draw.circle(screen, (115, 115, 115), (moon_x - 60, moon_y + 25), 8)
    pygame.draw.circle(screen, (115, 115, 115), (moon_x - 30, moon_y + 5), 5)
    pygame.draw.circle(screen, (115, 115, 115), (moon_x - 35, moon_y - 38), 6)




    # Mountain

        # Back mountains
    pygame.draw.polygon(screen, (95, 105, 135),
        [(0, 400), (100, 330), (200, 390), (290, 270), (390, 380), (470, 340),
         (620, 380), (670, 280), (760, 370), (860, 330), (1000, 400),
         (1000, 600), (0, 600)])

        # Snow Caps
    pygame.draw.polygon(screen, (245, 247, 250),
        [(290, 270), (272, 298), (282, 293), (290, 303), (299, 293), (309, 298)])
    pygame.draw.polygon(screen, (245, 247, 250),
        [(670, 280), (657, 310), (664, 304), (670, 313), (677, 304), (695, 310)])
    pygame.draw.polygon(screen, (245, 247, 250),
        [(100, 330), (88, 349), (95, 345), (100, 353), (106, 345), (113, 349)])
    pygame.draw.polygon(screen, (245, 247, 250),
        [(860, 330), (848, 349), (855, 345), (860, 353), (866, 345), (800, 349)])

    # Building if statements yk

    if percentage < 1:
        window_color = (255, 225, 120)
    else:
        window_color = (110, 140, 165)




     # Building 1

    pygame.draw.rect(screen, (163, 165, 163), (0, 334, 178, 334 ))
    pygame.draw.rect(screen, (95, 97, 105), (0, 324, 188, 15))

    # Window 1
    pygame.draw.rect(screen, window_color, (25, 360, 40, 45))
    pygame.draw.rect(screen, window_color, (110, 360, 40, 45))

    pygame.draw.rect(screen, window_color, (25, 440, 40, 45))
    pygame.draw.rect(screen, window_color, (110, 440, 40, 45))

    pygame.draw.rect(screen, window_color, (25, 520, 40, 45))
    pygame.draw.rect(screen, window_color, (110, 520, 40, 45))

    # Chimney 1
    pygame.draw.rect(screen, (120, 60, 55), (10, 292, 20, 32))    
    pygame.draw.rect(screen, (90, 45, 42), (6, 288, 28, 5))            

    # Building 2
    pygame.draw.rect(screen, (130, 135, 145), (390, 290, 220, 310))   # main body
    pygame.draw.rect(screen, (95, 97, 105), (380, 280, 240, 15))

    # Window 2
    # start?
    # end?
    # up by?

    x = 415
    x_dist = 67
    y = 250
    y_dist = 65
    for ny in range(0, 4):
        pygame.draw.rect(screen, window_color, (x, y + y_dist, 36, 40))
        y = y_dist + y
        ny + 1
        for nx in range(0, 2):
            pygame.draw.rect(screen, window_color,(x + x_dist, y, 36, 40 ))
            nx + 1
            x = x_dist + x
        x = 415
    # pygame.draw.rect(screen, window_color, (415, 315, 36, 40))
    # pygame.draw.rect(screen, window_color, (482, 315, 36, 40))
    # pygame.draw.rect(screen, window_color, (549, 315, 36, 40))

    # pygame.draw.rect(screen, window_color, (415, 375, 36, 40))
    # pygame.draw.rect(screen, window_color, (482, 375, 36, 40))
    # pygame.draw.rect(screen, window_color, (549, 375, 36, 40))

    # pygame.draw.rect(screen, window_color, (415, 435, 36, 40))
    # pygame.draw.rect(screen, window_color, (482, 435, 36, 40))
    # pygame.draw.rect(screen, window_color, (549, 435, 36, 40))

    # pygame.draw.rect(screen, window_color, (415, 495, 36, 40))
    # pygame.draw.rect(screen, window_color, (482, 495, 36, 40))
    # pygame.draw.rect(screen, window_color, (549, 495, 36, 40))

    # Chimney 2

    pygame.draw.rect(screen, (95, 97, 105), (405, 250, 20, 30))     
    pygame.draw.rect(screen, (70, 72, 80), (401, 246, 28, 5))       

    pygame.draw.rect(screen, (95, 97, 105), (578, 253, 18, 27))     
    pygame.draw.rect(screen, (70, 72, 80), (574, 249, 26, 5))         

    # Building 3
    pygame.draw.rect(screen, (163, 165, 163), (756, 254, 400, 756))
    pygame.draw.rect(screen, (95, 97, 105), (746, 244, 264, 15))


    # Window 3

    pygame.draw.rect(screen, window_color, (780, 285, 40, 45))
    pygame.draw.rect(screen, window_color, (850, 285, 40, 45))
    pygame.draw.rect(screen, window_color, (920, 285, 40, 45))

    pygame.draw.rect(screen, window_color, (780, 365, 40, 45))
    pygame.draw.rect(screen, window_color, (850, 365, 40, 45))
    pygame.draw.rect(screen, window_color, (920, 365, 40, 45))

    pygame.draw.rect(screen, window_color, (780, 445, 40, 45))
    pygame.draw.rect(screen, window_color, (850, 445, 40, 45))
    pygame.draw.rect(screen, window_color, (920, 445, 40, 45))

    pygame.draw.rect(screen, window_color, (780, 525, 40, 45))
    pygame.draw.rect(screen, window_color, (850, 525, 40, 45))
    pygame.draw.rect(screen, window_color, (920, 525, 40, 45))




    # Cloud 1

    pygame.draw.circle(screen, cloud_color1, (cloud_x1, cloud_y1), 30)
    pygame.draw.circle(screen, cloud_color1, (cloud_x1 + 30, cloud_y1 - 20), 35)
    pygame.draw.circle(screen, cloud_color1, (cloud_x1 + 65, cloud_y1 - 30), 40)
    pygame.draw.circle(screen, cloud_color1, (cloud_x1 + 100, cloud_y1 - 15), 30)
    pygame.draw.circle(screen, cloud_color1, (cloud_x1 + 125, cloud_y1), 25)
    pygame.draw.rect(screen, cloud_color1, (cloud_x1 - 16, cloud_y1, 140, 25))

    # Cloud 2

    pygame.draw.circle(screen, cloud_color2, (cloud_x2, cloud_y2), 25)
    pygame.draw.circle(screen, cloud_color2, (cloud_x2 + 30, cloud_y2 - 15), 30)
    pygame.draw.circle(screen, cloud_color2, (cloud_x2 + 65, cloud_y2 - 25), 32)
    pygame.draw.circle(screen, cloud_color2, (cloud_x2 + 95, cloud_y2 - 18), 27)
    pygame.draw.circle(screen, cloud_color2, (cloud_x2 + 125, cloud_y2 - 10), 30)
    pygame.draw.circle(screen, cloud_color2, (cloud_x2 + 155, cloud_y2), 22)
    pygame.draw.rect(screen, cloud_color2, (cloud_x2 - 15, cloud_y2 - 5, 160, 25))

    # Must be the last two lines
    # of the game loop
    pygame.display.flip()
    clock.tick(30)
    #---------------------------

pygame.quit()