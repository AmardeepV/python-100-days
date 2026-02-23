from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
X = [-285, -245, -205, -165, -125, -85, -
     45, -5, 35, 75, 115, 155, 195, 235, 275]
Y = [-250, -220, -190, -160, -130, -100, -70, -40, -
     10, 20, 50, 80, 110, 140, 170, 200, 230, 260, 290]


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.x = random.choice(X)
        self.y = random.choice(Y)

        self.shape("square")
        self.penup()
        self.color(random.choice(COLORS))
        self.shapesize(stretch_len=1.5, stretch_wid=1)
        self.goto(self.x, self.y)
        self.speed_score = 0.5

    def move(self):
        # self.goto(self.xcor() - random.randint(0, 10), self.ycor())
        self.goto(self.xcor() - (self.speed_score * MOVE_INCREMENT), self.ycor())

    def loop_again(self):
        self.goto(285, self.ycor())

    def increase_speed(self):
        self.speed_score += 0.5
