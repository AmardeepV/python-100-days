from turtle import *

alex = Turtle()
screen = Screen()


def move_forward():
    alex.forward(10)


def move_backword():
    alex.backward(10)


def move_right():
    new_heading = alex.heading() - 10
    alex.setheading(new_heading)


def move_left():
    new_heading = alex.heading() + 10
    alex.setheading(new_heading)


def clear_display():
    alex.clear()
    alex.penup()
    alex.home()
    alex.pendown()


screen.listen()
screen.onkey(move_backword, "s")
screen.onkey(move_left, "a")
screen.onkey(move_right, "d")
screen.onkey(clear_display, "c")


screen.exitonclick()
