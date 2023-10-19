import pygame
import sys
import random

pygame.init()

# set display
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Four-Way Intersection with Traffic Lights and Cars")

# colors
WHITE = (255, 255, 255)
GRAY = (169, 169, 169)
LIGHT_GREY = (220, 220, 220)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
CAR_COLOR = (0, 0, 255)

# traffic light timings 
GREEN_TIME_NS = 7 * 1000
YELLOW_TIME_NS = 3 * 1000
RED_TIME_NS = 7 * 1000 
YELLOW_TIME_SN = 3 * 1000

# initlialize car variales
CAR_WIDTH, CAR_HEIGHT = 30, 20
CAR_SPEED = 2
DIRECTION = ''

# initialize pedestrian variables
PEDESTRIAN_COLOR = (128, 0, 128)  # Purple color for pedestrians
PEDESTRIAN_WIDTH, PEDESTRIAN_HEIGHT = 10, 20
PEDESTRIAN_SPEED = 1
PEDESTRIAN_DIRECTION = ''

class Car:
    def __init__(self, x, y, color, speed=CAR_SPEED, direction=DIRECTION):
        self.rect = pygame.Rect(x, y, CAR_WIDTH, CAR_HEIGHT)
        self.color = color
        self.speed = speed
        self.direction = direction

    def move(self):
        if self.direction == 'Vertical':
            self.rect.y += self.speed
        elif self.direction == 'Horizontal':
            self.rect.x += self.speed
    
    def draw(self):
        pygame.draw.rect(screen, self.color, self.rect)

class Pedestrian:
    def __init__(self, x, y, color, speed=PEDESTRIAN_SPEED, direction=PEDESTRIAN_DIRECTION):
        self.rect = pygame.Rect(x, y, PEDESTRIAN_WIDTH, PEDESTRIAN_HEIGHT)
        self.color = color
        self.speed = speed
        self.direction = direction

    def move(self):
        if self.direction == 'Vertical':
            self.rect.y += self.speed
        elif self.direction == 'Horizontal':
            self.rect.x += self.speed

    def draw(self):
        pygame.draw.rect(screen, self.color, self.rect)


cars = []
pedestrians = []

