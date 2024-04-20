import pygame
from pygame.locals import *
import random
import Objects

def move(balls: list) -> None:
    for b in balls:
        if b.dr == 0:
            if b.y <= 0:
                b.dr = 1
            else:
                b.y -= b.speed
        if b.dr == 1:
            if b.y >= 1200 - b.w:
                b.dr = 0
            else:
                b.y += b.speed
        if b.dr == 2:
            if b.x <= 0:
                b.dr = 3
            else:
                b.x -= b.speed
        if b.dr == 3:
            if b.x >= 900 - b.h:
                b.dr = 2
            else:
                b.x += b.speed

def generate_obstacles(pl: Objects.Player, balls: list) -> None:
    if random.randint(1, 60) == 1:
        w = random.randint(5, 50)
        h = random.randint(5, 50)
        fl = random.randint(0, 1)
        if fl:
            newball = Objects.Obstacle(random.choice([0, 1200 - w]), random.randint(0, 900 - h), w, h, random.randint(3, 10), random.randint(0, 3))
            balls.append(newball)
        else:
            newball = Objects.Obstacle(random.randint(0, 1200 - w), random.choice([0, 900 - h]), w, h, random.randint(3, 10), random.randint(0, 3))
            balls.append(newball)
        w = random.randint(5, 50)
        h = random.randint(5, 50)
        fl = random.randint(0, 1)
        if fl:
            newball = Objects.Obstacle(random.choice([0, 1200 - w]), pl.x, w, h, 3, random.randint(0, 3))
            balls.append(newball)
        else:
            newball = Objects.Obstacle(pl.y, random.choice([0, 900 - h]), w, h, 3, random.randint(0, 3))
            balls.append(newball)

def check_collisions(pl: Objects.Player, balls: list) -> bool:
    for b in balls:
        if pygame.Rect.colliderect(Rect(pl.y, pl.x, 30, 30), Rect(b.y, b.x, b.w, b.h)):
            return False
    return True
