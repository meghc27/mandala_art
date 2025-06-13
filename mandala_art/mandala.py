import os
import turtle
from turtle import *

from mandala_art.designs.bright import bright_color_gen
from mandala_art.utils import *


def generate(
    color_scheme="colorful",
    bgcolor="black",
    screensize=550,
    fcolor=bright_color_gen(),
    color1=bright_color_gen(),
    color2=bright_color_gen(),
    animate=True,
    save_path=None,
    file_type="png",
    transparent=False,
):
    turtle.colormode(255)
    if bgcolor == "black" or bgcolor == "Black":
        bgc_tuple = (0, 0, 0)
    elif bgcolor == "red" or bgcolor == "Red":
        bgc_tuple = (255, 0, 0)
    elif bgcolor == "green" or bgcolor == "Green":
        bgc_tuple = (0, 255, 0)
    elif bgcolor == "blue" or bgcolor == "Blue":
        bgc_tuple = (0, 0, 255)
    elif (
        isinstance(bgcolor, tuple)
        and len(bgcolor) == 3
        and bgcolor[0] < 256
        and bgcolor[1] < 256
        and bgcolor[2] < 256
    ):
        bgc_tuple = bgcolor
    else:
        raise NameError(
            "bgcolor must be either 'black', 'white', 'red, 'green' or 'blue' or a tuple of three numbers between 0-255"
        )

    if animate:
        turtle.tracer(10)
        turtle.speed(0)
    else:
        turtle.tracer(0)

    screen = Screen()
    screen.setup(screensize, screensize)
    screen.setworldcoordinates(-410, -410, 410, 410)

    screen = turtle.Screen()
    screen.colormode(255)
    if transparent:
        bgc_tuple = (255, 255, 255)
        screen.bgcolor(bgc_tuple)
    else:
        screen.bgcolor(bgc_tuple)
        draw_background(bgc_tuple, screensize)

    if color_scheme == "colorful" or color_scheme == "Colorful":
        try:
            t1 = turtle.Turtle()
            layer1(t1, random.randint(1, 4), bright_color_gen(), bright_color_gen())
            t1.hideturtle()

            t2 = turtle.Turtle()
            layer2(t2, random.randint(1, 2), bright_color_gen(), bright_color_gen())
            t2.hideturtle()

            t3 = turtle.Turtle()
            layer3(t3, random.randint(1, 3), bright_color_gen(), bright_color_gen())
            t3.hideturtle()

            t4 = turtle.Turtle()
            layer4(t4, random.randint(1, 2), bright_color_gen(), bright_color_gen())
            t4.hideturtle()

        except Exception as e:
            print(e)

    if color_scheme == "b&w" or color_scheme == "B&W":
        turtle.bgcolor(0, 0, 0)
        try:
            t1 = turtle.Turtle()
            layer1(t1, random.randint(1, 4), col1=(255, 255, 255), col2=(125, 125, 125))
            t1.hideturtle()

            t2 = turtle.Turtle()
            layer2(t2, random.randint(1, 2), col2=(255, 255, 255), col1=(125, 125, 125))
            t2.hideturtle()

            t3 = turtle.Turtle()
            layer3(t3, random.randint(1, 3), col1=(255, 255, 255), col2=(125, 125, 125))
            t3.hideturtle()

            t4 = turtle.Turtle()
            layer4(t4, random.randint(1, 2), col2=(255, 255, 255), col1=(125, 125, 125))
            t4.hideturtle()

            turtle.hideturtle()

        except Exception as e:
            print(e)

    if color_scheme == "sepia" or color_scheme == "Sepia":
        turtle.bgcolor(112, 66, 20)
        try:
            t1 = turtle.Turtle()
            layer1(t1, random.randint(1, 4), col1=(255, 255, 255), col2=(255, 255, 255))
            t1.hideturtle()

            t2 = turtle.Turtle()
            layer2(t2, random.randint(1, 2), col2=(255, 255, 255), col1=(255, 255, 255))
            t2.hideturtle()

            t3 = turtle.Turtle()
            layer3(t3, random.randint(1, 3), col1=(255, 255, 255), col2=(255, 255, 255))
            t3.hideturtle()

            t4 = turtle.Turtle()
            layer4(t4, random.randint(1, 2), col2=(255, 255, 255), col1=(255, 255, 255))
            t4.hideturtle()

            turtle.hideturtle()

        except Exception as e:
            print(e)

    if color_scheme == "monochrome" or color_scheme == "Monochrome":
        try:
            t1 = turtle.Turtle()
            layer1(t1, random.randint(1, 4), col1=fcolor, col2=fcolor)
            t1.hideturtle()

            t2 = turtle.Turtle()
            layer2(t2, random.randint(1, 2), col1=fcolor, col2=fcolor)
            t2.hideturtle()

            t3 = turtle.Turtle()
            layer3(t3, random.randint(1, 3), col1=fcolor, col2=fcolor)
            t3.hideturtle()

            t4 = turtle.Turtle()
            layer4(t4, random.randint(1, 2), col1=fcolor, col2=fcolor)
            t4.hideturtle()

            turtle.hideturtle()

        except Exception as e:
            print(e)

    if color_scheme == "bicolor" or color_scheme == "Bicolor":
        try:
            t1 = turtle.Turtle()
            layer1(t1, random.randint(1, 4), col1=color1, col2=color2)
            t1.hideturtle()

            t2 = turtle.Turtle()
            layer2(t2, random.randint(1, 2), col1=color1, col2=color2)
            t2.hideturtle()

            t3 = turtle.Turtle()
            layer3(t3, random.randint(1, 3), col1=color1, col2=color2)
            t3.hideturtle()

            t4 = turtle.Turtle()
            layer4(t4, random.randint(1, 2), col1=color1, col2=color2)
            t4.hideturtle()

        except Exception as e:
            print(e)

    if save_path:
        from PIL import Image

        if "." in save_path:
            save_path = save_path.split(".")[0]
        canvas = turtle.getcanvas()
        eps_path = save_path + ".eps"
        canvas.postscript(file=eps_path)

        img = Image.open(eps_path)
        img.load(transparency=transparent)

        if transparent and file_type.lower() == "png":
            img = img.convert("RGBA")
            datas = img.getdata()
            newData = [
                (0, 0, 0, 0) if (r, g, b) == (0, 0, 0) else (r, g, b, a)
                for (r, g, b, a) in datas
            ]
            img.putdata(newData)
        else:
            img = img.convert("RGB")

        out_path = f"{save_path}.{file_type.lower()}"
        if file_type.lower() == "jpg":
            img.save(out_path, "JPEG")
        elif file_type.lower() == "png":
            img.save(out_path, "PNG")
        elif file_type.lower() == "pdf":
            img.save(out_path, "PDF")
        else:
            raise ValueError(f"Unsupported file type: {file_type}")

        # 🗑️ Now remove the EPS intermediary
        os.remove(eps_path)

    turtle.done()


