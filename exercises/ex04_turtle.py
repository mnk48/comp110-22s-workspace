"""Describe scene program."""

__author__ = "730389267"

from random import randint
from turtle import Turtle, colormode, done
colormode(255)


def main() -> None:
    """The entrypoint of my scene."""
    random_stars()
    done()


def draw_star() -> None:
    star: Turtle = Turtle()
    i: int = 0
    while i < 5:
        star.forward(20)
        star.right(144)
        i += 1

def random_stars() -> None:
    """Randomizes stars in the night sky."""
    star: Turtle = Turtle()
    star.hideturtle()
    i: int = 0
    while (i < 3):
        x: float = float(randint(-300, 300))
        y: float = float(randint(-300, 300))
        star.penup()
        star.goto(x, y)
        star.setheading(0.0)
        star.pendown()
        draw_star()
        i += 1
    done()


def night_sky() -> None:
    """Creates a peaceful night sky."""
    #  fill the night sky first
    #  then add stars


if __name__ == "__main__":
    main()