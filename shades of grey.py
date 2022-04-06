import turtle
turtle.color("black", "white")
turtle.colormode(1.0)
turtle.speed(0)
SQUARES = 50
SIDE = 150
shade = 1.0
turtle.write("Shades of Grey", move=True, align='left')
for count in range(SQUARES):
    turtle.fillcolor(shade, shade, shade)
    turtle.begin_fill()
    turtle.left(360 // SQUARES)
    for side in range(4):
        turtle.forward(SIDE)
        turtle.left(90)
    turtle.end_fill()
    shade -= turtle.colormode() / float(SQUARES)
turtle.write('Abhinav')
turtle.done()
