""""
    Rewriting homework2 without global variable
"""

from turtle import Turtle


def draw_part(turtle, lx_cor, ly_cor):
    """
    Function draw line to [lx_cor,ly_cor]
    """
    turtle.setpos(turtle.xcor() + lx_cor, turtle.ycor() + ly_cor)


def first_line(turtle, iter_num, line_size):
    if iter_num > 0:
        fourth_line(turtle, iter_num - 1, line_size)
        draw_part(turtle, +line_size, 0)

        first_line(turtle, iter_num - 1, line_size)
        draw_part(turtle, 0, line_size)

        first_line(turtle, iter_num - 1, line_size)
        draw_part(turtle, -line_size, 0)

        third_line(turtle, iter_num - 1, line_size)


def second_line(turtle, iter_num, line_size):
    if iter_num > 0:
        third_line(turtle, iter_num - 1, line_size)
        draw_part(turtle, -line_size, 0)

        second_line(turtle, iter_num - 1, line_size)
        draw_part(turtle, 0, -line_size)

        second_line(turtle, iter_num - 1, line_size)
        draw_part(turtle, line_size, 0)

        fourth_line(turtle, iter_num - 1, line_size)


def third_line(turtle, iter_num, line_size):
    if iter_num > 0:
        second_line(turtle, iter_num - 1, line_size)
        draw_part(turtle, 0, -line_size)
        third_line(turtle, iter_num - 1, line_size)
        draw_part(turtle, -line_size, 0)
        third_line(turtle, iter_num - 1, line_size)
        draw_part(turtle, 0, line_size)
        first_line(turtle, iter_num - 1, line_size)


def fourth_line(turtle, iter_num, line_size):
    if iter_num > 0:
        first_line(turtle, iter_num - 1, line_size)
        draw_part(turtle, 0, line_size)

        fourth_line(turtle, iter_num - 1, line_size)
        draw_part(turtle, line_size, 0)

        fourth_line(turtle, iter_num - 1, line_size)
        draw_part(turtle, 0, -line_size)

        second_line(turtle, iter_num - 1, line_size)


def hilbert(turtle, count_iterations, size):
    """
        Main function for draw Hilbert curves
    """
    turtle.speed("fast")
    turtle.up()
    turtle.setpos(-100, -100)
    turtle.down()
    first_line(turtle, count_iterations, size)
    turtle.done()


if __name__ == "__main__":
    hilbert(Turtle(), 4, 15)
