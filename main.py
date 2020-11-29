from turtle import Screen
from bar import Bar, HEIGHT, WIDTH, UPPERBOUNDARY, LOWERBOUNDARY
from board import Board
from ball import Ball
from scoreboard import Scoreboard
import time


screen = Screen()
screen.setup(width=WIDTH, height=HEIGHT)
screen.bgcolor('black')
screen.tracer(0)
screen.title("Pong")


player_bar = Bar(-((WIDTH/2)-30))
enemy_bar = Bar(((WIDTH/2)-30))
board = Board()
ball = Ball()
player_score = Scoreboard("player")
enemy_score = Scoreboard("enemy")
screen.update()


screen.listen()
screen.onkey(player_bar.go_up,"w")
screen.onkey(player_bar.go_down,"s")
screen.onkey(enemy_bar.go_up,"Up")
screen.onkey(enemy_bar.go_down,"Down")


enemy_up = True
game_on = True
while game_on:
    screen.update()
    time.sleep(ball.play_speed)
    ball.move()

    # if enemy_bar.ycor() > UPPERBOUNDARY or enemy_bar.ycor() < LOWERBOUNDARY:
    #     enemy_up = not enemy_up

    # if enemy_up:
    #     enemy_bar.go_up()
    # else:
    #     enemy_bar.go_down()

    if ball.ycor() > 270 or ball.ycor() < -270:
        ball.invert_y()

    if ball.xcor() > 470:
        player_score.score_up("player")
        ball.start()
    elif ball.xcor() < -470:
        enemy_score.score_up("enemy")
        ball.start()

    if ball.distance(enemy_bar) < 50 and ball.xcor() > 440 or ball.distance(player_bar) < 50 and ball.xcor() < -440:
        print("Touch")
        ball.invert_x()


screen.exitonclick()