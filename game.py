import pygame
import sys
import random

pygame.init()
WIDTH = 1920
HEIGHT = 600

YELLOW = (255, 255, 0)
LIGHT_BLUE = (0, 255, 255)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

class Cube:
    def __init__(self, x, y, width, height, velocity):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.velocity = velocity
        self.direction = ""

    def draw(self, screen):
        pygame.draw.rect(screen, YELLOW, (self.x, self.y, self.width, self.height))

def move_cube(cube):

    direction = random.choice(["left", "right"])
    if direction == "left":
        cube.x -= cube.velocity
    elif direction == "right":
        cube.x += cube.velocity

    # Границы экрана
    cube.x = max(0, min(cube.x, WIDTH - cube.width))
    cube.y = max(0, min(cube.y, HEIGHT - cube.height))

cube1 = Cube(WIDTH // 2 - 50, HEIGHT // 2 + 150, 100, 50, 5)
cube2 = Cube(WIDTH // 2 - 50, HEIGHT // 2 - 150, 100, 50, 5)

MOVE_CUBE1 = pygame.USEREVENT + 1
MOVE_CUBE2 = pygame.USEREVENT + 2
pygame.time.set_timer(MOVE_CUBE1, 200)  
pygame.time.set_timer(MOVE_CUBE2, 300)  

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == MOVE_CUBE1:
            move_cube(cube1)
        elif event.type == MOVE_CUBE2:
            move_cube(cube2)

    screen.fill(LIGHT_BLUE)
    cube1.draw(screen)
    cube2.draw(screen)

    pygame.display.flip()
    clock.tick(60)
