"""Every time you come home, the landlord has completely renovated."""

__author__ = "730389267"

from random import randint
from turtle import Turtle, colormode, done, tracer, update
colormode(255)

t: Turtle = Turtle()


def main() -> None:
    """The entrypoint of my scene."""
    tracer(0, 0)
    sky(t)
    grass(t)
    house(t)
    update()
    done()


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


def sun(artist: Turtle, radius: float) -> None:
    artist.penup()
    artist.goto(randint(-200, 500), randint(0, 200))
    artist.setheading(0.0)
    artist.pendown()
    artist.pencolor(randint(190, 255), randint(174, 233), randint(48, 62))
    artist.fillcolor(randint(190, 255), randint(174, 233), randint(48, 62))
    artist.begin_fill()
    artist.circle(radius)
    artist.end_fill()


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


def night_sky(artist: Turtle) -> None:
    """Randomizes stars and moon in the night sky."""
    i: int = 0
    while i < 20:
        draw_star(t, randint(-600, 600), randint(-200, 500))
        i += 1
    moon(artist, 50)


def leaves(artist: Turtle) -> None:
    random_color: int = randint(1, 3)
    leaf_color: str = ""
    if random_color == 1:
        leaf_color += "red"
    if random_color == 2:
        leaf_color += "green"
    if random_color == 3:
        leaf_color += "yellow"
    i: int = 0
    while i < 20:
        artist.penup()
        artist.goto(randint(-600, 600), randint(-400, 500))
        artist.setheading(0.0)
        artist.pendown()
        artist.pencolor(leaf_color)
        artist.fillcolor(leaf_color)
        artist.begin_fill()
        artist.circle(300, 70)
        artist.left(110)
        artist.circle(300, 70)
        artist.end_fill()


def time() -> str:
    x: int = randint(1, 2)
    if x == 1:
        return "day"
    else:
        return "night"


def season() -> str:
    x: int = randint(1, 4)
    season_type: str = ""
    if x == 1:
        season_type += "winter"
    if x == 2:
        season_type += "spring"
    if x == 3:
        season_type += "summer"
    if x == 4:
        season_type += "fall"
    return season_type


def sky(artist: Turtle) -> None:
    """Creates a peaceful sky."""
    # artist.pencolor(5, 4, 40)
    # artist.fillcolor(5, 4, 40)
    # artist.begin_fill()
    # square(t, -700, -700, 1400)
    # artist.end_fill()
    if time() == "day":
        artist.pencolor(39, 208, 219)
        artist.fillcolor(39, 208, 219)
        artist.begin_fill()
        square(t, -700, -700, 1400)
        artist.end_fill() 
        sun(artist, 50)
    else:
        artist.pencolor(5, 4, 40)
        artist.fillcolor(5, 4, 40)
        artist.begin_fill()
        square(t, -700, -700, 1400)
        artist.end_fill() 
        night_sky(artist)
    if season() == "fall":
        leaves(artist)
     

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


if __name__ == "__main__":
    main()