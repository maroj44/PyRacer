#####################
## Objects portion ##
##  Jack Anderson  ##
##  Code Day PRJ   ##
##   Version 1.0   ##
#####################

# import libraries
from cdGraphics import *
from random import *
from time import *

# ==========================================================================
# Classes
class Runner(object):

    # . . . . . . . . . . . . .
    # Attributes and Constructor
    def __init__(self, x, y, size, window, color):
        self.square = Rectangle(Point(x, y), Point(x + size, y + size))
        self.square.setFill(color)
        self.window = window
        self.size = size
        self.centerX = x + (size / 2)
        self.centerY = y + (size / 2)

    def getX(self):
        return self.centerX

    def getY(self):
        return self.centerY

    def setX(self, x, size):
        self.centerX = x + (size / 2)

    def setY(self, y, size):
        self.centerY = y + (size / 2)

    # . . . . . . . . . . . . .
    # Behavior
    def draw(self):
        self.square.draw(self.window)

    def undraw(self):
        self.square.undraw()

    def move(self, direction):
        if direction == "Up" or direction == "w":
            self.square.move(0, -self.size)
        elif direction == "Down" or direction == "s":
            self.square.move(0, self.size)
        elif direction == "Left" or direction == "a":
            self.square.move(-self.size, 0)
        elif direction == "Right" or direction == "d":
            self.square.move(self.size, 0)

class Track(object):

    # . . . . . . . . . . . . .
    # Attributes and Constructor
    def __init__(self, x, y, color, height, width, window):
        self.oval = Oval(Point(x, y), Point(x + width, y + height))
        self.oval.setFill(color)
        self.oval.setOutline(color)
        self.window = window
        self.height = height
        self.width = width

    # . . . . . . . . . . . . .
    # Behavior
    def draw(self):
        self.oval.draw(self.window)

    def undraw(self):
        self.oval.undraw()

# ==========================================================================