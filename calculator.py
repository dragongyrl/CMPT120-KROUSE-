#Author: Amelia Krouse
#Instructor: Juan Arias
#Date: 2/19

import graphics
from graphics import *

def inside(clicked, button, p1, p2):
    if clicked.getX() > button.p1.getX() and clicked.getX() < button.p2.getX():
        if clicked.getY() > button.p1.getY() and clicked.getY() < button.p2.getY():
            return True

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

    num71 = Point(60,140)
    num72 = Point(120,200)
    num7 = Rectangle(num71, num72)
    num7.setFill('yellow')
    text7 = Text(Point(90,170),'7')
    num7.draw(win)
    text7.draw(win)

    num81 = Point(140,140)
    num82 = Point(200,200)
    num8 = Rectangle(num81, num82)
    num8.setFill('yellow')
    text8 = Text(Point(170,170),'8')
    num8.draw(win)
    text8.draw(win)

    num91 = Point(220,140)
    num92 = Point(280,200)
    num9 = Rectangle(num91, num92)
    num9.setFill('yellow')
    text9 = Text(Point(250,170),'9')
    num9.draw(win)
    text9.draw(win)

    num41 = Point(60,220)
    num42 = Point(120,280)
    num4 = Rectangle(num41, num42)
    num4.setFill('yellow')
    text4 = Text(Point(90,250),'4')
    num4.draw(win)
    text4.draw(win)

    num51 = Point(140,220)
    num52 = Point(200,280)
    num5 = Rectangle(num51, num52)
    num5.setFill('yellow')
    text5 = Text(Point(170,250),'5')
    num5.draw(win)
    text5.draw(win)

    num61 = Point(220,220)
    num62 = Point(280,280)
    num6 = Rectangle(num61, num62)
    num6.setFill('yellow')
    text6 = Text(Point(250,250),'6')
    num6.draw(win)
    text6.draw(win)

    num11 = Point(60,300)
    num12 = Point(120,360)
    num1 = Rectangle(num11, num12)
    num1.setFill('yellow')
    text1 = Text(Point(90,330),'1')
    num1.draw(win)
    text1.draw(win)

    num21 = Point(140,300)
    num22 = Point(200,360)
    num2 = Rectangle(num21, num22)
    num2.setFill('yellow')
    text2 = Text(Point(170,330),'2')
    num2.draw(win)
    text2.draw(win)

    num31 = Point(220,300)
    num32 = Point(280,360)
    num3 = Rectangle(num31, num32)
    num3.setFill('yellow')
    text3 = Text(Point(250,330),'3')
    num3.draw(win)
    text3.draw(win)

    num01 = Point(140,380)
    num02 = Point(200,440)
    num0 = Rectangle(num01, num02)
    num0.setFill('yellow')
    text0 = Text(Point(170,410),'0')
    num0.draw(win)
    text0.draw(win)

    numdec1 = Point(220,380)
    numdec2 = Point(280,440)
    numdec = Rectangle(numdec1, numdec2)
    numdec.setFill('yellow')
    textdec = Text(Point(250,410),'.')
    numdec.draw(win)
    textdec.draw(win)

    add1 = Point(300,140)
    add2 = Point(360,200)
    add = Rectangle(add1, add2)
    add.setFill('orange')
    textadd = Text(Point(330,170),'+')
    add.draw(win)
    textadd.draw(win)

    sub1 = Point(300,220)
    sub2 = Point(360,280)
    sub = Rectangle(sub1, sub2)
    sub.setFill('orange')
    textsub = Text(Point(330,250),'-')
    sub.draw(win)
    textsub.draw(win)

    mult1 = Point(300,300)
    mult2 = Point(360,360)
    mult = Rectangle(mult1, mult2)
    mult.setFill('orange')
    textmult = Text(Point(330,330),'x')
    mult.draw(win)
    textmult.draw(win)

    div1 = Point(300,380)
    div2 = Point(360,440)
    div = Rectangle(div1, div2)
    div.setFill('orange')
    textdiv = Text(Point(330,410),'/')
    div.draw(win)
    textdiv.draw(win)

    equ1 = Point(300,460)
    equ2 = Point(360,520)
    equ = Rectangle(equ1, equ2)
    equ.setFill('orange')
    textequ = Text(Point(330,490),'=')
    equ.draw(win)
    textequ.draw(win)

    sign1 = Point(220,460)
    sign2 = Point(280,520)
    sign = Rectangle(sign1, sign2)
    sign.setFill('orange')
    textsign = Text(Point(250,490),'+/-')
    sign.draw(win)
    textsign.draw(win)

    displayString = ''
    operation = False
    opsign = 0
    secnum = False
    while 1==1:
        clicked = win.getMouse()
        if inside(clicked, num7, num71, num72):
            screenClean(win)
            displayString = displayString +'7'
            text = Text(Point(360-len(displayString) * 10, 90), displayString)
            text.draw(win)
            if operation ==True:
                if secnum==False:
                    displayString = '7'
                secnum=True
        if inside(clicked, num8, num81, num82):
            screenClean(win)
            displayString = displayString +'8'
            text = Text(Point(360-len(displayString) * 10, 90), displayString)
            text.draw(win)
            if operation ==True:
                if secnum==False:
                    displayString = '8'
                secnum=True
        if inside(clicked, num9, num91, num92):
            screenClean(win)
            displayString = displayString +'9'
            text = Text(Point(360-len(displayString) * 10, 90), displayString)
            text.draw(win)
            if operation ==True:
                if secnum==False:
                    displayString = '9'
                secnum=True
        if inside(clicked, num4, num41, num42):
            screenClean(win)
            displayString = displayString +'4'
            text = Text(Point(360-len(displayString) * 10, 90), displayString)
            text.draw(win)
            if operation ==True:
                if secnum==False:
                    displayString = '4'
                secnum=True
        if inside(clicked, num5, num51, num52):
            screenClean(win)
            displayString = displayString +'5'
            text = Text(Point(360-len(displayString) * 10, 90), displayString)
            text.draw(win)
            if operation ==True:
                if secnum==False:
                    displayString = '5'
                secnum=True
        if inside(clicked, num6, num61, num62):
            screenClean(win)
            displayString = displayString +'6'
            text = Text(Point(360-len(displayString) * 10, 90), displayString)
            text.draw(win)
            if operation ==True:
                if secnum==False:
                    displayString = '6'
                secnum=True
        if inside(clicked, num3, num31, num32):
            screenClean(win)
            displayString = displayString +'3'
            text = Text(Point(360-len(displayString) * 10, 90), displayString)
            text.draw(win)
            if operation ==True:
                if secnum==False:
                    displayString = '3'
                secnum=True
        if inside(clicked, num2, num21, num22):
            screenClean(win)
            displayString = displayString +'2'
            text = Text(Point(360-len(displayString) * 10, 90), displayString)
            text.draw(win)
            if operation ==True:
                if secnum==False:
                    displayString = '2'
                secnum=True
        if inside(clicked, num1, num11, num12):
            screenClean(win)
            displayString = displayString +'1'
            text = Text(Point(360-len(displayString) * 10, 90), displayString)
            text.draw(win)
            if operation ==True:
                if secnum==False:
                    displayString = '1'
                secnum=True
        if inside(clicked, num0, num01, num02):
            screenClean(win)
            displayString = displayString +'0'
            text = Text(Point(360-len(displayString) * 10, 90), displayString)
            text.draw(win)
            if operation ==True:
                if secnum==False:
                    displayString = '0'
                secnum=True
        if inside(clicked, numdec, numdec1, numdec2):
            screenClean(win)
            displayString = displayString +'.'
            text = Text(Point(360-len(displayString) * 10, 90), displayString)
            text.draw(win)
        if inside(clicked, add, add1, add2)and operation==False:
            screenClean(win)
            hiddenString1 = displayString
            displayString = '+'
            operation = True
            opsign = 1
            text = Text(Point(360-len(displayString) * 10, 90), displayString)
            text.draw(win)
        if inside(clicked, sub, sub1, sub2)and operation==False:
            screenClean(win)
            hiddenString1 = displayString
            displayString = '-'
            operation = True
            opsign = 2
            text = Text(Point(360-len(displayString) * 10, 90), displayString)
            text.draw(win)
        if inside(clicked, mult, mult1, mult2)and operation==False:
            screenClean(win)
            hiddenString1 = displayString
            displayString = 'x'
            operation = True
            opsign = 3
            text = Text(Point(360-len(displayString) * 10, 90), displayString)
            text.draw(win)
        if inside(clicked, div, div1, div2)and operation==False:
            screenClean(win)
            hiddenString1 = displayString
            displayString = '/'
            operation = True
            opsign = 4
            text = Text(Point(360-len(displayString) * 10, 90), displayString)
            text.draw(win)
        if inside(clicked, sign, sign1, sign2)and operation==False:
            screenClean(win)
            displayString= str(0-int(displayString))
            text = Text(Point(360-len(displayString) * 10, 90), displayString)
            text.draw(win)
        if inside(clicked, equ, equ1, equ2)and operation==True and secnum==True:
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
