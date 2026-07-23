import turtle
import random
from Searches import BFS

def draw(nodes, line_color="gray", background_color = "navy", islands_num = 1, island_size = 50, random_island_location = True, big_node_color = "yellow", big_node_size = 25, small_node_color = "black", small_node_size = 15, random_line_color = False, draw_background = True, should_draw_nodes = True, random_node_color = False):
    paths = get_paths(nodes)
    turtle.colormode(255)
    window = turtle.Screen()
    window.bgcolor(background_color)
    pen = turtle.Turtle()
    pen.color(line_color)
    pen.width(5)
    pen.hideturtle()
    if draw_background:
        background(nodes, window, islands_num, island_size, random_island_location)
    pen.speed(1000)
    if should_draw_nodes:
        draw_nodes(pen, nodes, big_node_color, big_node_size, random_node_color)

    for a in paths:
        if random_line_color:
            pen.pencolor(random.randint(1,255),random.randint(1,255),random.randint(1,255))
        pen.penup()
        pen.setpos(a[0][0], a[0][1])
        pen.pendown()
        pen.setpos(a[1][0], a[1][1])
    if should_draw_nodes:
        draw_nodes(pen, nodes, small_node_color, small_node_size, random_node_color)

    window.exitonclick()

def draw_nodes(pen, nodes, dot_color="green", dot_size = 15, random_node_color = False):
    for n in nodes:
        pen.penup()
        pen.setpos(n.x, n.y)
        if random_node_color:
            dot_color = (random.randint(1,255),random.randint(1,255),random.randint(1,255))
        pen.dot(dot_size, dot_color)

def get_paths(nodes):
    paths = set()
    for a in nodes:
        for b in a.children:
            if ((a.x,a.y),(b.x,b.y)) not in paths and ((b.x,b.y),(a.x,a.y)) not in paths:
                paths.add(((a.x,a.y),(b.x,b.y)))
    return paths

def get_points(nodes):
    points = set()
    for a in nodes:
        points.add((a.x, a.y))
    return points

def background(nodes, window, num, size, random_location = True):
    pen = turtle.Turtle()
    pen.hideturtle()
    pen.width(5)
    pen.speed(1000)
    pen.penup()
    points = get_points(nodes)    
    for p in points:
        for i in range(num):
            x = 0
            y = 0
            if random_location:
                x = random.uniform(-size/2, size/2)
                y = random.uniform(-((size/2)**2-x**2)**0.5, ((size/2)**2-x**2)**0.5)
            pen.setpos(p[0] + x, p[1] + y)
            
            pen.dot(size, "DarkGreen")
        
        