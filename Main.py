from Node import Node
from Searches import BFS, local
from Draw import draw
import random

def get_points(num):
    s = []
    for i in range(num):
        x = random.randint(-400, 400)
        y = random.randint(-400, 400)
        s.append((x, y))
    return s

points = get_points(25)
print(points)

nodes = local(points)
for i in nodes:
    print((i.x,i.y))

paths = nodes #Paths will be a list of tuples of Node objects (start node, end node)
draw(paths)