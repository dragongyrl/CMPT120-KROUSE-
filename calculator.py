#Author: Amelia Krouse
#Instructor: Juan Arias
#Date: 2/19

import graphics
import math
from graphics import *
from math import *
from button import Button
from display import Display

class Calculator:

    def __init__(self):
        self.win = GraphWin('Calculator', 750, 650)
        corner1 = Point(40,40)
        corner2 = Point(750,550)
        base = Rectangle(corner1, corner2)
        base.setFill('lightblue')
        base.draw(self.win)

    def getWin(self):
        return self.win

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
    displayString= displayString + sym
    text = beforeText(displayString)
    text.draw(win)
    return displayString

def screenClean(win):
        scr1 = Point(60, 60)
        scr2 = Point(380, 120)
        screen1 = Rectangle(scr1, scr2)
        screen1.setFill('white')
        screen1.draw(win)

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
    calc = Calculator()
    win = calc.getWin()

    screen = Display(win,Point(60,60))

    num7= Button(win,Point(90,170),60,60,'7','yellow')
    num8= Button(win,Point(170,170),60,60,'8','yellow')
    num9= Button(win,Point(250,170),60,60,'9','yellow')
    num4= Button(win,Point(90,250),60,60,'4','yellow')
    num5= Button(win,Point(170,250),60,60,'5','yellow')
    num6= Button(win,Point(250,250),60,60,'6','yellow')
    num1= Button(win,Point(90,330),60,60,'1','yellow')
    num2= Button(win,Point(170,330),60,60,'2','yellow')
    num3= Button(win,Point(250,330),60,60,'3','yellow')
    num0= Button(win,Point(170,410),60,60,'0','yellow')
    numdec= Button(win,Point(250,410),60,60,'.','yellow')
    
    add= Button(win,Point(330,170),60,60,'+','orange')
    sub= Button(win,Point(330,250),60,60,'-','orange')
    mult= Button(win,Point(330,330),60,60,'x','orange')
    div= Button(win,Point(330,410),60,60,'/','orange')
    equ= Button(win,Point(330,490),60,60,'=','orange')
    sign= Button(win,Point(250,490),60,60,'+/-','orange')
    percent= Button(win,Point(410,170),60,60,'%','orange')
    sqrt= Button(win,Point(410,250),60,60,'sqrt','orange')
    squ= Button(win,Point(410,330),60,60,'x^2','orange')
    denom= Button(win,Point(410,410),60,60,'1/x','orange')
    clear= Button(win,Point(90,410),60,60,'C','orange')

    memclear= Button(win,Point(490,170),60,60,'MC','pink')
    memadd= Button(win,Point(490,250),60,60,'M+','pink')
    memsub= Button(win,Point(490,330),60,60,'M-','pink')
    memrec= Button(win,Point(490,410),60,60,'MR','pink')
    memsubst= Button(win,Point(490,490),60,60,'MS','pink')

    science = Button(win,Point(410,490),60,60,'SM','red')

    displayString = ''
    hiddenString1=''
    operation = False
    opsign = 0
    secnum = False
    scienceBoo=False
    para=False
    numButts=[num0,num1,num2,num3,num4,num5,num6,num7,num8,num9]
    while 1==1:
        clicked = win.getMouse()
        for i in range(10):
            if numButts[i].clicked(clicked):
                displayString,secnum=insideChecker(str(i),win,displayString,secnum,operation)
        if numdec.clicked(clicked):
            screenClean(win)
            displayString = displayString +'.'
            text = beforeText(displayString)
            text.draw(win)
        if add.clicked(clicked):
            displayString =opDoer(win,para,'+',displayString,operation,opsign,hiddenString1)
        if sub.clicked(clicked):
            displayString =opDoer(win,para,'-',displayString,operation,opsign,hiddenString1)
        if mult.clicked(clicked):
            displayString =opDoer(win,para,'*',displayString,operation,opsign,hiddenString1)
        if div.clicked(clicked):
            displayString =opDoer(win,para,'/',displayString,operation,opsign,hiddenString1)
        if sign.clicked(clicked):
            screenClean(win)
            displayString= str(0-float(displayString))
            text = beforeText(displayString)
            text.draw(win)
        if equ.clicked(clicked):
            if scienceBoo ==False:
                screenClean(win)
            result=eval(displayString)
            restext = str(result)
            displayString = '=' + restext
            if scienceBoo ==False:
                text = beforeText(displayString)
            else:
                text = afterText(displayString)
            text.draw(win)
            para=False
        
        if percent.clicked(clicked) and operation==False:
            screenClean(win)
            hiddenString1 = displayString
            displayString = '%'
            operation = True
            opsign = 5
            text = beforeText(displayString)
            text.draw(win)
        if sqrt.clicked(clicked) and operation==False:
            screenClean(win)
            result = sqrty(displayString)
            displayString = str(result)
            text = afterText(displayString)
            text.draw(win)
        if squ.clicked(clicked) and operation==False:
            screenClean(win)
            result = squy(displayString)
            displayString = str(result)
            text = afterText(displayString)
            text.draw(win)
        if denom.clicked(clicked) and operation==False:
            screenClean(win)
            result = denomy(displayString)
            displayString = str(result)
            text = afterText(displayString)
            text.draw(win)
        if clear.clicked(clicked):
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

        if memclear.clicked(clicked):
            screenClean(win)
            memory = memcleary()
            displayString=''
        if memadd.clicked(clicked):
            screenClean(win)
            memory = memaddy(memory,displayString)
            displayString=''
            text = Text(Point(360-len(memory) * 10, 90), memory)
            text.draw(win)
        if memsub.clicked(clicked):
            screenClean(win)
            memory = memsubby(memory,displayString)
            displayString=''
            text = Text(Point(360-len(memory) * 10, 90), memory)
            text.draw(win)
        if memrec.clicked(clicked):
            screenClean(win)
            displayString = memrecy(memory,win)
        if memsubst.clicked(clicked):
            screenClean(win)
            memory = memsubsty(displayString,win)
            displayString=''

        if science.clicked(clicked):
            scienceBoo = True
            expo= Button(win,Point(570,170),60,60,'x^y','orange')
            sinbut= Button(win,Point(570,250),60,60,'sin','orange')
            cosbut= Button(win,Point(570,330),60,60,'cos','orange')
            tanbut= Button(win,Point(570,410),60,60,'tan','orange')
            tenpow= Button(win,Point(570,490),60,60,'10^x','orange')
            logbut= Button(win,Point(650,170),60,60,'log','orange')
            arcsbut= Button(win,Point(650,250),60,60,'arcsin','orange')
            arccbut= Button(win,Point(650,330),60,60,'arccos','orange')
            arctbut= Button(win,Point(650,410),60,60,'arctan','orange')
            natlog= Button(win,Point(650,490),60,60,'ln','orange')
            paraleft =Button(win,Point(90,490),60,60,'(','yellow')
            pararight=Button(win,Point(170,490),60,60,')','yellow')
            
            scr1 = Point(380, 60)
            scr2 = Point(600, 120)
            screen1 = Rectangle(scr1, scr2)
            screen1.setFill('white')
            screen1.draw(win)
            displayString=''
            
        if scienceBoo == True:
            if expo.clicked(clicked):
                screenClean(win)
                hiddenString1 = displayString
                displayString = displayString + "^"
                operation = True
                opsign = 6
                text = beforeText(displayString)
                text.draw(win)
            if sinbut.clicked(clicked):
                screenClean(win)
                randstring = "sin(" +displayString + ")"
                text = beforeText(randstring)
                text.draw(win)
                displayString ="=" + str(siny(displayString))
                text1 = afterText(displayString)
                text1.draw(win)
            if cosbut.clicked(clicked):
                screenClean(win)
                randstring = "cos(" +displayString + ")"
                text = beforeText(randstring)
                text.draw(win)
                displayString = "=" + str(cosy(displayString))
                text1 = afterText(displayString)
                text1.draw(win)
            if tanbut.clicked(clicked):
                screenClean(win)
                randstring = "tan(" +displayString + ")"
                text = beforeText(randstring)
                text.draw(win)
                displayString = "=" + str(tany(displayString))
                text1 = afterText(displayString)
                text1.draw(win)
            if tenpow.clicked(clicked):
                screenClean(win)
                randstring = "10^"+displayString 
                text = beforeText(randstring)
                text.draw(win)
                displayString = "=" + str(tenpowy(displayString))
                text1 = afterText(displayString)
                text1.draw(win)
            if logbut.clicked(clicked):
                screenClean(win)
                hiddenString1 = displayString
                displayString = "log("+displayString + ")"
                operation = True
                opsign = 7
                text = beforeText(displayString)
                text.draw(win)
            if arcsbut.clicked(clicked):
                screenClean(win)
                randstring = "arcsin(" +displayString + ")"
                text = beforeText(randstring)
                text.draw(win)
                displayString ="=" + str(arcsy(displayString))
                text1 = afterText(displayString)
                text1.draw(win)
            if arccbut.clicked(clicked):
                screen.screenClean(win)
                randstring = "arccos(" +displayString + ")"
                text = beforeText(randstring)
                text.draw(win)
                displayString = "=" + str(arccy(displayString))
                text1 = afterText(displayString)
                text1.draw(win)
            if arctbut.clicked(clicked):
                screenClean(win)
                randstring = "arctan(" +displayString + ")"
                text = beforeText(randstring)
                text.draw(win)
                displayString = "=" + str(arcty(displayString))
                text1 = afterText(displayString)
                text1.draw(win)
            if natlog.clicked(clicked):
                screenClean(win)
                randstring = "ln(" +displayString + ")"
                text = beforeText(randstring)
                text.draw(win)
                displayString = "=" + str(natlogy(displayString))
                text1 = afterText(displayString)
                text1.draw(win)
            if paraleft.clicked(clicked):
                screenClean(win)
                displayString = displayString + '('
                text = beforeText(displayString)
                text.draw(win)
                para=True
            if pararight.clicked(clicked):
                screenClean(win)
                displayString = displayString + ')'
                text = beforeText(displayString)
                text.draw(win)

main()
