from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):

    def __init__(self) -> Turtle:
        super().__init__()
        self.penup()
        self.left(90)
        self.shape('turtle')
        self.color('medium sea green')
        self.reposition()

    def is_at_finish_line(self) -> bool:
        if self.ycor() > FINISH_LINE_Y:
            return True
        return False

    def reposition(self):
        self.goto(STARTING_POSITION)

    def move(self):
        self.goto(x=0, y=self.ycor() + MOVE_DISTANCE)
