from turtle import Turtle

FORMAT = "center"
FONT = ("Courier", 15, "bold")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.color("white")
        self.hideturtle()
        y_cor = (self.getscreen().canvheight - 40) / 2

        self.total = -1
        self.goto(x=0, y=y_cor)
        self.inc_score()

    def inc_score(self):
        """Adds a point to the user's score"""
        self.total += 1
        self.clear()
        self.write(f"Score: {self.total}", move=False, align=FORMAT, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER.", move=False, align=FORMAT, font=FONT)