#imported turtle module
import turtle

wind = turtle.Screen() #initial screen
wind.title('Ping Pong by Abdelrahman') #set the title of the windo
wind.bgcolor("black")
wind.setup(width=800, height=600)
wind.tracer(0) #stops the window from updating automatically

#paddle1
paddle1 = turtle.Turtle() #initializes the turtle shape
paddle1.speed(0) #sets the speed
paddle1.shape('square')
paddle1.color('blue')
paddle1.penup() #stops the object from drawing lines
paddle1.goto(-370, 0) #sets the position of the object
paddle1.shapesize(5,1) #stretches the shape to meet the size
#paddle2
paddle2 = turtle.Turtle()
paddle2.speed(0)
paddle2.shape('square')
paddle2.color('red')
paddle2.penup()
paddle2.goto(370, 0)
paddle2.shapesize(5,1)
#ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape('square')
ball.color('white')
ball.penup()
ball.goto(0, 0)
ball.shapesize(1,1)
ball.dx = 2.5
ball.dy = 2.5

#score
score1 = 0
score2 = 0
score = turtle.Turtle()
score.color("white")
score.speed(0)
score.hideturtle()
score.penup()
score.goto(0, 260)
score.write("Player 1: 0  Player 2: 0", align="center", font=("Courier", 24, "normal"))
#Fucntions
def paddle1_up(): #set the y coordinate of paddle1
     y= paddle1.ycor()
     y += 30
     paddle1.sety(y) #set the y of paddle1 to the new coordinate

def paddle1_down():
     y= paddle1.ycor()
     y -= 30
     paddle1.sety(y)     

def paddle2_up():
     y= paddle2.ycor()
     y += 30
     paddle2.sety(y)

def paddle2_down():
     y= paddle2.ycor()
     y -= 30
     paddle2.sety(y)     


#keyboard bindings
wind.listen() #tell the window to expect input
wind.onkeypress(paddle1_up, 'w')
wind.onkeypress(paddle1_down, 's') 
wind.onkeypress(paddle2_up, 'Up')
wind.onkeypress(paddle2_down, 'Down')           

#main game loop
while True:
    wind.update() #updates the screen everytime the loop runs
  # moves the ball
    ball.setx(ball.xcor() + 0.1 * ball.dx)  # Update x by 10% of dx
    ball.sety(ball.ycor() + 0.1 * ball.dy)  # Update y by 10% of dy


    #border checking
    if ball.ycor() > 290: #if the ball is at top border
        ball.sety(290)
        ball.dy *= -1
    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        score1 += 1
        score.clear()
        score.write("player 1: {} player 2: {}".format(score1, score2), align="center",font=("Courier", 24, "normal"))
    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score2 += 1
        score.clear()
        score.write("player 1: {} player 2: {}".format(score1, score2), align="center",font=("Courier", 24, "normal"))
    #paddle and ball collisions
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle2.ycor() + 40 and ball.ycor() > paddle2.ycor() - 40):
        ball.setx(340)
        ball.dx *= -1
    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle1.ycor() + 40 and ball.ycor() > paddle1.ycor() - 40):
        ball.setx(-340)
        ball.dx *= -1
    