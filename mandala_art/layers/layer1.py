"""
This is the first layer of the mandala
"""

from math import cos, pi, sin, tan

from mandala_art.designs.designs import *
from mandala_art.designs.turtle_math import arc


def layer11(turt, col1, col2):
    turt.width(1)
    turt.pencolor(col1)

    for _ in range(18):
        for _ in range(360):
            forw = pi * 90 / 360
            turt.forward(forw)
            turt.left(1)
            # t.circle(50)

        turt.left(20)

    turt.width(2)
    turt.pencolor(col2)
    turt.left(10)

    for _ in range(9):
        for _ in range(360):
            forw = pi * 50 / 360
            turt.forward(forw)
            turt.left(1)
            # t.circle(50)

        turt.left(40)


def layer12(turt, col1, col2):
    turt.width(3)
    turt.pencolor(col1)
    move = 80 / cos(deg2rad(10))
    r = 80 * tan(deg2rad(10))
    forw = deg2rad(r)

    for _ in range(18):
        turt.forward(move)
        turt.left(10)

        turt.forward(forw / 2)
        for _ in range(179):
            turt.left(1)
            turt.forward(forw)

        turt.left(1)
        turt.forward(forw / 2)

        turt.left(10)
        turt.forward(move)
        turt.left(180)

    turt.width(2)
    turt.pencolor(col2)
    turt.left(10)
    turt.fillcolor(col1)

    def little_circles():
        turt.forward(forw / 4)

        for _ in range(359):
            turt.right(1)
            turt.forward(forw / 2)

        turt.right(1)
        turt.forward(forw / 4)

    for _ in range(18):
        turt.forward(80 - r / 2)
        turt.left(90)

        turt.begin_fill()
        little_circles()
        turt.end_fill()

        turt.left(90)
        turt.forward(80 - r / 2)
        turt.right(160)


def layer13(turt, col1, col2):
    turt.width(3)
    turt.pencolor(col1)
    # turt.fillcolor(col2)
    for _ in range(18):
        s1 = 65 / cos(deg2rad(15))
        s2 = 2 * sin(deg2rad(15)) * s1
        turt.forward(s1)
        turt.left(45)
        turt.forward(s2)
        turt.left(120)
        turt.forward(s2)
        turt.left(45)
        turt.forward(s1)
        turt.left(170)

    turt.right(5)

    turt.width(1)
    turt.pencolor(col2)

    for _ in range(18):
        turt.penup()
        turt.forward(70)
        turt.pendown()
        little_diamonds(turt, s2, col2, col1)
        turt.left(150)
        turt.penup()
        turt.forward(70)
        turt.right(160)


def layer14(turt, col1, col2):
    th = 60
    R = 80

    r = 2 * R * sin(deg2rad(th / 2)) * tan(deg2rad(10))
    turt.width(3)
    for i in range(9):
        turt.color(col1)
        arc(turt, th, R, "r")
        arc(turt, 150, r, "r")
        turt.penup()

        turt.goto(0, 0)
        turt.right(230 - th)
        turt.pendown()

        turt.color(col2)
        arc(turt, th, R, "r")
        arc(turt, 150, r, "r")
        turt.penup()

        turt.goto(0, 0)
        turt.right(230 - th)
        turt.pendown()

    turt.color(col1)
    arc(turt, th, R)
