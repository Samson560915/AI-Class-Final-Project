from Node import Node

def a_star(nodes, paths):
    pass

def local(points):
    x_avg = 0
    y_avg = 0
    for a in points:
        x, y = a
        x_avg += x
        y_avg += y
    x_avg /= len(points)
    y_avg /= len(points)

    max_d = float('-inf')
    far_point = None
    for a in range(len(points)):
        x, y = points[a]
        d = ((x_avg - x) ** 2 + (y_avg - y) ** 2) ** 0.5
        if d > max_d:
            max_d = d
            far_point = a
    
    nodes = []

    nodes.append(Node(points[far_point][0], points[far_point][1], None))

    cur = nodes[-1]
    del points[far_point]
    while points:
        min = float('inf')
        next_point = None
        for i in range(len(points)):
            x, y = points[i]
            d = ((cur.x - x) ** 2 + (cur.y - y) ** 2) ** 0.5
            if d < min:
                min = d
                next_point = i
        nodes.append(Node(points[next_point][0], points[next_point][1], cur))
        cur = nodes[-1]
        del points[next_point]

    return nodes
