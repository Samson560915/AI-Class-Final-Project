from Node import Node
from Searches import a_star, local
import random

def get_points(num):
    s = []
    for i in range(num):
        x = random.randint(1, 10)
        y = random.randint(1, 10)
        s.append((x, y))
    return s

points = get_points(5)
print(points)

for i in local(points):
    print((i.x,i.y))