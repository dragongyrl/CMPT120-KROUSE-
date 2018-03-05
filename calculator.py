#Author: Amelia Krouse
#Instructor: Juan Arias
#Date: 2/19

import graphics
from graphics import *

def inside(clicked, button, valX1,valY1,valX2,valY2):
    if clicked.getX() > valX1 and clicked.getX() < valX2:
        if clicked.getY() > valY1 and clicked.getY() < valY2:
            return True

def buttonMaker(valX1,valY1,valX2,valY2,color,num,win):
    num1 = Point(valX1,valY1)
    num2 = Point(valX2,valY2)
    buttonNum = Rectangle(num1, num2)
    buttonNum.setFill(color)
    text = Text(Point((valX2-valX1)/2,(valY2-valY1)/2),num)
    buttonNum.draw(win)
    text.draw(win)


def screenClean(win):
    scr1 = Point(60, 60)
    scr2 = Point(380, 120)
    screen = Rectangle(scr1, scr2)
    screen.setFill('white')
    screen.draw(win)

def main():
    win = GraphWin('Calculator', 500, 560)
    corner1 = Point(40,40)
    corner2 = Point(400,540)
    base = Rectangle(corner1, corner2)
    base.setFill('lightblue')
    base.draw(win)
    
    scr1 = Point(60, 60)
    scr2 = Point(380, 120)
    screen = Rectangle(scr1, scr2)
    screen.setFill('white')
    screen.draw(win)

    num7= buttonMaker(60,140,120,200,'yellow','7',win)
    num8= buttonMaker(140,140,200,200,'yellow','8',win)
    num9= buttonMaker(220,140,280,200,'yellow','9',win)
    num4= buttonMaker(60,220,120,280,'yellow','4',win)
    num5= buttonMaker(140,220,200,280,'yellow','5',win)
    num6= buttonMaker(220,220,280,280,'yellow','6',win)
    num1= buttonMaker(60,300,120,360,'yellow','1',win)
    num2= buttonMaker(140,300,200,360,'yellow','2',win)
    num3= buttonMaker(220,300,280,360,'yellow','3',win)
    num0= buttonMaker(140,380,200,440,'yellow','0',win)
    numdec= buttonMaker(220,380,280,440,'yellow','.',win)
    
    add= buttonMaker(300,140,360,200,'orange','+',win)
    sub= buttonMaker(300,220,360,280,'orange','-',win)
    mult= buttonMaker(300,300,360,360,'orange','x',win)
    div= buttonMaker(300,380,360,440,'orange','/',win)
    equ= buttonMaker(300,460,360,520,'orange','=',win)
    sign= buttonMaker(220,460,280,520,'orange','-',win)

    displayString = ''
    operation = False
    opsign = 0
    secnum = False
    while 1==1:
        clicked = win.getMouse()
        if inside(clicked, num7, 60,140,120,200):
            screenClean(win)
            displayString = displayString +'7'
            text = Text(Point(360-len(displayString) * 10, 90), displayString)
            text.draw(win)
            if operation ==True:
                if secnum==False:
                    displayString = '7'
                secnum=True
        if inside(clicked, num8, 140,140,200,200):
            screenClean(win)
            displayString = displayString +'8'
            text = Text(Point(360-len(displayString) * 10, 90), displayString)
            text.draw(win)
            if operation ==True:
                if secnum==False:
                    displayString = '8'
                secnum=True
        if inside(clicked, num9, 220,140,280,200):
            screenClean(win)
            displayString = displayString +'9'
            text = Text(Point(360-len(displayString) * 10, 90), displayString)
            text.draw(win)
            if operation ==True:
                if secnum==False:
                    displayString = '9'
                secnum=True
        if inside(clicked, num4, 60,220,120,280):
            screenClean(win)
            displayString = displayString +'4'
            text = Text(Point(360-len(displayString) * 10, 90), displayString)
            text.draw(win)
            if operation ==True:
                if secnum==False:
                    displayString = '4'
                secnum=True
        if inside(clicked, num5, 140,220,200,280):
            screenClean(win)
            displayString = displayString +'5'
            text = Text(Point(360-len(displayString) * 10, 90), displayString)
            text.draw(win)
            if operation ==True:
                if secnum==False:
                    displayString = '5'
                secnum=True
        if inside(clicked, num6, 220,220,280,280):
            screenClean(win)
            displayString = displayString +'6'
            text = Text(Point(360-len(displayString) * 10, 90), displayString)
            text.draw(win)
            if operation ==True:
                if secnum==False:
                    displayString = '6'
                secnum=True
        if inside(clicked, num3, 220,300,280,360):
            screenClean(win)
            displayString = displayString +'3'
            text = Text(Point(360-len(displayString) * 10, 90), displayString)
            text.draw(win)
            if operation ==True:
                if secnum==False:
                    displayString = '3'
                secnum=True
        if inside(clicked, num2, 140,300,200,360):
            screenClean(win)
            displayString = displayString +'2'
            text = Text(Point(360-len(displayString) * 10, 90), displayString)
            text.draw(win)
            if operation ==True:
                if secnum==False:
                    displayString = '2'
                secnum=True
        if inside(clicked, num1, 60,300,120,360):
            screenClean(win)
            displayString = displayString +'1'
            text = Text(Point(360-len(displayString) * 10, 90), displayString)
            text.draw(win)
            if operation ==True:
                if secnum==False:
                    displayString = '1'
                secnum=True
        if inside(clicked, num0, 140,380,200,440):
            screenClean(win)
            displayString = displayString +'0'
            text = Text(Point(360-len(displayString) * 10, 90), displayString)
            text.draw(win)
            if operation ==True:
                if secnum==False:
                    displayString = '0'
                secnum=True
        if inside(clicked, numdec, 220,380,280,440):
            screenClean(win)
            displayString = displayString +'.'
            text = Text(Point(360-len(displayString) * 10, 90), displayString)
            text.draw(win)
        if inside(clicked, add, 300,140,360,200)and operation==False:
            screenClean(win)
            hiddenString1 = displayString
            displayString = '+'
            operation = True
            opsign = 1
            text = Text(Point(360-len(displayString) * 10, 90), displayString)
            text.draw(win)
        if inside(clicked, sub, 300,220,360,280)and operation==False:
            screenClean(win)
            hiddenString1 = displayString
            displayString = '-'
            operation = True
            opsign = 2
            text = Text(Point(360-len(displayString) * 10, 90), displayString)
            text.draw(win)
        if inside(clicked, mult, 300,300,360,360)and operation==False:
            screenClean(win)
            hiddenString1 = displayString
            displayString = 'x'
            operation = True
            opsign = 3
            text = Text(Point(360-len(displayString) * 10, 90), displayString)
            text.draw(win)
        if inside(clicked, div, 300,380,360,440)and operation==False:
            screenClean(win)
            hiddenString1 = displayString
            displayString = '/'
            operation = True
            opsign = 4
            text = Text(Point(360-len(displayString) * 10, 90), displayString)
            text.draw(win)
        if inside(clicked, sign, 220,460,280,520)and operation==False:
            screenClean(win)
            displayString= str(0-int(displayString))
            text = Text(Point(360-len(displayString) * 10, 90), displayString)
            text.draw(win)
        if inside(clicked, equ, 300,460,360,520)and operation==True and secnum==True:
            screenClean(win)
            hiddenString2 = displayString
            if opsign==1:
                result= int(hiddenString1) + int(hiddenString2)
            elif opsign==2:
                result= int(hiddenString1) - int(hiddenString2)
            elif opsign==3:
                result= int(hiddenString1) * int(hiddenString2)
            elif opsign==4:
                result= int(hiddenString1) / int(hiddenString2)
            restext = str(result)
            displayString = '=' + restext
            text = Text(Point(360-len(displayString) * 10, 90), displayString)
            text.draw(win)


main()
