from turtle import Turtle

TILE_SIZE = 20
TILES_NUM = 4
SCALE = 0.2


class Board():

    def __init__(self):
        self.bar_list = []
        self.grid_list = []
        self.make_grid()

    def make_bar(self, start_y):
        for i in range(TILES_NUM):
            bod = Turtle("square")
            bod.shapesize(SCALE)
            bod.speed("fastest")
            bod.penup()
            bod.color("white")
            bod.goto(0, start_y + i * -(TILE_SIZE * SCALE))
            self.bar_list.append(self)

    def make_grid(self):
        for i in range(18):
            self.make_bar(280 - i * (TILE_SIZE * SCALE * TILES_NUM) * 2)
            self.grid_list.append(self.bar_list)
