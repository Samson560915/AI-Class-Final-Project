import turtle

def draw(paths):
    window = turtle.Screen()
    pen = turtle.Turtle()
    pen.width(5)
    
    for a in paths:
        pen.penup()
        pen.setpos(a[0].x, a[0].y)
        pen.pendown()
        pen.dot(25, "blue")
        pen.goto(a[1].x, a[1].y)
        pen.dot(25, "blue")

    window.exitonclick()