
import turtle

wn = turtle.Screen()
wn.title("Pong by @RamenGames")
wn.bgcolor("black")
wn.setup(width=800, height=600)
# stops window from updating and allows manual updates for faster game mechanics
wn.tracer(0)


#main game loop
while True:
    wn.update()
