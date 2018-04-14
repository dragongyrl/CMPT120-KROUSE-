#Author: Amelia Krouse
#Instructor: Juan Arias
#Date: 2/19

# There are still some improvements you can make to the code by putting the
# repeated statements into functions.

import graphics
import math
from graphics import *
from math import *

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

def insideChecker(num,win,displayString,secnum,operation):
    screenClean(win)
    displayString = displayString + num
    text = beforeText(displayString)
    text.draw(win)
    if operation ==True:
        if secnum==False:
            displayString = num
        secnum=True
    return displayString,secnum

def opDoer(win,para,sym,displayString,operation,opsign,hiddenString1):
    screenClean(win)
    if para==True:
        displayString= displayString+ sym
    else:
        hiddenString1 = displayString
        displayString = sym
        operation = True
        opsign = 1
    text = beforeText(displayString)
    text.draw(win)
    return displayString,operation,opsign,hiddenString1    

def screenClean(win):
    scr1 = Point(60, 60)
    scr2 = Point(380, 120)
    screen = Rectangle(scr1, scr2)
    screen.setFill('white')
    screen.draw(win)

def beforeText(displayString):
    return Text(Point(360-len(displayString) * 10, 90), displayString)

def afterText(displayString):
    return Text(Point(580-len(displayString)*5, 90), displayString)

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

def expoy(x,y):
    return float(x) **float(y)

def siny(x):
    return sin(float(x))

def cosy(x):
    return cos(float(x))

def tany(x):
    return tan(float(x))

def tenpowy(x):
    return 10 **float(x)

def logy(x,y):
    return log(float(y),float(x))

def arcsy(x):
    return 1/siny(x)

def arccy(x):
    return 1/cosy(x)

def arcty(x):
    return 1/tany(x)

def natlogy(x):
    return log(e,float(x))

