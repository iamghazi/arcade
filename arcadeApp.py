from graphics import *
from launcher import Launcher
from target import Target

class ArcadeApp:

    def __init__(self):
        # create graphics window
        self.win = GraphWin(
            "ARCADE V.0", 640, 480
        )
        self.win.setCoords(-10, -10, 210, 155)
        
        self.win.setBackground('black')

        # add the launcher to the window
        self.launcher = Launcher(self.win, Point(105, 75))

        # add a container to the store all the targets
        self.targets = []

        # Add a container to store all the bullets
        self.bullets = []

        # Initialise hit count to 0
        self.hitCount = 0

        # Display score i.e hitCount in the window
        self.score = Text(
            Point(5, 152), 
            "Hits: "+str(self.hitCount)
        )
        self.score.setSize(12)
        self.score.setTextColor('white')
        self.score.draw(self.win)

        # Set text to display on gameover
        self.gotext = Text(Point(105, 80), 'GAME OVER')
        self.gotext.setSize(36)
        self.gotext.setTextColor('red')
        self.infoText = Text(
            Point(105, 70), 
            'Press s restart and q to quit!'
        )
        self.infoText.setSize(8)
        self.infoText.setTextColor('white')

        # Display info to play the game
        self.info = Text(
            Point(105, -3),
            'Press Space or Enter or f to shoot. Press'+ 
            ' Up/Down arrow to move the shooter forward'+ 
            '/backward.\nPress > and < to rotate. '+
            'Press right/left key to slide horizontally.'
        )
        self.info.setSize(6)
        self.info.setTextColor('white')
        self.info.draw(self.win)
        
    def startGame(self):
        # add the launcher to the window
        self.launcher = Launcher(self.win, Point(105, 75))

        for target in self.targets:
            target.undraw()
        
        for bullet in self.bullets:
            bullet.undraw()

        # add a container to the store all the targets
        self.targets = []

        # Add a container to store all the bullets
        self.bullets = []

        # Initialise hit count to 0
        self.hitCount = 0

        # update score
        self.updateScore()

        # Undraw texts after restart
        self.gotext.undraw()
        self.infoText.undraw()
    
    def run(self):
        # main event/animation loop
        count=0
        while True:
            key = self.win.checkKey()
            self.updateBullets()
            self.updateTargets()
            if key in ["q" , "Q"] :
                break
            if self.launcher and key == "Up":
                self.launcher.translate(1)
            elif self.launcher and key == "Down":
                self.launcher.translate(-1)
            elif self.launcher and key == "Right":
                self.launcher.slide(1)
            elif self.launcher and key == "Left":
                self.launcher.slide(-1)
            elif self.launcher and key == "period":
                self.launcher.rotate(-10)
            elif self.launcher and key == "comma":
                self.launcher.rotate(10)
            elif key in ["enter", "space", "f", "F"]:
                if self.launcher:
                    self.bullets.append(
                        self.launcher.shoot()
                    )
            elif key in ["s", "S"]:
                self.startGame()
            
            update(30)
            count+=1
            if count%15==0:
                self.targets.append(Target(self.win))
        self.win.close()
    
    def updateBullets(self):
        for bullet in self.bullets:
            bullet.update()
            if (not 0 <= bullet.getY() <= 150 \
                and not -10 < bullet.getX() < 205):
                
                bullet.undraw()
                self.bullets.remove(bullet)
    
    def updateTargets(self):
        for target in self.targets:
            target.update()
            # check if target is inside the window
            if (0 <= target.getY() <=150 \
                and -10 < target.getX() < 205):
                
                # check if target is touching the launcher
                if (self.launcher \
                    and 0 <= abs(target.getX() -\
                    self.launcher.getX()) <= 7.5\
                    and 0 <= abs(target.getY() - \
                    self.launcher.getY()) <= 7):

                    self.launcher.undraw()
                    self.launcher = None
                    target.undraw()
                    self.targets.remove(target)
                    self.endGame()
                else:
                    # check if target was hit by bullet
                    for bullet in self.bullets:
                        if 0 <= abs(target.getX() - \
                            bullet.getX()) <= 6\
                            and 0 <= abs(target.getY() -\
                            bullet.getY()) <= 5.5:
                            
                            bullet.undraw()
                            self.bullets.remove(bullet)
                            target.undraw()
                            self.targets.remove(target)
                            self.hitCount += 1
                            self.updateScore()
            else:
                target.undraw()
                self.targets.remove(target)
    
    def updateScore(self):
        self.score.setText("Hits: "+str(self.hitCount))
    
    def endGame(self):
        self.gotext.draw(self.win)
        self.infoText.draw(self.win)

if __name__=='__main__':
    ArcadeApp().run()