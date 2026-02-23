import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

alex_turtle = Player()
score = Scoreboard()
cars = []
for i in range(30):
    cars.append(CarManager())

screen.listen()
screen.onkey(alex_turtle.move, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    for car in cars:
        car.move()

        if car.xcor() < - 290:
            car.loop_again()

        # check if the turtle collide with any car, game over restart
        if alex_turtle.distance(car) < 20:
            score.game_over()
            game_is_on = False

        # check if the turtle reached the top of the screen, update the level and increae the speed
        if alex_turtle.ycor() >= alex_turtle.end_point:
            print("you won, restaring")
            alex_turtle.home_position()
            score.score += 1
            score.update_scoreboard()
            for new_car in cars:
                new_car.increase_speed()


screen.exitonclick()
