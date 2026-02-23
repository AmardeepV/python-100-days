from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
X = [-285, -245, -205, -165, -125, -85, -
     45, -5, 35, 75, 115, 155, 195, 235, 275]
Y = [-250, -220, -190, -160, -130, -100, -70, -40, -
     10, 20, 50, 80, 110, 140, 170, 200, 230, 260, 290]


# class CarManager(Turtle):
#     def __init__(self):
#         super().__init__()
#         self.x = random.choice(X)
#         self.y = random.choice(Y)

#         self.shape("square")
#         self.penup()
#         self.color(random.choice(COLORS))
#         self.shapesize(stretch_len=1.5, stretch_wid=1)
#         self.goto(self.x, self.y)
#         self.speed_score = 0.5

#     def move(self):
#         self.goto(self.xcor() - (self.speed_score * MOVE_INCREMENT), self.ycor())

#     def loop_again(self):
#         self.goto(285, self.ycor())

#     def increase_speed(self):
#         self.speed_score += 0.5

class CarManager:
    def __init__(self):
        self.car_list = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        random_chance = random.randint(1, 6)
        if random_chance == 1:
            new_car = Turtle("square")
            new_car.penup()
            new_car.color(random.choice(COLORS))
            new_car.shapesize(stretch_len=2, stretch_wid=1)
            new_car.goto(300, random.choice(Y))
            self.car_list.append(new_car)

    def move(self):
        for car in self.car_list:
            car.backward(self.car_speed)

    def increase_speed(self):
        self.car_speed += MOVE_INCREMENT
