from turtle import Turtle
from random import randint


class Food(Turtle):

    def __init__(self):
        super().__init__()
        # Initializing food properties
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("red")
        self.speed("fastest")

        self.width = (self.getscreen().canvwidth / 2) - 20
        self.height = (self.getscreen().canvheight / 2) - 20

        self.relocate()

    def relocate(self):
        rand_x = randint(self.width * -1, self.width)
        rand_y = randint(self.height * -1, self.height)
        self.goto(x=rand_x, y=rand_y)
