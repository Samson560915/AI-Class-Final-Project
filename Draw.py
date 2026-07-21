import turtle
from Searches import BFS

def draw(paths, line_color="black", dot_color="blue"):
    window = turtle.Screen()
    pen = turtle.Turtle()
    pen.color(line_color)
    pen.width(5)
    pen.speed(1000)
    
    for a in paths:
        pen.penup()
        pen.setpos(a[0].x, a[0].y)
        pen.pendown()
        pen.dot(25, dot_color)
        pen.goto(a[1].x, a[1].y)
        pen.dot(25, dot_color)

    window.exitonclick()

def get_paths(nodes):
    paths_list = []
    for a in nodes:
        for b in a.children:
            paths_list.append((a,b))
    return paths_list

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

def trace_path(start, end):
    path = BFS(start, end)

    paths_taken = []
    for i in range(len(path) - 1):
        paths_taken.append((path[i], path[i + 1]))
    
    draw(paths_taken, "pink", "red")
