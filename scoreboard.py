from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self) -> Turtle:
        super().__init__()
        self.score = 1
        self.hideturtle()
        self.penup()
        self.color('black')
        self.goto(x=-210, y=260)
        self.get_level()

    def increase_score(self):
        self.score += 1
        self.get_level()

    def get_level(self):
        self.clear()
        self.write(f"Level: {self.score}", move=False, align='center', font=FONT)

    def game_over(self):
        self.goto(x=0, y=0)
        self.write("Game over.", move=False, align='center', font=FONT)
