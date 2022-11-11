from turtle import Turtle

# Y_POSITION = 0
# X_POSITION = 0


class Ball():
    def __init__(self):
        super().__init__()
        self.ball = Turtle("circle")
        self.ball.color("white")
        self.ball.shapesize(.5, .50)
        self.ball.penup()
        self.move_speed = 0.1
        # self.ball.goto((X_POSITION, Y_POSITION))

        self.x_move = 8
        self.y_move = 7
        self.move()
        self.bounce_x()

    def move(self):
        new_x = self.ball.xcor() + self.x_move
        new_y = self.ball.ycor() + self.y_move
        self.ball.goto(new_x, new_y)
        # print(self.ball.ycor())

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1
        self.move_speed *= 0.9

    def reset_position(self):
        self.ball.goto(0, 0)
        self.move_speed = 0.1
        self.bounce_x()

    def if_bounce_y(self):
        if self.ball.ycor() > 280 or self.ball.ycor() < -280:
            self.bounce_y()

    def ball_posx(self):
        return self.ball.xcor()

    # def ball_posxx(self):
    #     return self.ball.xcor()
