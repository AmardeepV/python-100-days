from turtle import Turtle

ALINGMENT = "center"
FONT = ("Arial", 80, "normal")


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()

        self.l_score = 0
        self.r_score = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.update_score()

    def update_score(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.l_score, align=ALINGMENT,
                   font=FONT)
        self.goto(100, 200)
        self.write(self.r_score, align=ALINGMENT,
                   font=FONT)
