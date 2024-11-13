from random import randint
from math import sqrt
import pygame


# Constants
W, H = 800, 600
FPS = 60
N_SHEEP = 20


# Game vars
sheeps = [
  [
    [int(randint(W * 0.1, W * 0.9)), randint(H * 0.1, H * 0.9)], # pos
    [0, 0] # speed
  ]
  for i in range(N_SHEEP)
]
mouse_x, mouse_y = 0, 0


# Pygame vars
screen = pygame.display.set_mode((W, H))
clock = pygame.time.Clock()


def move_sheeps():
  # Contact with other sheeps
  for i, sheep in enumerate(sheeps):
    pos = sheep[0]
    speed = sheep[1]

    for j, other in enumerate(sheeps):
      if 1: 
        dx = pos[0] - other[0][0]
        dy = pos[1] - other[0][1]
        d = sqrt(dx ** 2 + dy ** 2)

        if d > 70:
          speed[0] -= dx * 0.001
          speed[1] -= dy * 0.001
        if d < 30:
          speed[0] += dx * 0.1
          speed[1] += dy * 0.1

  # Contact with mouse
  for sheep in sheeps:
    ...

  # Move sheeps
  for sheep in sheeps:
    pos = sheep[0]
    speed = sheep[1]
        
    speed[0] *= 0.1
    speed[1] *= 0.1

    pos[0] += speed[0]
    pos[1] += speed[1]


def draw_sheeps():
  for i, sheep in enumerate(sheeps):
    pos = sheep[0]
    c = 200 + 55 * i / len(sheeps)
    c = int(c)
    pygame.draw.circle(screen, (c, c, c), (pos[0], pos[1]), 10)


# Gave loop
while True:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      exit()
  
  # Logic
  mouse_x, mouse_y = pygame.mouse.get_pos()

  move_sheeps()

  # Draw
  screen.fill((0, 161, 43))
  draw_sheeps()

  pygame.display.flip()
  clock.tick(FPS)