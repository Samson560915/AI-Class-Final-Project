import turtle

def draw(paths):
    window = turtle.Screen()
    pen = turtle.Turtle()
    pen.width(5)
    pen.hideturtle()
    pen.speed(1000)
    
    for a in paths:
        pen.penup()
        pen.setpos(a[0][0], a[0][1])
        pen.pendown()
        pen.dot(25, "blue")
        pen.goto(a[1][0], a[1][1])
        pen.dot(25, "blue")

    window.exitonclick()

def get_paths(nodes):
    paths = set()
    for a in nodes:
        for b in a.children:
            if ((a.x,a.y),(b.x,b.y)) not in paths and ((b.x,b.y),(a.x,a.y)) not in paths:
                paths.add(((a.x,a.y),(b.x,b.y)))
    return paths

def draw_old(paths):
    window = turtle.Screen()
    pen = turtle.Turtle()
    pen.width(5)

    pen.penup()
    pen.setpos(paths[0].x, paths[0].y)
    pen.pendown()
    for a in paths:
        pen.goto(a.x, a.y)
        pen.dot(25, "blue")

    window.exitonclick()