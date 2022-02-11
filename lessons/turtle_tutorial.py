"""Turtle tutorial."""

from turtle import Turtle, colormode, done
colormode(255)
leo: Turtle = Turtle()

# i: int = 0
# while (i < 4):
#     leo.forward(300)
#     leo.left(90)
#     i = i + 1

leo.speed(10)
leo.hideturtle()

leo.penup()
leo.goto(-120, -100)
leo.pendown()

leo.pencolor(17, 13, 153)
leo.fillcolor(47, 248, 220)

leo.begin_fill()
i: int = 0
while (i < 3):
    leo.forward(300)
    leo.left(120)
    i = i + 1
leo.end_fill()

bob: Turtle = Turtle()
bob.color("black")

bob.penup()
bob.goto(-120, -100)
bob.pendown()

bob.speed(100)

side_length: float = 300.0
i: int = 0
while (i < 500):
    side_length = side_length * 0.97
    bob.forward(side_length)
    bob.left(120.5)
    i = i + 1
done()