def main():
    win = GraphWin('Calculator', 750, 650)
    corner1 = Point(40,40)
    corner2 = Point(750,550)
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
    sign= buttonMaker(220,460,280,520,'orange','+/-',win)
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

    science =buttonMaker(380,460,440,520,'red','SM',win)

    displayString = ''
    hiddenString1=''
    operation = False
    opsign = 0
    secnum = False
    scienceBoo=False
    para=False
    while 1==1:
        clicked = win.getMouse()
        if inside(clicked, num7, 60,140,120,200):
            displayString,secnum=insideChecker('7',win,displayString,secnum,operation)
        if inside(clicked, num8, 140,140,200,200):
            displayString,secnum=insideChecker('8',win,displayString,secnum,operation)
        if inside(clicked, num9, 220,140,280,200):
            displayString,secnum=insideChecker('9',win,displayString,secnum,operation)
        if inside(clicked, num4, 60,220,120,280):
            displayString,secnum=insideChecker('4',win,displayString,secnum,operation)
        if inside(clicked, num5, 140,220,200,280):
            displayString,secnum=insideChecker('5',win,displayString,secnum,operation)
        if inside(clicked, num6, 220,220,280,280):
            displayString,secnum=insideChecker('6',win,displayString,secnum,operation)
        if inside(clicked, num3, 220,300,280,360):
            displayString,secnum=insideChecker('3',win,displayString,secnum,operation)
        if inside(clicked, num2, 140,300,200,360):
            displayString,secnum=insideChecker('2',win,displayString,secnum,operation)
        if inside(clicked, num1, 60,300,120,360):
            displayString,secnum=insideChecker('1',win,displayString,secnum,operation)
        if inside(clicked, num0, 140,380,200,440):
            displayString,secnum=insideChecker('0',win,displayString,secnum,operation)
        if inside(clicked, numdec, 220,380,280,440):
            screenClean(win)
            displayString = displayString +'.'
            text = beforeText(displayString)
            text.draw(win)
        if inside(clicked, add, 300,140,360,200)and operation==False:
            displayString,operation,opsign,hiddenString1=opDoer(win,para,'+',displayString,operation,opsign,hiddenString1)
        if inside(clicked, sub, 300,220,360,280)and operation==False:
            displayString,operation,opsign,hiddenString1=opDoer(win,para,'-',displayString,operation,opsign,hiddenString1)
        if inside(clicked, mult, 300,300,360,360)and operation==False:
            displayString,operation,opsign,hiddenString1=opDoer(win,para,'x',displayString,operation,opsign,hiddenString1)
        if inside(clicked, div, 300,380,360,440)and operation==False:
            displayString,operation,opsign,hiddenString1=opDoer(win,para,'/',displayString,operation,opsign,hiddenString1)
        if inside(clicked, sign, 220,460,280,520)and operation==False:
            screenClean(win)
            displayString= str(0-float(displayString))
            text = beforeText(displayString)
            text.draw(win)
        if inside(clicked, equ, 300,460,360,520)and ((operation==True and secnum==True) or para==True):
            if scienceBoo ==False:
                screenClean(win)
            if para==True:
                result=eval(displayString)
            else:
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
                elif opsign==6:
                    result= expoy(hiddenString1, displayString)
                elif opsign==7:
                    result= logy(hiddenString1, displayString)
            restext = str(result)
            displayString = '=' + restext
            if scienceBoo ==False:
                text = beforeText(displayString)
            else:
                text = afterText(displayString)
            text.draw(win)
            para=False
        
        if inside(clicked, percent, 380,140,440,200)and operation==False:
            screenClean(win)
            hiddenString1 = displayString
            displayString = '%'
            operation = True
            opsign = 5
            text = beforeText(displayString)
            text.draw(win)
        if inside(clicked, sqrt, 380,220,440,280)and operation==False:
            screenClean(win)
            result = sqrty(displayString)
            displayString = str(result)
            text = afterText(displayString)
            text.draw(win)
        if inside(clicked, squ, 380,300,440,360)and operation==False:
            screenClean(win)
            result = squy(displayString)
            displayString = str(result)
            text = afterText(displayString)
            text.draw(win)
        if inside(clicked, denom, 380,380,440,440)and operation==False:
            screenClean(win)
            result = denomy(displayString)
            displayString = str(result)
            text = afterText(displayString)
            text.draw(win)
        if inside(clicked, clear, 60,380,120,440):
            screenClean(win)
            hiddenString1 = ''
            displayString = ''
            operation = False
            opsign= 0
            secnum=False
            if scienceBoo==True:
                scr1 = Point(380, 60)
                scr2 = Point(600, 120)
                screen1 = Rectangle(scr1, scr2)
                screen1.setFill('white')
                screen1.draw(win)

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

        if inside(clicked, science, 380,460,440,520):
            scienceBoo = True
            expo= buttonMaker(540,140,600,200,'orange','x^y',win)
            sinbut= buttonMaker(540,220,600,280,'orange','sin',win)
            cosbut= buttonMaker(540,300,600,360,'orange','cos',win)
            tanbut= buttonMaker(540,380,600,440,'orange','tan',win)
            tenpow= buttonMaker(540,460,600,520,'orange','10^x',win)
            logbut= buttonMaker(620,140,680,200,'orange','log',win)
            arcsbut= buttonMaker(620,220,680,280,'orange','arcsin',win)
            arccbut= buttonMaker(620,300,680,360,'orange','arccos',win)
            arctbut= buttonMaker(620,380,680,440,'orange','arctan',win)
            natlog= buttonMaker(620,460,680,520,'orange','ln',win)
            paraleft =buttonMaker(60,460,120,520,'yellow','(',win)
            pararight=buttonMaker(140,460,200,520,'yellow',')',win)
            scr1 = Point(380, 60)
            scr2 = Point(600, 120)
            screen1 = Rectangle(scr1, scr2)
            screen1.setFill('white')
            screen1.draw(win)
            displayString=''
            
        if scienceBoo == True:
            if inside(clicked, expo, 540,140,600,200):
                screenClean(win)
                hiddenString1 = displayString
                displayString = displayString + "^"
                operation = True
                opsign = 6
                text = beforeText(displayString)
                text.draw(win)
            if inside(clicked, sinbut, 540,220,600,280):
                screenClean(win)
                randstring = "sin(" +displayString + ")"
                text = beforeText(randstring)
                text.draw(win)
                displayString ="=" + str(siny(displayString))
                text1 = afterText(displayString)
                text1.draw(win)
            if inside(clicked, cosbut, 540,300,600,360):
                screenClean(win)
                randstring = "cos(" +displayString + ")"
                text = beforeText(randstring)
                text.draw(win)
                displayString = "=" + str(cosy(displayString))
                text1 = afterText(displayString)
                text1.draw(win)
            if inside(clicked, tanbut, 540,380,600,440):
                screenClean(win)
                randstring = "tan(" +displayString + ")"
                text = beforeText(randstring)
                text.draw(win)
                displayString = "=" + str(tany(displayString))
                text1 = afterText(displayString)
                text1.draw(win)
            if inside(clicked, tenpow, 540,460,600,520):
                screenClean(win)
                randstring = "10^"+displayString 
                text = beforeText(randstring)
                text.draw(win)
                displayString = "=" + str(tenpowy(displayString))
                text1 = afterText(displayString)
                text1.draw(win)
            if inside(clicked, logbut, 620,140,680,200):
                screenClean(win)
                hiddenString1 = displayString
                displayString = "log("+displayString + ")"
                operation = True
                opsign = 7
                text = beforeText(displayString)
                text.draw(win)
            if inside(clicked, arcsbut, 620,220,680,280):
                screenClean(win)
                randstring = "arcsin(" +displayString + ")"
                text = beforeText(randstring)
                text.draw(win)
                displayString ="=" + str(arcsy(displayString))
                text1 = afterText(displayString)
                text1.draw(win)
            if inside(clicked, arccbut, 620,300,680,360):
                screenClean(win)
                randstring = "arccos(" +displayString + ")"
                text = beforeText(randstring)
                text.draw(win)
                displayString = "=" + str(arccy(displayString))
                text1 = afterText(displayString)
                text1.draw(win)
            if inside(clicked, arctbut, 620,380,680,440):
                screenClean(win)
                randstring = "arctan(" +displayString + ")"
                text = beforeText(randstring)
                text.draw(win)
                displayString = "=" + str(arcty(displayString))
                text1 = afterText(displayString)
                text1.draw(win)
            if inside(clicked, natlog, 620,460,680,520):
                screenClean(win)
                randstring = "ln(" +displayString + ")"
                text = beforeText(randstring)
                text.draw(win)
                displayString = "=" + str(natlogy(displayString))
                text1 = afterText(displayString)
                text1.draw(win)
            if inside(clicked, paraleft, 60,460,120,520):
                screenClean(win)
                displayString = displayString + '('
                text = beforeText(displayString)
                text.draw(win)
                para=True
            if inside(clicked, pararight, 140,460,200,520):
                screenClean(win)
                displayString = displayString + ')'
                text = beforeText(displayString)
                text.draw(win)

main()
