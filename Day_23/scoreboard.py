from turtle import Turtle
FONT = ("Courier", 24, "normal")
ALINGMENT = "center"


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()

        self.score = 0
        self.color("black")
        self.hideturtle()
        self.penup()
        self.goto(-240, 260)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Level {self.score}", align=ALINGMENT,
                   font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write(f"Game Over", align=ALINGMENT,
                   font=FONT)
