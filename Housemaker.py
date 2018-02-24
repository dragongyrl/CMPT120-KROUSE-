#Author: Amelia Krouse
#Instructor: Juan Arias
#Date: 2/12/18

import graphics
from graphics import *
def main():
    win = GraphWin()
    win = GraphWin('House',400,400)
    corner1 = win.getMouse()
    corner2 = win.getMouse()
    house = Rectangle(corner1, corner2)
    house.draw(win)
    door = win.getMouse()
    houseWidth = corner2.getX()-corner1.getX()
    doorWidth = houseWidth/5
    doorCorner1 = Point(door.getX()-doorWidth/2, door.getY())
    doorCorner2 = Point(door.getX()+doorWidth/2, corner1.getY())
    doorFrame = Rectangle(doorCorner1, doorCorner2)
    doorFrame.draw(win)
    windowCenter = win.getMouse()
    windowWidth = doorWidth/2
    windowCorner1 = Point(windowCenter.getX()-windowWidth/2, windowCenter.getY()-windowWidth/2)
    windowCorner2 = Point(windowCenter.getX()+windowWidth/2, windowCenter.getY()+windowWidth/2)
    windowFrame = Rectangle(windowCorner1, windowCorner2)
    windowFrame.draw(win)
    roofTop = win.getMouse()
    houseTop1 = Point(corner1.getX(), corner2.getY())
    roofLine1 = Line(houseTop1, roofTop)
    roofLine2 = Line(roofTop, corner2)
    roofLine1.draw(win)
    roofLine2.draw(win)

main()

