import turtle
import random
from Searches import BFS

def draw(nodes, line_color="gray", dot_color="black"):
    paths = get_paths(nodes)
    turtle.colormode(255)
    window = turtle.Screen()
    pen = turtle.Turtle()
    pen.color(line_color)
    pen.width(5)
    pen.hideturtle()
    background(pen, paths, window, 2, 300)
    pen.speed(1000)
    draw_nodes(pen, nodes, "yellow", 25)

    for a in paths:
        #pen.pencolor(random.randint(1,255),random.randint(1,255),random.randint(1,255))
        pen.penup()
        pen.setpos(a[0][0], a[0][1])
        pen.pendown()
        pen.goto(a[1][0], a[1][1])

    draw_nodes(pen, nodes, "black", 15)

    window.exitonclick()

def draw_nodes(pen, nodes, dot_color="green", dot_size = 15):
    for n in nodes:
        pen.penup()
        pen.setpos(n.x, n.y)
        pen.dot(dot_size, dot_color)

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

def background(pen, nodes, window, num, size):
    window.bgcolor("navy")
    pen.penup()
    for node in nodes:
        for i in range(num):
            x = random.uniform(-size/2, size/2)
            y = random.uniform(-((size/2)**2-x**2)**0.5, ((size/2)**2-x**2)**0.5)
            pen.goto(node[0][0] + x, node[0][1] + y)
            pen.dot(size, "DarkGreen")
            x = random.uniform(-size/2, size/2)
            y = random.uniform(-((size/2)**2-x**2)**0.5, ((size/2)**2-x**2)**0.5)
            pen.goto(node[1][0] + x, node[1][1] + y)
            pen.dot(size, "DarkGreen")
        