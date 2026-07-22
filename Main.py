from Node import Node
from Searches import BFS, weighted_local
from Draw import draw, draw_old, get_paths
from Determine_Path import add_path, del_path
import random

def get_points(num):
    s = []
    for i in range(num):
        x = random.randint(-400, 400)
        y = random.randint(-400, 400)
        s.append((x, y))
    return s

points = get_points(10)

def get_nodes(num):
    nodes = []
    for p in get_points(num):
        nodes.append(Node(p[0],p[1],None))
    return nodes

#print(points)

nodes = weighted_local(points)
#nodes = get_nodes(20)
#for i in nodes:
#    print((i.x,i.y))

paths = get_paths(nodes) #Paths will be a list of tuples of Node objects (start node, end node)

for i in range(10):
    for i in range(5):
        add_path(nodes)
        #add_path(nodes)
    del_path(nodes)


#for i in range(2):
#    del_path(nodes)

#should_run = True
#while should_run:
#    should_run = False
#    if (random.uniform(0,1) > 0.45):
#        add_path(nodes)
#    else:
#        del_path(nodes)
#    for n1 in nodes:
#        for n2 in nodes:
#            if n1 != n2:
#                check = BFS(n1,n2)[0]/n1.get_dist(n2) 
#                if (check>4):
#                    should_run = True

#for i in paths:
#    print((i[0][0], i[0][1])) 
#    print((i[1][0], i[1][1]))

paths = get_paths(nodes)

draw(nodes)
