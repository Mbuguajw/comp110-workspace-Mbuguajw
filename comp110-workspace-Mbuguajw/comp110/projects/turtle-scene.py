"""Bob Ross and MS Paint Collab: Where the random command meets art."""

__author__ = "730329579"

import random
from turtle import forward, left, right, goto, setheading
from turtle import pencolor, fillcolor, colormode, pensize
from turtle import penup, pendown, begin_fill, end_fill
from turtle import speed, done

colormode(255)
x: int = random.randint(100, 255)
y: int = random.randint(100, 255)
z: int = random.randint(100, 255)
a: int = random.randint(0, 99)
b: int = random.randint(0, 99)
c: int = random.randint(0, 99)
pensize(10)


def draw_scene() -> None:
    """Draw an amazing awe inspiring message with the type of a single command."""
    fillcolor(a, b, c)
    pencolor(x, y, z)
    begin_fill()
    drawbox(-300, 250)
    end_fill()
    writec(-200, 200, 50)
    writeo(-125, 150, 50)
    writem(-90, 150, 50)
    writep(-15, 150, 50)
    writes(-100, 75, 50)
    writec(-25, 75, 50)
    writei(0, 25, 50)
    writei(-50, -100, 50)
    writes(25, -50, 50)
    pencolor(z, x, y)
    writec(50, -150, 50)
    writeo(125, -200, 50)
    writeo(200, -200, 50)
    writel(225, -150, 50)
   

def writec(x: float, y: float, width: float) -> None:
    """The process of writing the letter c, including width and the location."""
    i: int = 0
    penup()
    goto(x, y)
    setheading(180)
    pendown()
    while i < 3:
        forward(width)
        left(90)
        i = i + 1


def writeo(x: float, y: float, width: float) -> None:
    """The process of writing the letter o, including width and the location."""
    i: int = 0
    penup()
    goto(x, y)
    setheading(0.0)
    pendown()
    while i < 4:
        left(90)
        forward(width)
        i = i + 1


def writem(x: float, y: float, width: float) -> None:
    """The process of writing the letter m, including width and the location."""
    penup()
    goto(x, y)
    setheading(90)
    pendown()
    forward(width)
    right(110)
    forward(width / 2)
    left(40)
    forward(width / 2)
    right(110)
    forward(width)
    

def writep(x: float, y: float, width: float) -> None:
    """The process of writing the letter p, including width and the location."""
    i: int = 0
    penup()
    goto(x, y)
    setheading(0.0)
    pendown()
    left(90)
    forward(width)
    while i < 3:
        right(90)
        forward(3 * width / 4)
        i = 1 + i


def writei(x: float, y: float, width: float) -> None:
    """The process of writing the letter i, including width and the location."""
    penup()
    goto(x, y)
    setheading(0.0)
    pendown()
    left(90)
    forward((3 * width) / 4)
    penup()
    forward(width / 4)
    pendown()
    forward(width / 4)


def writes(x: float, y: float, width: float) -> None:
    """The process of writing the letter s, including width and the location."""
    penup()
    goto(x, y)
    setheading(0.0)
    pendown()
    right(180)
    forward(width)
    left(90)
    forward(width / 2)
    left(90)
    forward(width)
    right(90)
    forward(width / 2)
    right(90)
    forward(width)


def writel(x: float, y: float, width: float) -> None:
    """The process of writing the letter l, including width and the location."""
    penup()
    goto(x, y)
    setheading(0.0)
    pendown()
    right(90)
    forward(width)
    left(90)
    forward(width)


def drawbox(x: float, y: float) -> None:
    """Drawing a box in the background to accentuate the features and colors of the font of the message."""
    i: int = 0
    penup()
    goto(x, y)
    setheading(0.0)
    pendown()
    while i < 2:
        forward(600)
        right(90)
        forward(500)
        right(90)
        i = i + 1


speed(10)
draw_scene()
done()