"""This fall has been a weird one; Every time you come home, the landlord has completely renovated.

Attempting 'break up complex functions' in lines 87-93, 141-158, and 199-225.
Attempting 'try something fun' through randomization of time of day (lines 33-41); house position
and color (both fill and pen color of house and windows) (lines 199-225); sun, moon, and star position (lines 44-54, 57-67, and 87-93);
leaf position and color (lines 96-119); bird position (lines 122-138); and watching eye position (lines 228-249).
"""


__author__ = "730389267"


from random import randint
from turtle import Turtle, colormode, done, tracer, update
colormode(255)


def main() -> None:
    """The entrypoint of my scene."""
    t: Turtle = Turtle()
    t.pensize(3)
    tracer(0, 0)
    time()
    sky(t)
    grass(t)
    house(t)
    eyes(t, randint(100, 500), randint(100, 400))
    eyes(t, randint(100, 500), randint(100, 400))
    update()
    done()


def time() -> str:
    """Decides the time of the scene: day or night."""
    x: int = randint(1, 2)
    random_time: str = ""
    if x == 1:
        random_time += "day"
    if x == 2:
        random_time += "night"
    return random_time


def moon(artist: Turtle, radius: float) -> None:
    """Generates a full moon at a different position each time."""
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
    """Generates a beaming sun of different colors at a different position each time."""
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
    """Draws a yellow star."""
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
    """Randomizes stars and moon in the sky."""
    i: int = 0
    while i < 20:
        draw_star(artist, randint(-600, 600), randint(-200, 500))
        i += 1
    moon(artist, 50)


def leaves(artist: Turtle) -> None:
    """Creates red, green, or yellow leaves at random locations."""
    random_color: int = randint(1, 3)  # random_color is being established to determine a random leaf color.
    leaf_color: str = ""
    if random_color == 1:
        leaf_color += "red"
    if random_color == 2:
        leaf_color += "green"
    if random_color == 3:
        leaf_color += "yellow"
    i: int = 0
    while i < 25:
        artist.penup()
        artist.goto(randint(-600, 600), randint(-400, 500))
        artist.setheading(0.0)
        artist.pendown()
        artist.pencolor(leaf_color)
        artist.fillcolor(leaf_color)
        artist.begin_fill()
        artist.circle(15, 70)
        artist.left(110)
        artist.circle(15, 70)
        artist.end_fill()
        i += 1


def birds(artist: Turtle) -> None:
    """Creates random birds in the sky."""
    x: int
    y: int
    i: int = 0
    while i < 6:
        x = randint(-700, 700)
        y = randint(0, 400)
        artist.penup()
        artist.goto(x, y)
        artist.setheading(0.0)
        artist.pendown()
        artist.pencolor("black")
        artist.fillcolor("black")
        artist.circle(-15, 70)
        artist.circle(15, -70)
        i += 1


def sky(artist: Turtle) -> None:
    """Creates a peaceful day (with sun, leaves, and birds) or night (with moon and stars) sky."""
    if time() == "day":  # Calls time() to decide what elements to place in the sky, and to decide the color of the sky.
        artist.pencolor(39, 208, 219)
        artist.fillcolor(39, 208, 219)
        artist.begin_fill()
        square(artist, -700, -700, 1400)
        artist.end_fill() 
        sun(artist, 50)
        leaves(artist)
        birds(artist)
    else:
        artist.pencolor(5, 4, 40)
        artist.fillcolor(5, 4, 40)
        artist.begin_fill()
        square(artist, -700, -700, 1400)
        artist.end_fill() 
        night_sky(artist)
     

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
    """Draws a square with left bottom corner at (x, y) and with inputed width."""
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
    """Grows the grass and mows the lawn."""
    artist.hideturtle()
    artist.pencolor(12, 82, 3)
    artist.fillcolor(12, 82, 3)
    artist.begin_fill()
    rectangle(artist, -700, -700, 550, 1400)
    artist.end_fill()


def house(artist: Turtle) -> None:
    """Builds a different house each time with new colors and position."""
    artist.hideturtle()
    artist.pencolor(randint(0, 255), randint(0, 255), randint(0, 255))  # Randomizes the outline and fill color of the main house.
    artist.fillcolor(randint(0, 255), randint(0, 255), randint(0, 255))
    position: int = randint(-500, 300)
    artist.begin_fill()  # Makes the main house.
    rectangle(artist, position, -150, 280, 250)
    # triangle(artist, position, -150 + height, 250)
    artist.end_fill()
    artist.pencolor(randint(0, 255), randint(0, 255), randint(0, 255))  # Randomizes the outline and fill color of the door.
    artist.fillcolor(randint(0, 255), randint(0, 255), randint(0, 255))
    artist.begin_fill()  # Makes the door.
    rectangle(artist, position + 100, -150, 100, 50)
    artist.end_fill()
    artist.pencolor(randint(0, 255), randint(0, 255), randint(0, 255))  # Randomizes the outline and fill color of the windows.
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


def eyes(artist: Turtle, x: int, y: int) -> None:
    """A pair of eyes protect over the scene, at random positions each time."""
    i: int = 0
    while i < 2:
        artist.penup()
        artist.goto(x + (i * 20), y)
        artist.setheading(0.0)
        artist.pendown()
        artist.pencolor("black")
        artist.fillcolor("white")
        artist.begin_fill()
        artist.circle(10)
        artist.end_fill()
        artist.penup()
        artist.goto(x + (i * 20) + 3, y + 3)
        artist.setheading(0.0)
        artist.pendown()
        artist.fillcolor("black")
        artist.begin_fill()
        artist.circle(2)
        artist.end_fill()
        i += 1


if __name__ == "__main__":
    main()