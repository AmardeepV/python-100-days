from turtle import Turtle

WIDTH = 1  # 20
LENGTH = 1  # 20


class Ball(Turtle):
    def __init__(self):
        super().__init__()

        self.shape("circle")
        self.penup()
        self.color("white")
        self.shapesize(stretch_len=LENGTH, stretch_wid=WIDTH)
        self.new_x = 10
        self.new_y = 10
        self.ball_speed = 0.1

    def move(self):
        x_cor = self.xcor() + self.new_x
        y_cor = self.ycor() + self.new_y
        self.goto(x_cor, y_cor)

    def bounce_y(self):
        self.new_y *= -1

    def bounce_x(self):
        self.new_x *= -1
        self.ball_speed *= 0.9

    def ball_reset(self):
        self.goto(0, 0)
        self.ball_speed = 0.1
        self.bounce_x()
