from turtle import *


def middle(a, b):
    return [(a[0] + b[0]) / 2, (a[1] + b[1]) / 2]


def draw_triangle(v1, v2, v3, n):
    if n == 0:
        return
    nv1 = middle(v1, v2)
    nv2 = middle(v2, v3)
    nv3 = middle(v3, v1)
    up()
    setpos(nv3)
    down()
    setpos(nv1)
    setpos(nv2)
    setpos(nv3)
    draw_triangle(v1, nv1, nv3, n - 1)
    draw_triangle(v2, nv1, nv2, n - 1)
    draw_triangle(v3, nv3, nv2, n - 1)


def main_serpinskogo(len, n):
    v1 = [-len, -len / 2]
    v2 = [0, len]
    v3 = [len, -len / 2]
    speed("fast")
    up()
    setpos(v1)
    down()
    setpos(v2)
    setpos(v3)
    setpos(v1)
    draw_triangle(v1, v2, v3, n - 1)
    done()


# main_serpinskogo(350,7)
main_serpinskogo(200, 5)
