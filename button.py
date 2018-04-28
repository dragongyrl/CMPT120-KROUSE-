#Amelia Krouse
#4/27

from graphics import *

class Button:

    def __init__(self, win, center, width, height, label,color):
        """Creats a rectangular button, eg:
        qb = Button(myWin, Point(30,25), 20, 10, 'Quit') """

        w,h = width/2.0, height/2.0
        x,y = center.getX(),center.getY()
        self.xmax, self.xmin = x+w, x-w
        self.ymax, self.ymin = y+h, y-h
        p1 = Point(self.xmin, self.ymin)
        p2 = Point(self.xmax, self.ymax)
        self.rect = Rectangle(p1, p2)
        self.rect.setFill(color)
        self.rect.draw(win)
        self.label = Text(center, label)
        self.label.draw(win)
        self.activate()

    def activate(self):
        "Sets this button to 'active'."
        self.label.setFill('black')
        self.rect.setWidth(2)
        self.active = True

    def deactivate(self):
        "Sets this button to 'inactive'."
        self.label.setFill('darkgrey')
        self.rect.setWidth(1)
        self.active = False

    def clicked(self, p):
        "Returns true if button active and p is inside"
        return self.active and \
               self.xmin <= p.getX() <= self.xmax and \
               self.ymin <= p.getY() <= self.ymax

    def getLabel(self):
        return self.label;
        
        
        
