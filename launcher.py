from graphics import *
from math import radians, cos, sin, degrees, sqrt
from bullet import Bullet

class Launcher:

    def __init__(self, win, apex):
        '''
            creates a launcher which shoots bullets 
        '''        
        self.win = win
        self.vel = 3.0
        self.angle = radians(90.0)
        self.vertices = [
            Point(apex.getX(), apex.getY()),
            Point(apex.getX()+sqrt(3), apex.getY()-3-sqrt(3)),
            Point(apex.getX(), apex.getY()-3),
            Point(apex.getX()-sqrt(3), apex.getY()-3-sqrt(3))
        ]

        # Draw the launcher
        self.shooter = Polygon(self.vertices)
        self.shooter.setOutline('white')
        self.shooter.draw(win)

    def rotate(self, amt):
        '''Rotates the shooter by amt degrees'''

        self.angle = self.angle + radians(amt)
        self.shooter.undraw()

        # set center x and y
        cx = self.vertices[2].getX()
        cy = self.vertices[2].getY()

        # Rotate each point except the center
        for i, pt in enumerate(self.vertices):
            if i!= 2:
                px = pt.getX()
                py = pt.getY()
                self.vertices[i] = Point(
                    cos(radians(amt))*(px-cx)\
                    -sin(radians(amt))*(py-cy)+cx,
                    sin(radians(amt))*(px-cx)\
                    +cos(radians(amt))*(py-cy)+cy,
                )
        
        # Update shooter
        self.shooter = Polygon(self.vertices)
        self.shooter.setOutline('white')
        self.shooter.draw(self.win)
    
    def translate(self, direction):
        '''
            Translates the shooter in the direction
            of set angle by set velocity
        '''
        for i, pt in enumerate(self.vertices):
            self.vertices[i] = Point(
                pt.getX() + self.vel*direction*cos(self.angle),
                pt.getY() + self.vel*direction*sin(self.angle)
            )
        
        self.shooter.undraw()

        # Update the shooter position
        self.shooter = Polygon(self.vertices)
        self.shooter.setOutline('white')
        self.shooter.draw(self.win)
    
    def slide(self, direction):
        '''
            Slides target horizontally left or right
        '''
        for i, pt in enumerate(self.vertices):
            self.vertices[i] = Point(
                pt.getX() + self.vel*direction,
                pt.getY()
            )

            self.shooter.undraw()

            # Update the shooter position
            self.shooter = Polygon(self.vertices)
            self.shooter.setOutline('white')
            self.shooter.draw(self.win)

    def shoot(self):
        '''
            Shoots a bullet through apex
        '''
        return Bullet(
            self.win,
            self.vertices[0],
            self.vel,
            degrees(self.angle)
        )
    
    def getX(self):
        return self.vertices[0].getX()
    
    def getY(self):
        return self.vertices[0].getY()
    
    def undraw(self):
        self.shooter.undraw()