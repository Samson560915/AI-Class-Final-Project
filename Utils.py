import math
import random

def get_circle_points(num_points=20, radius=1.0, center=(0, 0)):
    points = []
    cx, cy = center
    
    for i in range(num_points):
        # Calculate the angle for the current point
        angle = 2 * math.pi * i / num_points
        
        # Calculate x and y coordinates
        x = cx + radius * math.cos(angle)
        y = cy + radius * math.sin(angle)
        
        points.append((x, y))
        
    return points

def get_points(num):
    s = []
    for i in range(num):
        x = random.randint(-600, 600)
        y = random.randint(-400, 400)
        s.append((x, y))
    return s

def get_nodes(num):
    nodes = []
    for p in get_points(num):
        nodes.append(Node(p[0],p[1],None))
    return nodes
