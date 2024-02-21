from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.return_back()
        self.left(90)


    def move(self):
        new_y = self.ycor() + MOVE_DISTANCE
        self.goto(self.xcor(), new_y)


    def return_back(self):
        self.goto(STARTING_POSITION)

    def game_over(self):
        self.color("black")
        self.penup()
        self.goto(0,0)
        self.hideturtle()
        self.write("Game Over!", align="center", font=("Courier", 24, "normal"))