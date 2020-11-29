from turtle import Turtle

STARTING_SPEED = 0.05
SPEED_INCREASE_RATE = 0.1
Z_SQUARED = 401
UPPER_BOUND = 20
LOWER_BOUND = -20

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.speed("fastest")
        self.shape("square")
        self.penup()
        self.color("white")
        self.y_movement = 10
        self.x_movement = 10
        self.x_positive = True
        self.play_speed = STARTING_SPEED


    def start(self):
        self.invert_x()
        self.play_speed = STARTING_SPEED
        self.goto(0, 0)



    def move(self):
        new_x = self.xcor() + self.x_movement
        new_y = self.ycor() + self.y_movement
        self.goto(new_x, new_y)


    def invert_y(self):
        self.y_movement = self.y_movement * -1


    def invert_x(self):
        self.x_movement *= -1
        self.increase_speed()

    def increase_speed(self):
        self.play_speed *= (1 - SPEED_INCREASE_RATE)
