class Player:
    def __init__(self, y: int, x: int, speed: int):
        self.y = y
        self.x = x
        self.speed = speed

class Obstacle:
    def __init__(self, y: int, x: int, w: int, h: int, speed: int, dr: int):
        self.y = y
        self.x = x
        self.h = h
        self.w = w
        self.speed = speed
        self.dr = dr