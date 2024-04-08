class Player(object):
    def __init__(self,y,x,speed):
        self.y = y
        self.x = x
        self.speed = speed

class Obstacle(object):
    def __init__(self,y,x,w,h,speed,dr):
        self.y = y
        self.x = x
        self.h = h
        self.w = w
        self.speed = speed
        self.dr = dr