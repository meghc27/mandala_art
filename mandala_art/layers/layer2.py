"""
This is the second layer of the mandala
"""

import turtle
from math import cos, tan

from mandala_art.designs.designs import *


def layer21(turt, col1, col2):
    turt.width(4)
    turt.pencolor(col1)
    move = 140 / cos(deg2rad(20))
    r = 140 * tan(deg2rad(20))
    flower2(turt, r, move)

    turt.left(10)
    turt.width(2)
    turt.pencolor(col2)
    move = 110 / cos(deg2rad(20))
    r = 110 * tan(deg2rad(20))
    flower2(turt, r, move)
    dots1(turt, col1, col2)

    turt.right(2)
    turt.forward(100)

    turt.width(1)

    for _ in range(18):
        petal4(turt, col1, col2)


def layer22(turt, col1, col2):
    turt.right(10.5)

    turt.penup()
    turt.forward(100)

    turt.pendown()

    outer3(turt, col1, col2, width=3)

    turt.right(90)
    turt.penup()
    deg = 4

    arc(turt, deg, 100)

    turt.left(90)

    inner(turt, col1, col2, deg)
    turt.penup()
    turt.right(90)
    arc(turt, 10 - deg, 100)

    turt.left(90)

    turt.forward(65)
    turt.right(130)
    turt.pendown()
    turt.fillcolor((tuple(map(lambda x: int(x), list(turtle.bgcolor())))))

    lengths = [20, 27, 50, 27, 20]

    for _ in range(18):
        petal1(turt, col1, 5, lengths)
        turt.left(50)
        turt.forward(45)
        turt.dot()
        turt.backward(45)
        turt.right(90)

        turt.penup()

        arc(turt, 20, 165, "l")

        turt.left(140)
        turt.pendown()

    turt.left(130)
    turt.penup()
    turt.forward(5)
    turt.left(90)
    turt.pencolor(col2)
    turt.fillcolor(col2)

    arc(turt, 10, 170, "l")

    turt.right(90)

    turt.pendown()

    turt.width(3)

    for _ in range(18):
        petal3(turt, col1, col2)
        turt.right(90)

        turt.penup()

        turt.forward(deg2rad(170 / 2))
        turt.right(1)

        for _ in range(19):
            turt.forward(deg2rad(170))
            turt.right(1)

        turt.forward(deg2rad(170 / 2))
        turt.left(90)

        turt.pendown()

    turt.penup()
    turt.forward(20)
    turt.left(90)

    turt.pencolor(col1)
    turt.fillcolor(col1)

    dots2(turt)