def multiple(num_mandalas=10, screensize=550):
    turtle.colormode(255)
    turtle.bgcolor(0, 0, 0)
    screen = Screen()
    screen.setup(screensize, screensize)
    screen.setworldcoordinates(-410, -410, 410, 410)

    try:
        for i in range(num_mandalas):
            turtle.tracer(5)

            t1 = turtle.Turtle()
            layer1(t1, random.randint(1, 4), bright_color_gen(), bright_color_gen())
            t1.hideturtle()

            t2 = turtle.Turtle()
            layer2(t2, random.randint(1, 2), bright_color_gen(), bright_color_gen())
            t2.hideturtle()

            t3 = turtle.Turtle()
            layer3(t3, random.randint(1, 3), bright_color_gen(), bright_color_gen())
            t3.hideturtle()

            t4 = turtle.Turtle()
            layer4(t4, random.randint(1, 2), bright_color_gen(), bright_color_gen())
            t4.hideturtle()
            if i == num_mandalas - 1:
                continue
            t4.color(0, 0, 0)
            turtle.tracer(1)
            t4.circle(50)
            screen.clear()
            turtle.bgcolor(0, 0, 0)
            turtle.colormode(255)
            turtle.hideturtle()

        turtle.done()
        turtle.bye()

    except Exception as e:
        print(e)


def custom(
    l1,
    color11,
    color12,
    l2,
    color21,
    color22,
    l3,
    color31,
    color32,
    l4,
    color41,
    color42,
    bgcolor=(0, 0, 0),
    screensize=550,
    animate=True,
):
    try:
        if animate:
            turtle.tracer(5)
        else:
            turtle.tracer(0)

        turtle.colormode(255)
        turtle.bgcolor(bgcolor)
        screen = Screen()
        screen.setup(screensize, screensize)
        screen.setworldcoordinates(-410, -410, 410, 410)

        t1 = turtle.Turtle()
        layer1(t1, l1, color11, color12)
        t1.hideturtle()

        t2 = turtle.Turtle()
        layer2(t2, l2, color21, color22)
        t2.hideturtle()

        t3 = turtle.Turtle()
        layer3(t3, l3, color31, color32)
        t3.hideturtle()

        t4 = turtle.Turtle()
        layer4(t4, l4, color41, color42)
        t4.hideturtle()

        turtle.done()
        turtle.bye()

    except Exception as e:
        print(e)


if __name__ == "__main__":
    print("Generating a random mandala...")
    generate(screensize=900)