# white main loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # clear screen
    screen.fill(WHITE)

    # draw horizontal road
    pygame.draw.rect(screen, GRAY, (0, HEIGHT // 2 - 50, WIDTH, 100))
    pygame.draw.line(screen, WHITE, (0, HEIGHT // 2), (WIDTH, HEIGHT // 2), 5)
    
    # dar vertical road
    pygame.draw.rect(screen, GRAY, (WIDTH // 2 - 50, 0, 100, HEIGHT))
    pygame.draw.line(screen, WHITE, (WIDTH // 2, 0), (WIDTH // 2, HEIGHT), 5)

    # west vertical crosswalk 
    pygame.draw.rect(screen, WHITE, (WIDTH // 2 - 75, HEIGHT // 2 - 45, 20, 90)) 
    # east vertical crosswalk
    pygame.draw.rect(screen, WHITE, (WIDTH // 2 + 55, HEIGHT // 2 - 45, 20, 90))

    # north horizontal crosswalk
    pygame.draw.rect(screen, WHITE, (WIDTH // 2 - 37 , HEIGHT // 2 - 80, 75, 20))
    # south horizontal crosswalk
    pygame.draw.rect(screen, WHITE, (WIDTH // 2 - 37, HEIGHT // 2 + 55, 75, 20))

    # traffic light logic
    current_time = pygame.time.get_ticks()
    state_time = current_time % (GREEN_TIME_NS + YELLOW_TIME_NS + RED_TIME_NS + YELLOW_TIME_SN)
    
    # green for north and south | red for east and west
    if state_time < GREEN_TIME_NS:
        pygame.draw.circle(screen, GREEN, (WIDTH // 2, HEIGHT // 4), 20)
        pygame.draw.circle(screen, GREEN, (WIDTH // 2, 3 * HEIGHT // 4), 20)
        pygame.draw.circle(screen, RED, (WIDTH // 4, HEIGHT // 2), 20)
        pygame.draw.circle(screen, RED, (3 * WIDTH // 4, HEIGHT // 2), 20)

        # horizontal crosswalks read stop
        pygame.draw.circle(screen, RED, (WIDTH // 2 - 50, HEIGHT // 2 - 85), 10)
        pygame.draw.circle(screen, RED, (WIDTH // 2 + 50, HEIGHT // 2 - 85), 10)
        pygame.draw.circle(screen, RED, (WIDTH // 2 - 50, HEIGHT // 2 + 80), 10)
        pygame.draw.circle(screen, RED, (WIDTH // 2 + 50, HEIGHT // 2 + 80), 10)

        # vertical crosswalks read walk
        pygame.draw.circle(screen, LIGHT_GREY, (WIDTH // 2 - 75, HEIGHT // 2 - 60), 10)
        pygame.draw.circle(screen, LIGHT_GREY, (WIDTH // 2 - 75, HEIGHT // 2 + 60), 10)
        pygame.draw.circle(screen, LIGHT_GREY, (WIDTH // 2 + 75, HEIGHT // 2 - 60), 10)
        pygame.draw.circle(screen, LIGHT_GREY, (WIDTH // 2 + 75, HEIGHT // 2 + 60), 10)


        CAR_WIDTH, CAR_HEIGHT = 20, 30 # reinitialization of car dimensions
        # random spawn of cars traveling vertically
        if random.randint(1, 100) < 2:
            cars.append(Car(WIDTH // 2.22,  -CAR_HEIGHT, CAR_COLOR, CAR_SPEED, 'Vertical'))
        if random.randint(1, 100) < 2:
            cars.append(Car(WIDTH // 1.95, HEIGHT, CAR_COLOR, -CAR_SPEED, 'Vertical'))

        # random spawn of pedestrains traveling vertically on both crosswalks
        if random.randint(1, 100) < 2:
            cars.append(Pedestrian(WIDTH // 1.75,  -PEDESTRIAN_HEIGHT, PEDESTRIAN_COLOR, PEDESTRIAN_SPEED, 'Vertical'))
        if random.randint(1, 100) < 2:
            cars.append(Pedestrian(WIDTH // 1.72, HEIGHT, PEDESTRIAN_COLOR, -PEDESTRIAN_SPEED, 'Vertical'))
        if random.randint(1, 100) < 2:
            cars.append(Pedestrian(WIDTH // 2.45,  -PEDESTRIAN_HEIGHT, PEDESTRIAN_COLOR, PEDESTRIAN_SPEED, 'Vertical'))
        if random.randint(1, 100) < 2:
            cars.append(Pedestrian(WIDTH // 2.42, HEIGHT, PEDESTRIAN_COLOR, -PEDESTRIAN_SPEED, 'Vertical'))

    # yellow for north and south | red for east and west
    elif state_time < GREEN_TIME_NS + YELLOW_TIME_NS:
        pygame.draw.circle(screen, YELLOW, (WIDTH // 2, HEIGHT // 4), 20)
        pygame.draw.circle(screen, YELLOW, (WIDTH // 2, 3 * HEIGHT // 4), 20)
        pygame.draw.circle(screen, RED, (WIDTH // 4, HEIGHT // 2), 20)
        pygame.draw.circle(screen, RED, (3 * WIDTH // 4, HEIGHT // 2), 20) 

        # horizontal corsswalks read stop
        pygame.draw.circle(screen, RED, (WIDTH // 2 - 50, HEIGHT // 2 - 85), 10)
        pygame.draw.circle(screen, RED, (WIDTH // 2 + 50, HEIGHT // 2 - 85), 10)
        pygame.draw.circle(screen, RED, (WIDTH // 2 - 50, HEIGHT // 2 + 80), 10)
        pygame.draw.circle(screen, RED, (WIDTH // 2 + 50, HEIGHT // 2 + 80), 10)

        # vertical corsswalks read stop
        pygame.draw.circle(screen, RED, (WIDTH // 2 - 75, HEIGHT // 2 - 60), 10)
        pygame.draw.circle(screen, RED, (WIDTH // 2 - 75, HEIGHT // 2 + 60), 10)
        pygame.draw.circle(screen, RED, (WIDTH // 2 + 75, HEIGHT // 2 - 60), 10)
        pygame.draw.circle(screen, RED, (WIDTH // 2 + 75, HEIGHT // 2 + 60), 10)

    # red for north and south | green for east and west
    elif state_time < GREEN_TIME_NS + YELLOW_TIME_NS + RED_TIME_NS:  
        pygame.draw.circle(screen, RED, (WIDTH // 2, HEIGHT // 4), 20)  
        pygame.draw.circle(screen, RED, (WIDTH // 2, 3 * HEIGHT // 4), 20) 
        pygame.draw.circle(screen, GREEN, (WIDTH // 4, HEIGHT // 2), 20)
        pygame.draw.circle(screen, GREEN, (3 * WIDTH // 4, HEIGHT // 2), 20)

        # horizontal corsswalks read walk
        pygame.draw.circle(screen, LIGHT_GREY, (WIDTH // 2 - 50, HEIGHT // 2 - 85), 10)
        pygame.draw.circle(screen, LIGHT_GREY, (WIDTH // 2 + 50, HEIGHT // 2 - 85), 10)
        pygame.draw.circle(screen, LIGHT_GREY, (WIDTH // 2 - 50, HEIGHT // 2 + 80), 10)
        pygame.draw.circle(screen, LIGHT_GREY, (WIDTH // 2 + 50, HEIGHT // 2 + 80), 10)

        # vertical corsswalks read stop
        pygame.draw.circle(screen, RED, (WIDTH // 2 - 75, HEIGHT // 2 - 60), 10)
        pygame.draw.circle(screen, RED, (WIDTH // 2 - 75, HEIGHT // 2 + 60), 10)
        pygame.draw.circle(screen, RED, (WIDTH // 2 + 75, HEIGHT // 2 - 60), 10)
        pygame.draw.circle(screen, RED, (WIDTH // 2 + 75, HEIGHT // 2 + 60), 10)

        # fx car dimentsions
        CAR_WIDTH, CAR_HEIGHT = 30, 20
        # random spawn of cars traveling horizontally
        if random.randint(1, 100) < 2:
            cars.append(Car(WIDTH - CAR_WIDTH, HEIGHT // 2.2, CAR_COLOR, -CAR_SPEED, 'Horizontal'))  
        if random.randint(1, 100) < 2:
            cars.append(Car(CAR_WIDTH, HEIGHT // 1.9, CAR_COLOR, CAR_SPEED, 'Horizontal'))  

        # random spawn of pedestrains traveling horizontally on both crosswalks
        if random.randint(1, 100) < 2:
            cars.append(Pedestrian(WIDTH - CAR_WIDTH,  HEIGHT // 2.77, PEDESTRIAN_COLOR, -PEDESTRIAN_SPEED, 'Horizontal'))
        if random.randint(1, 100) < 2:
            cars.append(Pedestrian(CAR_WIDTH, HEIGHT // 1.72, PEDESTRIAN_COLOR, PEDESTRIAN_SPEED, 'Horizontal'))
        if random.randint(1, 100) < 2:
            cars.append(Pedestrian(WIDTH - CAR_WIDTH, HEIGHT // 1.70, PEDESTRIAN_COLOR, -PEDESTRIAN_SPEED, 'Horizontal'))
        if random.randint(1, 100) < 2:
            cars.append(Pedestrian(CAR_WIDTH,  HEIGHT // 2.75, PEDESTRIAN_COLOR, PEDESTRIAN_SPEED, 'Horizontal'))
    
    # red for north and south | yellow for east and west
    else:  
        pygame.draw.circle(screen, RED, (WIDTH // 2, HEIGHT // 4), 20) 
        pygame.draw.circle(screen, RED, (WIDTH // 2, 3 * HEIGHT // 4), 20)  
        pygame.draw.circle(screen, YELLOW, (WIDTH // 4, HEIGHT // 2), 20) 
        pygame.draw.circle(screen, YELLOW, (3 * WIDTH // 4, HEIGHT // 2), 20) 
        
        # horizontal corsswalks read stop
        pygame.draw.circle(screen, RED, (WIDTH // 2 - 50, HEIGHT // 2 - 85), 10)
        pygame.draw.circle(screen, RED, (WIDTH // 2 + 50, HEIGHT // 2 - 85), 10)
        pygame.draw.circle(screen, RED, (WIDTH // 2 - 50, HEIGHT // 2 + 80), 10)
        pygame.draw.circle(screen, RED, (WIDTH // 2 + 50, HEIGHT // 2 + 80), 10)

        # vertical corsswalks read stop
        pygame.draw.circle(screen, RED, (WIDTH // 2 - 75, HEIGHT // 2 - 60), 10)
        pygame.draw.circle(screen, RED, (WIDTH // 2 - 75, HEIGHT // 2 + 60), 10)
        pygame.draw.circle(screen, RED, (WIDTH // 2 + 75, HEIGHT // 2 - 60), 10)
        pygame.draw.circle(screen, RED, (WIDTH // 2 + 75, HEIGHT // 2 + 60), 10)

    # move and draw cars
    for car in cars:
        car.move()
        car.draw()

    # move and draw pedestrians
    for pedestrian in pedestrians:
        pedestrian.move()
        pedestrian.draw()
    
    # update display
    pygame.display.flip()
