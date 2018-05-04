""""
    Rewriting homework2 without global variable
"""

from turtle import Turtle


def draw_part(my_turtle, lx_cor, ly_cor):
    """
    Function draw line to [lx_cor,ly_cor]
    """
    my_turtle.setpos(my_turtle.xcor()+lx_cor, my_turtle.ycor()+ly_cor)


def first_line(my_turtle, iter_num, size_line):
    if iter_num > 0:
        fourth_line(my_turtle, iter_num - 1, size_line)
        draw_part(my_turtle, +size_line, 0)

        first_line(my_turtle, iter_num - 1, size_line)
        draw_part(my_turtle, 0, size_line)

        first_line(my_turtle, iter_num - 1, size_line)
        draw_part(my_turtle, -size_line, 0)

        third_line(my_turtle, iter_num - 1, size_line)


def second_line(my_turtle, iter_num, size_line):
    if iter_num > 0:
        third_line(my_turtle, iter_num - 1, size_line)
        draw_part(my_turtle, -size_line, 0)

        second_line(my_turtle, iter_num - 1, size_line)
        draw_part(my_turtle, 0, -size_line)

        second_line(my_turtle, iter_num - 1, size_line)
        draw_part(my_turtle, size_line, 0)

        fourth_line(my_turtle, iter_num - 1, size_line)


def third_line(my_turtle, iter_num, size_line):
    if iter_num > 0:
        second_line(my_turtle, iter_num - 1, size_line)
        draw_part(my_turtle, 0, -size_line)
        third_line(my_turtle, iter_num - 1, size_line)
        draw_part(my_turtle, -size_line, 0)
        third_line(my_turtle, iter_num - 1, size_line)
        draw_part(my_turtle, 0, size_line)
        first_line(my_turtle, iter_num - 1, size_line)


def fourth_line(my_turtle, iter_num, size_line):
    if iter_num > 0:
        first_line(my_turtle, iter_num - 1, size_line)
        draw_part(my_turtle, 0, size_line)

        fourth_line(my_turtle, iter_num - 1, size_line)
        draw_part(my_turtle, size_line, 0)

        fourth_line(my_turtle, iter_num - 1, size_line)
        draw_part(my_turtle, 0, -size_line)

        second_line(my_turtle, iter_num - 1, size_line)


def hilbert(my_turtle, count_iterations, size):
    """
        Main function for draw Hilbert curves
    """
    my_turtle.speed("fast")
    my_turtle.up()
    my_turtle.setpos(-100, -100)
    my_turtle.down()
    first_line(my_turtle, count_iterations, size)
    my_turtle.done()


if __name__ == "__main__":
    hilbert(Turtle(), 4, 15)

