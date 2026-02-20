import turtle as t
import random

alex = t.Turtle()

t.colormode(255)


def color_mode():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)

    return (r, g, b)


# directions = [0, 90, 180, 270]
alex.pensize(2)
alex.speed("fastest")


for i in range(0, 360, 5):
    alex.color(color_mode())
    alex.circle(100)
    alex.setheading(i)


screen = t.Screen()
screen.exitonclick()
