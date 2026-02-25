from turtle import Turtle

ALINGMENT = "center"
FONT = ("Arial", 24, "normal")
SCORE_FILE = "score.txt"


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open(SCORE_FILE) as file:
            self.high_score = int(file.read())

        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, 270)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()

        self.write(f"Score {self.score} High score: {self.high_score}", align=ALINGMENT,
                   font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open(SCORE_FILE, 'w') as file:
                file.write(f"{self.high_score}")
        self.score = 0
        self.update_scoreboard()

    def update_score(self):
        self.score += 1
        self.update_scoreboard()
