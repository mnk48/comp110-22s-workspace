"""Describe scene program."""

__author__ = "730389267"

from turtle import Turtle, colormode, done
colormode(255)
from random import randint


def main() -> None:
    """The entrypoint of my scene."""

def draw_star() -> None:
    

def random_stars() -> None:
    """Randomizes stars in the night sky."""
    star: Turtle = Turtle()
    i: int = 0
    while (i < 10):
        star.penup()
        star.goto(randint(-200, 200), randint(-200, 200))
        star.pendown()




def night_sky() -> None:
    """Creates a peaceful night sky."""
    #  fill the night sky first
    #  then add stars


if __name__ == "__main__":
    main()