import random
import turtle

from mandala_art.designs.bright import bright_color_gen


def draw_background(bgcolor, size):
    bg = turtle.Turtle()
    bg.hideturtle()
    bg.penup()
    bg.goto(-size // 2, -size // 2)
    bg.color(bgcolor)
    bg.begin_fill()
    for _ in range(4):
        bg.forward(size)
        bg.left(90)
    bg.end_fill()


def layer1(
    turt, num=random.randint(1, 4), col1=bright_color_gen(), col2=bright_color_gen()
):
    if num == 1:
        from mandala_art.layers.layer1 import layer11

        layer11(turt, col1, col2)

    elif num == 2:
        from mandala_art.layers.layer1 import layer12

        layer12(turt, col1, col2)

    elif num == 3:
        from mandala_art.layers.layer1 import layer13

        layer13(turt, col1, col2)

    elif num == 4:
        from mandala_art.layers.layer1 import layer14

        layer14(turt, col1, col2)


def layer2(
    turt, num=random.randint(1, 2), col1=bright_color_gen(), col2=bright_color_gen()
):
    if num == 1:
        from mandala_art.layers.layer2 import layer21

        layer21(turt, col1, col2)

    elif num == 2:
        from mandala_art.layers.layer2 import layer22

        layer22(turt, col1, col2)


def layer3(
    turt, num=random.randint(1, 3), col1=bright_color_gen(), col2=bright_color_gen()
):
    if num == 1:
        from mandala_art.layers.layer3 import layer31

        layer31(turt, col1, col2)

    elif num == 2:
        from mandala_art.layers.layer3 import layer32

        layer32(turt, col1, col2)

    elif num == 3:
        from mandala_art.layers.layer3 import layer33

        layer33(turt, col1, col2)


def layer4(
    turt, num=random.randint(1, 2), col1=bright_color_gen(), col2=bright_color_gen()
):
    if num == 1:
        from mandala_art.layers.layer4 import layer41

        layer41(turt, col1, col2)

    elif num == 2:
        from mandala_art.layers.layer4 import layer42

        layer42(turt, col1, col2)
