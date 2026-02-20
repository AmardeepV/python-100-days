from turtle import *
import random

screen = Screen()
screen.screensize(500, 500)

turtle_colors = ["red", "midnight blue", "forest green",
                 "goldenrod", "coral", "dark orchid", "yellow green"]
turtles_in_race = []
y_start_coordinates = [150, 100, 50, 0, -50, -100, -150]
is_race_on = False

bet_on_turtle = screen.textinput(
    "Bet on Turtle", "On which color turle you want to place your bet")

if bet_on_turtle:
    is_race_on = True

for index in range(0, 7):
    new_turtle = Turtle()
    new_turtle.penup()
    new_turtle.shape("turtle")
    new_turtle.color(turtle_colors[index])
    new_turtle.goto(x=-230, y=y_start_coordinates[index])
    turtles_in_race.append(new_turtle)

while is_race_on:

    for turtle in turtles_in_race:

        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()

            if bet_on_turtle == winning_color:
                print(
                    f"You won the race, Turtle with {winning_color} won the race")
            else:
                print(
                    f"You lost the race, Turtle with {winning_color} won the race")

        turtle.forward(random.randint(0, 10))


screen.exitonclick()
