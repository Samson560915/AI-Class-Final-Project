from Node import Node
from Searches import BFS, weighted_local
from Draw import draw, draw_old, get_paths, trace_path
import random

def get_points(num):
    s = []
    for i in range(num):
        x = random.randint(-300, 300)
        y = random.randint(-300, 300)
        s.append((x, y))
    return s

points = get_points(25)
print(points)

nodes = weighted_local(points)
for i in nodes:
    print((i.x,i.y))

paths = get_paths(nodes) #Paths will be a list of tuples of Node objects (start node, end node)
for i in paths:
    print((i[0].x, i[0].y),(i[1].x, i[1].y))
draw(paths)
trace_path(paths[0][0], paths[-1][0])