from turtle import Turtle
import random



# create a class food which inherits from the Turtle class
class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.generate_food()
        self.shape("circle")
        self.penup()
        # create a food with dim (10x10)
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("red")
        self.speed("fastest")

    def generate_food(self):
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)