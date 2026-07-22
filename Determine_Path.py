from Searches import BFS
from Node import Node
from Draw import get_paths
import heapq

def check_paths(nodes):
    possible_paths = []
    for n1 in nodes:
        for n2 in nodes:
            d = n1.get_dist(n2)
            curr_d, temp = BFS(n1, n2)
            #print(d, curr_d)
            if curr_d is None:
                curr_d = 0
            r = 0
            if d != 0:
                r = -curr_d/d
            #if r > 10:
            #    print("EONTUHEONTUHENOTH")
            #    print(d, curr_d)
            heapq.heappush(possible_paths, (r, (n1, n2)))
    return(possible_paths) 

def add_path(nodes):
    possible_paths = check_paths(nodes)
    priority, path = heapq.heappop(possible_paths)
    #for p in range(len(possible_paths)):
    #    priority, path = heapq.heappop(possible_paths)
    #    threshold = 0
    #    if possible_paths:
    #        threshold, temp = possible_paths[9*(len(possible_paths)//10)]
    #    if priority >= threshold: #TODO: CHANGE THIS VALUE
    #        print(priority, threshold)
    path[0].add_child(path[1])
    path[1].add_child(path[0])

# def del_path(nodes):
#     min = float('inf')
#     best_path = None
#     for n1 in nodes:
#         for n2 in nodes:
#             is_child = False
#             for child in n1.children:
#                 if n2 == child:
#                     is_child = True
#             if n1 != n2 and not is_child:
#                 d = n1.get_dist(n2)
#                 curr_d, path = BFS(n1, n2)
#                 r = curr_d/d
#                 if r <= min: #TODO: CHANGE THIS VALUE
#                     min = r
#                     best_path = path
#     if best_path is not None:
#         for i in range(len(best_path)-1):
#             best_path[i].del_child(best_path[i+1])
#             best_path[i+1].del_child(best_path[i])
                
def del_path(nodes):
    min = float('inf')
    node1 = None
    node2 = None
    for n1 in nodes:
        for child in n1.children:
            d = n1.get_dist(child)
            n1.del_child(child)
            child.del_child(n1)
            curr_d, path = BFS(n1, child)
            r = curr_d/d
            if r <= min: #TODO: CHANGE THIS VALUE
                min = r
                node1 = n1
                node2 = child
            n1.add_child(child)
            child.add_child(n1)
    node1.del_child(node2)
    node2.del_child(node1)




