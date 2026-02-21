from turtle import *
from paddle import Paddle
from ball import Ball
import time
from scoreboard import ScoreBoard


def main():
    screen = Screen()
    screen.setup(width=800, height=600)
    screen.bgcolor("black")
    screen.title("Pong")
    screen.tracer(0)

    X_POS = 350
    Y_POS = 0
    delay_time = 0.1

    r_paddle = Paddle(X_POS, Y_POS)
    l_paddle = Paddle(-X_POS, Y_POS)

    ball = Ball()
    score = ScoreBoard()

    screen.listen()
    screen.onkey(r_paddle.go_up, "i")
    screen.onkey(r_paddle.go_down, "k")
    screen.onkey(l_paddle.go_up, "w")
    screen.onkey(l_paddle.go_down, "s")

    game_is_on = True
    while game_is_on:
        screen.update()
        ball.move()
        time.sleep(ball.ball_speed)

        # logic for collision to the upper and lower wall
        if ball.ycor() > 280 or ball.ycor() < -280:
            ball.bounce_y()

        # logic for collision to the paddles
        if (ball.xcor() > 340 and ball.distance(r_paddle) < 50) or (ball.xcor() < -340 and ball.distance(l_paddle) < 50):
            ball.bounce_x()

        # logic for collifing to the right wall
        if ball.xcor() > 380:
            ball.ball_reset()
            score.l_score += 1
            score.update_score()
        # logic for collifing to the left wall
        if ball.xcor() < -380:
            ball.ball_reset()
            score.r_score += 1
            score.update_score()

    screen.exitonclick()


if __name__ == '__main__':
    main()
