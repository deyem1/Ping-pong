from turtle import Turtle

import ball
# from ball import Ball
#
# y = Ball.bounce_x


#


class Paddle(Turtle):
    def __init__(self, position):
        super(Paddle, self).__init__()

        self.paddle = Turtle("square")
        self.paddle.color("white")
        self.paddle.shapesize(5, 1)
        self.paddle.penup()
        self.paddle.goto(position)

    def move_up(self):
        new_y = self.paddle.ycor() + 20
        self.penup()
        self.paddle.goto(self.paddle.xcor(), new_y)

    def move_down(self):
        self.penup()
        new_y = self.paddle.ycor() - 20
        self.paddle.goto(self.paddle.xcor(), new_y)

    # def bounce_from_paddle(self):
    #     if self.ball.distance(self.paddle) < 50 and self.ball.xcor() > 340 or self.ball.distance(self.paddle) < 50 and self.ball.xcor() < -340:
    #         print("made contact")
    #         self.ball.bounce_x()

    def paddle_posx(self):
        return self.paddle.xcor()

    def paddle_posy(self):
        return self.paddle.ycor()


        # if ball.distance(self.paddle) < 50 and self.ball.xcor() > 340 or self.ball.distance(self.paddle) < 50 and self.ball.xcor() < -340:
        #     print("made contact")
        #     self.ball.bounce_x()
