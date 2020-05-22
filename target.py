from graphics import *
from math import sqrt, sin, cos, radians, pi
from random import randrange, randint

class Target:

    def __init__(self, win):

        self.posX = randrange(0, 200)
        self.posY = randrange(0, 150)
        self.angle = radians(randrange(0, 360))
        self.vel = 1.0

        # Set initial vertices of the targets
        self.vertices = [
            Point(self.posX, self.posY),
            Point(self.posX+10, self.posY+3),
            Point(self.posX+10, self.posY+6),
            Point(self.posX+2, self.posY+9),
            Point(self.posX+5, self.posY+12),
            Point(self.posX+3, self.posY+14),
            Point(self.posX, self.posY+9),
            Point(self.posX-3, self.posY+14),
            Point(self.posX-5, self.posY+12),
            Point(self.posX-2, self.posY+9),
            Point(self.posX-8, self.posY+6),
            Point(self.posX-8,self.posY+3)
        ]
        self.marker = Polygon(self.vertices)
        self.marker.setOutline('white')
        self.marker.draw(win)

    def update(self):
        """Every second move the target 
        in the direction of set angle"""
        dx = self.vel*cos(self.angle)
        dy = self.vel*sin(self.angle)

        # Update posX and posY
        self.posX += dx
        self.posY += dy

        self.marker.move(dx, dy)
    
    def getX(self):
        return self.posX
    
    def getY(self):
        return self.posY+4.5
        
    def undraw(self):
        self.marker.undraw()
