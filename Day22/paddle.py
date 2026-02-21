from turtle import Turtle

WIDTH = 20
HEIGHT = 100


class Paddle(Turtle):
    def __init__(self, x_pos, y_pos):
        super().__init__()
        self.x_pos = x_pos
        self.y_pos = y_pos

        self.create_paddle()

    def create_paddle(self):
        self.shape("square")
        self.penup()
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.color("white")
        self.goto(self.x_pos, self.y_pos)

    def go_up(self):
        self.goto(self.x_pos, self.ycor() + 20)

    def go_down(self):
        self.goto(self.x_pos, self.ycor() - 20)
