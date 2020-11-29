from turtle import Turtle

SIDES = {"enemy": 100, "player": -100}


class Scoreboard(Turtle):

    def __init__(self, side):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.show_score(side)


    def show_score(self, side):
        self.clear()
        self.goto(SIDES[side], 200)
        self.write(self.score, align="center", font=("Courier", 80, "normal"))

    def score_up(self, side):
        self.score += 1
        self.show_score(side)