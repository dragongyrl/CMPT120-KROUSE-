#Amelia Krouse
#4/27

from graphics import *

class Display:

    def __init__(self, win, pt1):
        self.win = win
        ptX= pt1.getX() + 320
        ptY= pt1.getY() + 60
        self.pt2 = Point(ptX,ptY)
        self.rect = Rectangle(pt1, self.pt2)
        self.rect.setFill('white')
        self.rect.draw(win)
