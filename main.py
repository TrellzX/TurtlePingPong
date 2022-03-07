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

#creating the pingpong bat
rightPaddle = t.Turtle()
rightPaddle.speed(0)
rightPaddle.shape("square")
rightPaddle.color("white")
#changing the square to look like a bat
rightPaddle.shapesize(stretch_wid=5, stretch_len=1)
rightPaddle.penup()
rightPaddle.goto(350,0)

ball = t.Turtle()
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(5,5)











exitonclick()
