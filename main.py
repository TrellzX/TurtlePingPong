import turtle as t
from turtle import *

# creating window

window = t.Screen()

window.title("Pong game!")
#making background black
window.bgcolor("black")
#variable for scoring
playerAscore = 0
playerBscore = 0
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

#creating ball
ball = t.Turtle()
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0,0)

#making pen
pen = t.Turtle()
pen.speed(0)
pen.color("blue")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("SCORE", align="center", font=("Ariel", 24, "normal"))

#paddle up (right)
def rightPaddleUp():
    y = rightPaddle.ycor()
    y = y+15
    rightPaddle.sety(y)

#paddle down (right)
def rightPaddleDown():
    y = rightPaddle.ycor()
    y = y-15
    rightPaddle.sety(y)

#paddle up (left)
def leftPaddleUp():
    y = leftPaddle.ycor()
    y = y+15
    leftPaddle.sety(y)

#paddle down (left)
def leftPaddleDown():
    y = leftPaddle.ycor()
    y = y-15
    leftPaddle.sety(y)

#ball movement
ballDirectrionX = 4
ballDirectrionY = 4

#creating keybinds
window.listen()
window.onkey(rightPaddleUp,         "Up")
window.onkey(rightPaddleDown,       "Down")
window.onkey(leftPaddleUp,          "w")
window.onkey(leftPaddleDown,        "s")

#game loop

while True:
    window.update()

    #moving ball
    ball.setx(ball.xcor()+ballDirectrionX)
    ball.sety(ball.ycor() + ballDirectrionY)

#right top border
    if ball.ycor() > 290:
        ball.sety(290)
        ballDirectrionY *=-1
#left top border
    if ball.ycor() < -290:
        ball.sety(-290)
        ballDirectrionY *=-1
#Checking if the ball has hit the rightwall
    if ball.xcor() > 390:
        #bringing the ball back to the middle after it scores
        ball.goto(0,0)
        # moving the ball opposite side
        ballDirectrionX *=-1
        #inreasing player A's score
        playerAscore += 1
        pen.clear()
        #Typing the score
        pen.write("Player A: {}               "
                  "Player B  {}".format(playerAscore,playerBscore), align="center",font=("Monaco", 24 , "bold"))










exitonclick()
