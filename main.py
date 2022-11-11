from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("pong")
screen.tracer(0)
r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(r_paddle.move_up, key="Up")
screen.onkey(r_paddle.move_down, key="Down")

screen.onkey(l_paddle.move_up, key="w")
screen.onkey(l_paddle.move_down, key="s")

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    # detect collision with top wall and bounce
    ball.if_bounce_y()
    print(l_paddle.paddle_posy())
    r_paddle.paddle_posy()
    #print(ball.ball_posx())
    #scoreboard.l_point()
    print(ball.xcor())


    # detect collision with right paddle


    #detect when r_paddle misses
    if ball.ball_posx() > 340:
        ball.reset_position()
        scoreboard.l_point()

    # detect when l_paddle misses
    if ball.ball_posx() < -340:
        ball.reset_position()
        scoreboard.r_point()

screen.exitonclick()
