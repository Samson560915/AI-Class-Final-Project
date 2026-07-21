from Searches import BFS
from Node import Node
import heapq

def check_paths(nodes):
    possible_paths = []
    for n1 in nodes:
        for n2 in nodes:
            d = n1.get_dist(n2)
            curr_d = BFS(n1, n2)
            if curr_d is None:
                curr_d = 0
            r = 0
            if d != 0:
                r = curr_d/d
            heapq.heappush(possible_paths, (r, ((n1.x,n1.y), (n2.x,n2.y))))
    return(possible_paths) 

def add_path(paths, nodes):
    possible_paths = check_paths(nodes)
    new_paths = paths.copy()
    for p in range(len(possible_paths)):
        priority, path = heapq.heappop(possible_paths)
        if priority > 5: #TODO: CHANGE THIS VALUE
            new_paths.add(path)
    return(new_paths)

def del_path(paths, nodes):
    possible_paths = check_paths(nodes)
    new_paths = paths.copy()
    for p in range(len(possible_paths)):
        priority, path = heapq.heappop(possible_paths)
        if priority < 7: #TODO: CHANGE THIS VALUE
            new_paths.discard(path)
    return(new_paths)
    




