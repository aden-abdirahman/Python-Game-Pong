
import turtle

wn = turtle.Screen()
wn.title("Pong by @RamenGames")
wn.bgcolor("black")
wn.setup(width=800, height=600)
# stops window from updating and allows manual updates for faster game mechanics
wn.tracer(0)


# Paddle A
# paddle a is a turtke object, small t for module name, capital T for class name
paddle_a = turtle.Turtle()
# not speed that the paddle moves but the speed of animation, sets the speed to the maximum speed
paddle_a.speed(0)
# built in turtle module, sets the shape of the paddle. each shape is 20px x 20px
paddle_a.shape("square")
# stretching width to 100px(5x20) and len stays the same
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.color("white")
# turtle by default draws lines so penup is used to not do that
paddle_a.penup()
#sets paddle to the middle of the screen vertically, and to the left side of the screen horizontally
paddle_a.goto(-350, 0)



# Paddle B
paddle_b = turtle.Turtle()

paddle_b.speed(0)

paddle_b.shape("square")

paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.color("white")

paddle_b.penup()

paddle_b.goto(+350, 0)


# Ball
ball = turtle.Turtle()

ball.speed(0)

ball.shape("circle")

ball.color("white")

ball.penup()

ball.goto(0, 0)
# d means delta(change), everytime our ball moves it moves by 2px
ball.dx = 2
ball.dy = 2

# Functions

#defining the paddles upward movement 
def paddle_a_up():
    # ycor is the y coordinate of the turtle object. ycor is a property of the turtle object
    y = paddle_a.ycor()
    # adding 20px to yc coordinate
    y += 20
    paddle_a.sety(y)

def paddle_a_down():
    y = paddle_a.ycor()
    # subtracting 20px to yc coordinate
    y -= 20
    paddle_a.sety(y)

def paddle_b_up():
    y = paddle_b.ycor()
    # subtracting 20px to yc coordinate
    y += 20
    paddle_b.sety(y)

def paddle_b_down():
    y = paddle_b.ycor()
    # subtracting 20px to yc coordinate
    y -= 20
    paddle_b.sety(y)

# Keyboard binding
#built in methods in turtle for key events
wn.listen()
# when user presses "w" call function paddle_a_up
wn.onkeypress(paddle_a_up, "w")
# when user presses "s" call function paddle_a_down
wn.onkeypress(paddle_a_down, "s")
    
wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_down, "Down")
    

#main game loop
while True:
    wn.update()

    # Ball movement
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border checking
    #if current ycor is greater than 290(since ball is 20x20 and starts at center)
    if ball.ycor() > 290:
        #sets it back to 290(the border)
        ball.sety(290)
        #since dy is 2 multiplying it by -1 sets it to -2 to reverse movement
        ball.dy *= -1

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    # horizontal border conditions
    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1

    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1