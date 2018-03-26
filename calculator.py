#Author: Amelia Krouse
#Instructor: Juan Arias
#Date: 2/19

# There are still some improvements you can make to the code by putting the
# repeated statements into functions.

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
    text = Text(Point(valX1+30,valY1+30),num)
    buttonNum.draw(win)
    text.draw(win)

def screenClean(win):
    scr1 = Point(60, 60)
    scr2 = Point(380, 120)
    screen = Rectangle(scr1, scr2)
    screen.setFill('white')
    screen.draw(win)

def addy(x,y):
    return float(x) + float(y)

def subby(x,y):
    return float(x) - float(y)

def multy(x,y):
    return float(x) * float(y)

def divy(x,y):
    return float(x) / float(y)

def percy(x,y):
    return float(x) * float(y)/100.0

def sqrty(x):
    return float(x) **(1/2)

def squy(x):
    return float(x) **2

def denomy(x):
    return 1/float(x)

def memcleary():
    return ''

def memaddy(mem,dis):
    return str(float(mem)+float(dis))

def memsubby(mem,dis):
    return str(float(mem)-float(dis))

def memrecy(mem,win):
    text = Text(Point(360-len(mem) * 10, 90), mem)
    text.draw(win)
    return ''

def memsubsty(dis,win):
    text = Text(Point(360-len(dis) * 10, 90), dis)
    text.draw(win)
    return dis

def main():
    win = GraphWin('Calculator', 700, 560)
    corner1 = Point(40,40)
    corner2 = Point(600,540)
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
    percent= buttonMaker(380,140,440,200,'orange','%',win)
    sqrt= buttonMaker(380,220,440,280,'orange','sqrt',win)
    squ= buttonMaker(380,300,440,360,'orange','x^2',win)
    denom= buttonMaker(380,380,440,440,'orange','1/x',win)
    clear= buttonMaker(60,380,120,440,'orange','C',win)

    memclear= buttonMaker(460,140,520,200,'pink','MC',win)
    memadd= buttonMaker(460,220,520,280,'pink','M+',win)
    memsub= buttonMaker(460,300,520,360,'pink','M-',win)
    memrec= buttonMaker(460,380,520,440,'pink','MR',win)
    memsubst= buttonMaker(460,460,520,520,'pink','MS',win)

    displayString = ''
    operation = False
    opsign = 0
    secnum = False
    while 1==1:
        clicked = win.getMouse()
        if inside(clicked, num7, 60,140,120,200):
            screenClean(win)
            displayString = displayString + '7'
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
            displayString= str(0-float(displayString))
            text = Text(Point(360-len(displayString) * 10, 90), displayString)
            text.draw(win)
        if inside(clicked, equ, 300,460,360,520)and operation==True and secnum==True:
            screenClean(win)
            if opsign==1:
                result= addy(hiddenString1, displayString)
            elif opsign==2:
                result= subby(hiddenString1, displayString)
            elif opsign==3:
                result= multy(hiddenString1, displayString)
            elif opsign==4:
                result= divy(hiddenString1, displayString)
            elif opsign==5:
                result= percy(hiddenString1, displayString)
            restext = str(result)
            displayString = '=' + restext
            text = Text(Point(360-len(displayString) * 10, 90), displayString)
            text.draw(win)
        
        if inside(clicked, percent, 380,140,440,200)and operation==False:
            screenClean(win)
            hiddenString1 = displayString
            displayString = '%'
            operation = True
            opsign = 5
            text = Text(Point(360-len(displayString) * 10, 90), displayString)
            text.draw(win)
        if inside(clicked, sqrt, 380,220,440,280)and operation==False:
            screenClean(win)
            result = sqrty(displayString)
            displayString = str(result)
            text = Text(Point(360-len(displayString) * 10, 90), displayString)
            text.draw(win)
        if inside(clicked, squ, 380,300,440,360)and operation==False:
            screenClean(win)
            result = squy(displayString)
            displayString = str(result)
            text = Text(Point(360-len(displayString) * 10, 90), displayString)
            text.draw(win)
        if inside(clicked, denom, 380,380,440,440)and operation==False:
            screenClean(win)
            result = denomy(displayString)
            displayString = str(result)
            text = Text(Point(360-len(displayString) * 10, 90), displayString)
            text.draw(win)
        if inside(clicked, clear, 60,380,120,440):
            screenClean(win)
            hiddenString1 = ''
            displayString = ''
            operation = False
            opsign= 0
            secnum=False
            text = Text(Point(360-len(displayString) * 10, 90), displayString)
            text.draw(win)

        if inside(clicked, memclear, 460,140,520,200):
            screenClean(win)
            memory = memcleary()
            displayString=''
        if inside(clicked, memadd, 460,220,520,280):
            screenClean(win)
            memory = memaddy(memory,displayString)
            displayString=''
            text = Text(Point(360-len(memory) * 10, 90), memory)
            text.draw(win)
        if inside(clicked, memsub, 460,300,520,360):
            screenClean(win)
            memory = memsubby(memory,displayString)
            displayString=''
            text = Text(Point(360-len(memory) * 10, 90), memory)
            text.draw(win)
        if inside(clicked, memrec, 460,380,520,440):
            screenClean(win)
            displayString = memrecy(memory,win)
        if inside(clicked, memsubst, 460,460,520,520):
            screenClean(win)
            memory = memsubsty(displayString,win)
            displayString=''

main()
