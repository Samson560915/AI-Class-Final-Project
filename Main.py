from Node import Node
from Searches import BFS, weighted_local
from Draw import draw, get_paths
from Determine_Path import check_paths, add_path, del_path, replace_path
from Code_Tests import test_two
from Utils import get_points, get_circle_points, get_nodes
from progress.bar import Bar
import time
import random
import math


#points = get_circle_points(20, 300)

start_time = time.perf_counter()
points = get_points(100)

us_metros = [
    (205.750, 37.279),    # New York City
    (-236.627, -29.327),  # Los Angeles
    (69.512, 48.8932),    # Chicago
    (-22.160, -42.082),   # Dallas
    (-7.888, -72.245),    # Houston
    (101.930, -32.359),   # Atlanta
    (175.441, 19.223),    # Washington D.C.
    (143.892, -112.232),  # Miami
    (194.158, 29.677),    # Philadelphia
    (-174.930, -35.365),  # Phoenix
    (235.221, 53.752),    # Boston
    (-227.945, -30.316),  # Riverside
    (-278.384, 7.900),    # San Francisco
    (115.352, 53.465),    # Detroit
    (-277.511, 106.213),  # Seattle
    (13.160, 79.929),     # Minneapolis
    (-225.801, -42.692),  # San Diego
    (121.238, -90.343),   # Tampa
    (-104.093, 27.543),   # Denver
    (179.9688, 23.055)    # Baltimore
]

# points = us_metros

nodes = weighted_local(points)


paths = get_paths(nodes) #Paths will be a list of tuples of Node objects (start node, end node)

count = 0
cont_add = True
cont_del = True
with Bar("start", max = len(nodes)*3, suffix ='%(percent).1f%% - %(eta)ds') as bar:
    while (cont_add or cont_del) and count < len(nodes)*3:
        cont_add = add_path(nodes, 3.1, True)
        cont_del = del_path(nodes, 3.1, True)
        count += 1
        bar.next()
        


priority = replace_path(nodes)
print(priority)
while priority > 0.6:
    print("hi")
    priority = replace_path(nodes)
    print(priority)


#draw(nodes, island_size = 200, islands_num = 3)
#draw(nodes, background_color = "moccasin", island_size = 0, big_node_size = 0, small_node_size = 0, line_color = "black", random_line_color=True)
draw(nodes = nodes, background_color = "white", random_line_color = True, draw_background = False, random_node_color = True)
#draw(nodes, background_color = "white", line_color = "black", draw_background = False, big_node_color = "gray")
#draw(nodes)

#test_two(1)
