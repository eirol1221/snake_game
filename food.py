from turtle import Turtle, Screen
from random import randint

screen = Screen()
screen.colormode(255)


class Food(Turtle):

    def __init__(self):
        super().__init__()
        rand_color = ()
        self.shape("turtle")
        self.up()
        # self.shapesize(stretch_len=1.0, stretch_wid=1.0)
        self.change_color()
        self.speed("fastest")
        rand_x = randint(-270, 270)
        rand_y = randint(-270, 270)
        self.goto(rand_x, rand_y)

    # transfer the food to another random position once the snake collided with the food
    def refresh(self):
        self.change_color()
        rand_x = randint(-280, 280)
        rand_y = randint(-280, 280)
        self.goto(rand_x, rand_y)

    # generate a random color of the food
    def change_color(self):
        r = randint(50, 255)
        g = randint(50, 255)
        b = randint(50, 255)
        rand_color = (r, g, b)
        self.color(rand_color)
