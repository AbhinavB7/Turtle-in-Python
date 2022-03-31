import turtle

turtle.speed(0)
turtle.bgcolor("black")
for i in range(5):
    for colours in ("violet", "indigo", "blue", "cyan", "green", "yellow", "orange", "red"):
        turtle.color(colours)
        turtle.pensize(2)
        turtle.left(7)
        turtle.forward(260)
        turtle.left(90)
        turtle.forward(260)
        turtle.left(90)
        turtle.forward(260)
        turtle.left(90)
        turtle.forward(260)
        turtle.left(90)