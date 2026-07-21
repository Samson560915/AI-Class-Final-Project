from Node import Node
from Searches import BFS, weighted_local
from Draw import draw, draw_old, get_paths
from Determine_Path import add_path, del_path
import random

def get_points(num):
    s = []
    for i in range(num):
        x = random.randint(-300, 300)
        y = random.randint(-300, 300)
        s.append((x, y))
    return s

points = get_points(20)
print(points)

nodes = weighted_local(points)
for i in nodes:
    print((i.x,i.y))

paths = get_paths(nodes) #Paths will be a list of tuples of Node objects (start node, end node)
for i in paths:
    print((i[0][0], i[0][1]),(i[1][0], i[1][1]))
for i in range(10):
    paths = add_path(paths, nodes)
    paths = del_path(paths, nodes)

draw(paths)