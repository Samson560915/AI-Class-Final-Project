from Node import Node
from Searches import a_star, local
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

draw(nodes)