import pygame
import sys

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Four-Way Intersection with Traffic Lights")

WHITE = (255, 255, 255)
GRAY = (169, 169, 169)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)

GREEN_TIME_NS = 7 * 1000  
YELLOW_TIME_NS = 3 * 1000 
RED_TIME_NS = 7 * 1000  
YELLOW_TIME_SN = 3 * 1000  

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill(WHITE)
    
    pygame.draw.rect(screen, GRAY, (0, HEIGHT // 2 - 50, WIDTH, 100)) 
    pygame.draw.line(screen, WHITE, (0, HEIGHT // 2), (WIDTH, HEIGHT // 2), 5)
    
    pygame.draw.rect(screen, GRAY, (WIDTH // 2 - 50, 0, 100, HEIGHT))
    pygame.draw.line(screen, WHITE, (WIDTH // 2, 0), (WIDTH // 2, HEIGHT), 5)
    
    current_time = pygame.time.get_ticks()
    state_time = current_time % (GREEN_TIME_NS + YELLOW_TIME_NS + RED_TIME_NS + YELLOW_TIME_SN)
    
    if state_time < GREEN_TIME_NS:
        pygame.draw.circle(screen, GREEN, (WIDTH // 2, HEIGHT // 4), 20)
        pygame.draw.circle(screen, GREEN, (WIDTH // 2, 3 * HEIGHT // 4), 20)
        pygame.draw.circle(screen, RED, (WIDTH // 4, HEIGHT // 2), 20)
        pygame.draw.circle(screen, RED, (3 * WIDTH // 4, HEIGHT // 2), 20)
    elif state_time < GREEN_TIME_NS + YELLOW_TIME_NS:
        pygame.draw.circle(screen, YELLOW, (WIDTH // 2, HEIGHT // 4), 20)
        pygame.draw.circle(screen, YELLOW, (WIDTH // 2, 3 * HEIGHT // 4), 20)
        pygame.draw.circle(screen, RED, (WIDTH // 4, HEIGHT // 2), 20)
        pygame.draw.circle(screen, RED, (3 * WIDTH // 4, HEIGHT // 2), 20)
    elif state_time < GREEN_TIME_NS + YELLOW_TIME_NS + RED_TIME_NS:
        pygame.draw.circle(screen, RED, (WIDTH // 2, HEIGHT // 4), 20)
        pygame.draw.circle(screen, RED, (WIDTH // 2, 3 * HEIGHT // 4), 20)
        pygame.draw.circle(screen, GREEN, (WIDTH // 4, HEIGHT // 2), 20)
        pygame.draw.circle(screen, GREEN, (3 * WIDTH // 4, HEIGHT // 2), 20)
    else:  
        pygame.draw.circle(screen, RED, (WIDTH // 2, HEIGHT // 4), 20)
        pygame.draw.circle(screen, RED, (WIDTH // 2, 3 * HEIGHT // 4), 20)
        pygame.draw.circle(screen, YELLOW, (WIDTH // 4, HEIGHT // 2), 20)
        pygame.draw.circle(screen, YELLOW, (3 * WIDTH // 4, HEIGHT // 2), 20)
    
    pygame.display.flip()
