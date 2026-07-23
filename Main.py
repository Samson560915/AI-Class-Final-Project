from Node import Node
from Searches import BFS, weighted_local
from Draw import draw, get_paths
from Determine_Path import add_path, del_path
import random

def get_points(num):
    s = []
    for i in range(num):
        x = random.randint(-400, 400)
        y = random.randint(-400, 400)
        s.append((x, y))
    return s

points = get_points(20)

def get_nodes(num):
    nodes = []
    for p in get_points(num):
        nodes.append(Node(p[0],p[1],None))
    return nodes


nodes = weighted_local(points)


paths = get_paths(nodes) #Paths will be a list of tuples of Node objects (start node, end node)

# for i in range(10):
#     for i in range(5):
#         add_path(nodes)
#     del_path(nodes)

should_add = True
should_del = True
while should_add or should_del:
    if should_add:
        upper = add_path(nodes)
    if should_del:
        lower = del_path(nodes)
    if upper <= 2.5:
        should_add = False
    if lower >= 2.5:
        should_del = False


paths = get_paths(nodes)

draw(nodes)
