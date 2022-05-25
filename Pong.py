
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

#main game loop
while True:
    wn.update()
