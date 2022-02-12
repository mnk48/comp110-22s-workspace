"""Every time you come home, the landlord has completely renovated."""

__author__ = "730389267"

from random import randint
from turtle import Turtle, colormode, done, tracer, update
colormode(255)

t: Turtle = Turtle()


def main() -> None:
    """The entrypoint of my scene."""
    tracer(0, 0)
    night_sky(t)
    random_stars(t)
    moon(t, 50)
    grass(t)
    house(t)
    update()
    done()


def draw_star(artist: Turtle, x: int, y: int) -> None:
    """An artist draws a star."""
    artist.hideturtle()
    artist.penup()
    artist.goto(x, y)
    artist.setheading(0.0)
    artist.pendown()
    artist.pencolor("yellow")
    artist.fillcolor("yellow")
    i: int = 0
    artist.begin_fill()
    while i < 5:
        artist.forward(20)
        artist.right(144)
        i += 1
    artist.end_fill()


def random_stars(artist: Turtle) -> None:
    """Randomizes stars in the night sky."""
    i: int = 0
    while i < 20:
        draw_star(t, randint(-600, 600), randint(-200, 500))
        i += 1


def square(artist: Turtle, x: int, y: int, width: int) -> None:
    """Draws a square with inputed width."""
    artist.penup()
    artist.goto(x, y)
    artist.setheading(0.0)
    artist.pendown()
    i: int = 0
    while i < 4:
        artist.forward(width)
        artist.left(90)
        i += 1


def night_sky(artist: Turtle) -> None:
    """Creates a peaceful night sky."""
    artist.pencolor(5, 4, 40)
    artist.fillcolor(5, 4, 40)
    artist.begin_fill()
    square(t, -700, -700, 1400)
    artist.end_fill()


def rectangle(artist: Turtle, x: int, y: int, height: int, width: int) -> None:
    """Draws a rectangle with left bottom corner at (x, y) and inputed width and height."""
    artist.penup()
    artist.goto(x, y)
    artist.setheading(0.0)
    artist.pendown()
    artist.forward(width)
    artist.left(90)
    artist.forward(height)
    artist.left(90)
    artist.forward(width)
    artist.left(90)
    artist.forward(height)


def grass(artist: Turtle) -> None:
    """Mows the lawn."""
    artist.hideturtle()
    artist.pencolor(12, 82, 3)
    artist.fillcolor(12, 82, 3)
    artist.begin_fill()
    rectangle(artist, -700, -700, 550, 1400)
    artist.end_fill()


def triangle(artist: Turtle, x: int, y: int, side_length: int) -> None:
    """Draws a triangle with left corner at (x, y) and with inputed side length."""
    artist.hideturtle()
    artist.penup()
    artist.goto(x, y)
    artist.setheading(0.0)
    artist.pendown()
    i: int = 0
    while (i < 3):
        artist.forward(side_length)
        artist.left(120)
        i = i + 1


def house(artist: Turtle) -> None:
    """Builds a different house each time."""
    artist.hideturtle()
    artist.pencolor(randint(0, 255), randint(0, 255), randint(0, 255))
    artist.fillcolor(randint(0, 255), randint(0, 255), randint(0, 255))
    position: int = randint(-500, 300)
    artist.begin_fill()  # Makes the main house.
    rectangle(artist, position, -150, 280, 250)
    # triangle(artist, position, -150 + height, 250)
    artist.end_fill()
    artist.pencolor(randint(0, 255), randint(0, 255), randint(0, 255))
    artist.fillcolor(randint(0, 255), randint(0, 255), randint(0, 255))
    artist.begin_fill()  # Makes the door.
    rectangle(artist, position + 100, -150, 100, 50)
    artist.end_fill()
    artist.pencolor(randint(0, 255), randint(0, 255), randint(0, 255))
    artist.fillcolor(randint(0, 255), randint(0, 255), randint(0, 255))
    artist.begin_fill()  # Makes the top window. 
    rectangle(artist, position + 25, 0, 80, 200)
    artist.end_fill()
    i: int = 0
    while i < 2:  # Makes the two windows.
        artist.begin_fill()
        square(artist, position + 30, -120, 50)
        artist.end_fill()
        position += 140
        i += 1


def moon(artist: Turtle, radius: float) -> None:
    artist.penup()
    artist.goto(randint(-200, 500), randint(0, 200))
    artist.setheading(0.0)
    artist.pendown()
    artist.pencolor("yellow")
    artist.fillcolor("yellow")
    artist.begin_fill()
    artist.circle(radius)
    artist.end_fill()
   

if __name__ == "__main__":
    main()