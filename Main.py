from Node import Node
from Searches import BFS, weighted_local
from Draw import draw, draw_old
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

paths = nodes #Paths will be a list of tuples of Node objects (start node, end node)
draw_old(paths)