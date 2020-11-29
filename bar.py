from turtle import Turtle

WIDTH = 1000
HEIGHT = 600
UPPERBOUNDARY = (HEIGHT / 2) - 80
LOWERBOUNDARY = -(HEIGHT / 2) + 80
TILE_SIZE = 20
TILES_HEIGHT = 5
STEP = 40

class Bar(Turtle):
    def __init__(self, deslocation):
        super().__init__()
        self.deslocation = deslocation
        self.make_bar()

    def make_bar(self):
        self.shape("square")
        self.shapesize(TILES_HEIGHT, 1)
        self.speed("fastest")
        self.penup()
        self.color("white")
        self.goto(self.deslocation, 0)

    def go_up(self):
        if self.ycor() <= UPPERBOUNDARY:
            new_y = self.ycor() + STEP
            self.goto(self.xcor(), new_y)


    def go_down(self):
        if self.ycor() >= LOWERBOUNDARY:
            new_y = self.ycor() - STEP
            self.goto(self.xcor(), new_y)
