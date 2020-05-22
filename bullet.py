from graphics import *
from math import cos, sin, radians

class Bullet:

    def __init__(self, win, pos, vel, angle):

        self.vel = vel
        self.theta = radians(angle)
        self.pos = pos
        self.bullet = Circle(pos, 0.5)
        self.bullet.setFill('white')
        self.bullet.setOutline('white')
        self.bullet.draw(win)

    def update(self):
        '''Updates location of the bullet'''
        dx = self.vel*cos(self.theta)
        dy = self.vel*sin(self.theta)

        self.bullet.move(dx, dy)
    
    def getX(self):
        return self.bullet.getCenter().getX()
    
    def getY(self):
        return self.bullet.getCenter().getY()
    
    def undraw(self):
        self.bullet.undraw()