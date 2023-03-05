# Python 3.x
import turtle
from random import *
from math import *
from time import *

def draw():
    turtle.pencolor(random(), random(), random())
    global n, sf
    n = 0
    sf = 0
    while  n > width / (-2 * zoom):
        f = evale(express, n)
        drawf(n, f)
        n -= (1 / zoom)
    n = 0
    sf = 0
    while  n < width / (2 * zoom):
        f = evale(express, n)
        drawf(n, f)
        n += (1 / zoom)

def drawf(n, f):
    if n == 0 or isnan(f.real):
        turtle.penup()
    else:
        turtle.pendown()
    if isnan(f.real):
        f = 0
    elif n.imag != 0:
        f = abs(f)
    if hight / -zoom < f.real < hight / zoom:
        turtle.goto(n * zoom, f.real * zoom)

def drawxy():
    turtle.clear()
    turtle.pencolor(0, 0, 0)
    turtle.penup()
    turtle.goto(0, 0)
    turtle.pendown()
    turtle.goto(width / -2, 0)
    turtle.goto(width / 2, 0)
    turtle.goto(0, 0)
    turtle.goto(0, hight / 2)
    turtle.goto(0, hight / -2)

def format(s):
    s = s.replace("^","**")
    s = s.replace("@","differentiate")
    s = s.replace("$","integral")
    return s

def evale(s, n):
    x = n
    try:
        return eval(s)
    except BaseException:
        return nan

def differentiate(s):
    dx = 0.1 / zoom
    f1 = evale(s, n)
    df = evale(s, n + dx) - f1
    return df / dx

def integral(s):
    global sf
    dx = copysign(1 / zoom, n)
    f1 = evale(s, n)
    df = (f1 + evale(s, n + dx)) / 2
    sf = sf + df * dx
    return sf

def rezoom(n):
    global zoom
    zoom = n
    drawxy()
    draw()

zoom = eval(input("zoom = "))
width = 1280
hight = 720

turtle.setup(width, hight)
turtle.hideturtle()
turtle.delay(0)
turtle.pensize(2)
drawxy()

while True:
    express = format(input("f(x) = "))
    draw()

    while True:
        i = input(": ")
        if i == "break":
            break
        else:
            try:
                print(eval(i))
            except BaseException:
                print("Input error.")