import turtle

def draw(nodes):
    window = turtle.Screen()
    pen = turtle.Turtle()
    pen.width(5)
    pen.penup()
    pen.setpos(nodes[0].x, nodes[0].y)
    pen.pendown()
    for a in nodes:
        pen.goto(a.x,a.y)
        pen.dot(25, "blue")

    window.exitonclick()