from turtle import *


def draw_part(lx, ly):
    setpos(X + lx, Y + ly)
    global X
    X = X + lx
    global Y
    Y = Y + ly


def a(i):
    if i > 0:
        d(i - 1)
        draw_part(+lx, 0)
        a(i - 1)
        draw_part(0, ly)
        a(i - 1)
        draw_part(-lx, 0)
        c(i - 1)


def b(i):
    if i > 0:
        c(i - 1)
        draw_part(-lx, 0)
        b(i - 1)
        draw_part(0, -ly)
        b(i - 1)
        draw_part(lx, 0)
        d(i - 1)


def c(i):
    if i > 0:
        b(i - 1)
        draw_part(0, -ly)
        c(i - 1)
        draw_part(-lx, 0)
        c(i - 1)
        draw_part(0, ly)
        a(i - 1)


def d(i):
    if i > 0:
        a(i - 1)
        draw_part(0, ly)
        d(i - 1)
        draw_part(lx, 0)
        d(i - 1)
        draw_part(0, -ly)
        b(i - 1)


speed("fast")
lx = 15
ly = 15
X = -100
Y = -100
up()
setpos(X, Y)
down()
a(4)
done()
