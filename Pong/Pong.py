import turtle
import winsound


wn = turtle.Screen()
wn.title("Pong by Harley")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

# Score
score_a = 0
score_b = 0




#Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
#Default size is 20px x 20px
paddle_a.shapesize(stretch_wid=5, stretch_len=1)

paddle_a.penup()
paddle_a.goto(-350, 0)


#Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")

#Default size is 20px x 20px
paddle_b.shapesize(stretch_wid=5, stretch_len=1)

paddle_b.penup()
paddle_b.goto(350, 0)


#Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("green")
#Default size is 20px x 20px
ball.penup()
ball.goto(0, 0)
ball.dx = 0.2 #Moves by 2 pixels on x axis
ball.dy = 0.2 #Moves by 2 pixels on y axis


# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("| Player A: 0 |      | Player B: 0 | ", align="center", font=("Courier", 24, "normal"))


#Functions
#Paddle a controls
def paddle_a_up():
    y = paddle_a.ycor() #Current y coordinate of paddle a and assign it to variable y
    y += 20 #Subtracts 20px from Y coordinate
    paddle_a.sety(y)


def paddle_a_down():
    y = paddle_a.ycor() #Current y coordinate of paddle a and assign it to variable y
    y -= 20 #Adds 20px to Y coordinate
    paddle_a.sety(y)

#Paddle b controls
def paddle_b_up():
    y = paddle_b.ycor() #Current y coordinate of paddle a and assign it to variable y
    y += 20 #Subtracts 20px from Y coordinate
    paddle_b.sety(y)


def paddle_b_down():
    y = paddle_b.ycor() #Current y coordinate of paddle a and assign it to variable y
    y -= 20 #Adds 20px to Y coordinate
    paddle_b.sety(y)


#Keyboard bindings
wn.listen() #listen for keyboard input
wn.onkeypress(paddle_a_up, "w") #When w is pressed calls function paddle_a_up (which adds 20 to y coordinate)
wn.onkeypress(paddle_a_down, "s")
wn.onkeypress(paddle_b_up, "Up") #Whenup arrow is pressed calls function paddle_b_up (which adds 20 to y coordinate)
wn.onkeypress(paddle_b_down, "Down")

# Game Loop
while True:
    wn.update()

    #Move the ball
    ball.setx(ball.xcor() + ball.dx) #Ball starts at 0,0 then moves 2px on x axis
    ball.sety(ball.ycor() + ball.dy) #Ball starts at 0,0 then moves 2px on y axis

    #Border checks
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1 #Reverses direction of ball
        winsound.PlaySound("F:\Downloads\ping_pong_8bit_beeep", winsound.SND_ASYNC)
        delay = input

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1 #Reverses direction of ball
        winsound.PlaySound("F:\Downloads\ping_pong_8bit_beeep", winsound.SND_ASYNC)
        delay = input

    if ball.xcor() > 395:
        ball.goto(0, 0)
        ball.dx *= -1
        score_a += 1
        pen.clear()
        pen.write("| Player A: {} |      | Player B: {} | ".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))

    if ball.xcor() < -395:
        ball.goto(0, 0)
        ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.write("| Player A: {} |      | Player B: {} | ".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))

#Ball collisions with paddles
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor() + 40 and ball.ycor() > paddle_b.ycor() -40):
        ball.setx(340)
        ball.dx *= -1
        winsound.PlaySound("F:\Downloads\ping_pong_8bit_plop", winsound.SND_ASYNC) #Sound files included but will need to be changed based on your download directory
        delay = input

    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_a.ycor() + 40 and ball.ycor() > paddle_a.ycor() -40):
        ball.setx(-340)
        ball.dx *= -1
        winsound.PlaySound("F:\Downloads\ping_pong_8bit_plop", winsound.SND_ASYNC) #Sound files included but will need to be changed based on your download directory
        delay = input