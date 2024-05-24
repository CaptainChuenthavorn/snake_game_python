from turtle import Turtle
import random

# Inheritance from Turtle
class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.color("Blue")
        self.shape("circle")
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.speed("fastest")
        self.penup()
        self.refresh()

    def refresh(self):
        random_x = random.randint(-14, 14) * 20
        random_y = random.randint(-14, 14) * 20
        self.goto(random_x, random_y)
