from turtle import *
import time

screen = Screen()
screen.screensize(600, 400)
screen.title("My snake game")
screen.bgcolor("black")
screen.tracer(0)

start_pos = [(0, 0), (-20, 0), (-40, 0)]
new_segments = []
game_is_on = True

for pos in start_pos:
    snake_seg = Turtle("square")
    snake_seg.color("white")
    snake_seg.penup()
    snake_seg.goto(pos)
    new_segments.append(snake_seg)

while game_is_on:
    screen.update()
    time.sleep(0.1)

    for seg in range(len(new_segments)-1, 0, -1):
        seg_x = new_segments[seg-1].xcor()
        seg_y = new_segments[seg-1].ycor()
        new_segments[seg].goto(seg_x, seg_y)
    new_segments[0].forward(20)


screen.exitonclick()
