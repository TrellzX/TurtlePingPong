import turtle as t
from turtle import *

# creating window

window = t.Screen()

window.title("Pong game!")
#making background black
window.bgcolor("black")

# setting window dimensions
window.setup(width=800, height=600)
#creating the pingpong bat
leftPaddle = t.Turtle()
leftPaddle.speed(0)
leftPaddle.shape("square")
leftPaddle.color("white")
#changing the square to look like a bat
leftPaddle.shapesize(stretch_wid=5, stretch_len=1)
leftPaddle.penup()
leftPaddle.goto(-350,0)










exitonclick()
