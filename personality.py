#Amelia Krouse
#Instructor: Juan Arias
#4/9/18

import graphics
from graphics import *

def makeAI():
    board = [ #0.happy 1.anger 2.sad 3.fear 4.disgust 5.surprise
        ['happy','surprise','happy','happy','surprise','happy'], #reward
        ['fear','anger','fear','fear','anger','fear'], #threaten
        ['happy','anger','surprise','disgust','anger','happy'], #joke
        ['surprise','fear','fear','fear','anger','disgust']] #punish
    return board

def buttonMaker(valX1,valY1,valX2,valY2,action,win):
    num1 = Point(valX1,valY1)
    num2 = Point(valX2,valY2)
    buttonNum = Rectangle(num1, num2)
    buttonNum.setFill('white')
    text = Text(Point(valX1+30,valY1+30),action)
    buttonNum.draw(win)
    text.draw(win)

def inside(clicked, valX1,valY1,valX2,valY2):
    if clicked.getX() > valX1 and clicked.getX() < valX2:
        if clicked.getY() > valY1 and clicked.getY() < valY2:
            return True

def screenClean(win):
    scr1 = Point(60, 60)
    scr2 = Point(300, 120)
    screen = Rectangle(scr1, scr2)
    screen.setFill('white')
    screen.draw(win)

def setEmotion(emotion):
    temp = 0
    if emotion=='happy':
        temp=0
    elif emotion=='anger':
        temp=1
    elif emotion=='sad':
        temp=2
    elif emotion=='fear':
        temp=3
    elif emotion=='disgust':
        temp=4
    elif emotion=='surprise':
        temp=5
    return temp
        
def main():
    win = GraphWin('AI', 400, 400)
    scr1 = Point(60, 60)
    scr2 = Point(300, 120)
    screen = Rectangle(scr1, scr2)
    screen.setFill('white')
    screen.draw(win)
    board = makeAI()
    buttonMaker(60,150,120,210,'reward',win)
    buttonMaker(150,150,210,210,'punish',win)
    buttonMaker(60,240,120,300,'joke',win)
    buttonMaker(150,240,210,300,'threaten',win)
    emotion = 0
    action = 0
    while True:
        clicked = win.getMouse()
        if inside(clicked, 60,150,120,210):
            action=0
        elif inside(clicked, 150,240,210,300):
            action=1
        elif inside(clicked, 60,240,120,300):
            action=2
        elif inside(clicked, 150,150,210,210):
            action=3
        displayString = board[action][emotion]
        screenClean(win)
        text=Text(Point(300-len(displayString) * 10, 90), displayString)
        text.draw(win)
        emotion = setEmotion(displayString)
main()
