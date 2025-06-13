"""
This is the third layer of the mandala
"""

import turtle

from mandala_art.designs.designs import *
from mandala_art.designs.turtle_math import arc


def layer31(turt, col1, col2):
    radial = 205

    tr = turtle.tracer()
    lengths = [23, 24, 26, 31, 39, 31, 26, 24, 23]
    outer1wpetals(205, lengths, turt, col1, col2)

    turt.right(90)

    turt.forward(10)
    turt.pendown()
    turt.right(10)
    outer1(215, turt, col2, 1)

    turt.left(10)

    radial = 225
    turt.penup()

    turt.forward(10)
    turt.pendown()

    turt.right(10)

    outer1(225, turt, col1, 3)

    turt.left(10)

    turt.width(1)
    turt.penup()

    turt.forward(35)

    for _ in range(18):
        petal2(turt, col2, 35, 80, "l")

        turt.left(90)
        turt.penup()

        arc(turt, 20, 260, "r")
        turt.left(90)
        turt.pendown()

    turt.penup()
    # turt.left(180)
    turt.forward(15)
    turt.right(90)
    arc(turt, 3, 275)
    turt.left(90)

    for _ in range(18):
        petal2(turt, col2, 25, 80, "l")

        turt.left(90)
        turt.penup()

        arc(turt, 20, 275, "r")
        turt.left(90)
        turt.pendown()

    turt.penup()
    # turt.left(180)
    turt.forward(15)
    turt.right(90)
    arc(turt, 3, 290)
    turt.left(90)

    for _ in range(18):
        petal2(turt, col2, 15, 80, "l")

        turt.left(90)
        turt.penup()

        arc(turt, 20, 290, "r")
        turt.left(90)
        turt.pendown()


def layer32(turt, col1, col2):
    radial = 205

    tr = turtle.tracer()
    lengths = [44, 45, 48]
    outer1wsidepetals(205, lengths, turt, col1, col2)

    turt.right(90)

    turt.forward(10)
    turt.pendown()
    turt.right(10)
    outer1(215, turt, col2, 1)

    turt.left(10)

    radial = 225
    turt.penup()

    turt.forward(10)
    turt.pendown()

    turt.right(10)

    outer1(225, turt, col1, 3)

    turt.left(10)

    radial = 260
    turt.width(1)
    turt.penup()

    turt.forward(35)

    for _ in range(18):
        petal2(turt, col2, 35, 80, "l")

        turt.left(90)
        turt.penup()

        arc(turt, 20, 260, "r")
        turt.left(90)
        turt.pendown()

    turt.penup()
    # turt.left(180)
    turt.forward(15)
    turt.right(90)
    arc(turt, 3, 275)
    turt.left(90)

    for _ in range(18):
        petal2(turt, col2, 25, 80, "l")

        turt.left(90)
        turt.penup()

        arc(turt, 20, 275, "r")
        turt.left(90)
        turt.pendown()

    turt.penup()
    # turt.left(180)
    turt.forward(15)
    turt.right(90)
    arc(turt, 3, 290)
    turt.left(90)

    for _ in range(18):
        petal2(turt, col2, 15, 80, "l")

        turt.left(90)
        turt.penup()

        arc(turt, 20, 290, "r")
        turt.left(90)
        turt.pendown()


def layer33(turt, col1, col2):
    turt.pencolor(col2)
    outer2(turt, base=225, a1=65, a2=5, width=3)
    turt.penup()
    turt.goto(0, 0)
    turt.pendown()
    turt.pencolor(col1)
    outer2(turt, base=210, a1=65, a2=5, width=2)

    th = 60
    R = 30
    turt.left(90)

    turt.pencolor(col2)

    for _ in range(18):
        turt.penup()
        arc(turt, 10, 205, "l")
        h = turt.heading()
        turt.left(210 - th)

        x = turt.xcor()
        y = turt.ycor()
        turt.pendown()
        twisted_petals(turt, R, th, 8, x, y)

        turt.penup()
        turt.seth(h)
        arc(turt, 10, 210, "l")

    turt.penup()
    turt.goto(0, 0)
    turt.pendown()

    for _ in range(18):
        turt.penup()
        turt.forward(250)
        turt.pendown()
        turt.width(2)
        little_diamonds(turt, 50, col1, col2)
        turt.left(150)
        turt.penup()
        turt.forward(250)
        turt.right(160)

    turt.penup()
    turt.goto(0, 0)
    turt.pendown()
    turt.left(10)

    for _ in range(18):
        turt.penup()
        turt.forward(270)
        turt.pendown()
        turt.width(2)
        little_diamonds(turt, 50, col2, col1)
        turt.left(150)
        turt.penup()
        turt.forward(270)
        turt.right(160)
