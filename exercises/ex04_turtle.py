"""Describe scene program."""

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
    while i < 10:
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


def rectangle(artist: Turtle, x: int, y: int, height: int, width: int):
    """Draws a rectangle with inputed width and height."""
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


def grass(artist: Turtle):
    """Mows the lawn."""
    artist.hideturtle()
    artist.pencolor(12, 82, 3)
    artist.fillcolor(12, 82, 3)
    artist.begin_fill()
    rectangle(artist, -700, -700, 550, 1400)
    artist.end_fill()


def triangle(artist: Turtle, x: int, y: int, side_length: int):
    """Draws a triangle with inputed side length."""
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


def house(artist: Turtle):
    """Builds a different house each time."""
    artist.hideturtle()
    artist.pencolor(randint(0, 255), randint(0, 255), randint(0, 255))
    artist.fillcolor(randint(0, 255), randint(0, 255), randint(0, 255))
    position: int = randint(-500, 300)
    height: int = randint(250, 400)
    artist.begin_fill()
    rectangle(artist, position, -150, height, 250)
    triangle(artist, position, -150 + height, 250)
    artist.end_fill()


if __name__ == "__main__":
    main()