import turtle
import string


def middle(a, b):
    return [(a[0] + b[0]) / 2, (a[1] + b[1]) / 2]


def draw_triangle(v1, v2, v3, n, my_turtle):
    if n == 0:
        return
    nv1 = middle(v1, v2)
    nv2 = middle(v2, v3)
    nv3 = middle(v3, v1)
    my_turtle.up()
    my_turtle.setpos(nv3)
    my_turtle.down()
    my_turtle.setpos(nv1)
    my_turtle.setpos(nv2)
    my_turtle.setpos(nv3)
    draw_triangle(v1, nv1, nv3, n - 1, my_turtle)
    draw_triangle(v2, nv1, nv2, n - 1, my_turtle)
    draw_triangle(v3, nv3, nv2, n - 1, my_turtle)


def main_serpinskogo(len, n):
    my_turtle = turtle.Turtle()  # type: Turtle
    v1 = [-len, -len / 2]
    v2 = [0, len]
    v3 = [len, -len / 2]
    my_turtle.speed("fast")
    my_turtle.up()
    my_turtle.setpos(v1)
    my_turtle.down()
    my_turtle.setpos(v2)
    my_turtle.setpos(v3)
    my_turtle.setpos(v1)
    draw_triangle(v1, v2, v3, n - 1, my_turtle)
    my_turtle.done()


# main_serpinskogo(350,7)
main_serpinskogo(200, 5)
