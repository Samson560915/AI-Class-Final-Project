from Searches import BFS
from Node import Node
import heapq

#Finds all possible paths that can be taken then puts them into a priority queue with the most important one in front
def check_paths(nodes):
    possible_paths = [] #paths that can be taken
    for n1 in nodes:
        for n2 in nodes: #Check all sets of two nodes
            d = n1.get_dist(n2) #Find the straight-line distance between the two nodes
            curr_d, temp = BFS(n1, n2) #Find our best current path there with our current paths using Breadth-First Search
            r = 0
            if d != 0: #makes sure n1 is not n2
                r = -curr_d/d #As priority queues are stored with lowest priority first, we put the negative sign to make sure the highest priority is the lowest
            heapq.heappush(possible_paths, (r, (n1, n2))) #Add the path to possible_paths in the correct order
    return(possible_paths) 

#Adds the best path to maximize priority
def add_path(nodes):
    possible_paths = check_paths(nodes) #Find possible paths to add
    priority, path = heapq.heappop(possible_paths) #Get the highest priority path (remember that it is negative so it is stored as the lowest)
    path[0].add_child(path[1]) #Add the paths 
    path[1].add_child(path[0])
    priority, path = heapq.heappop(possible_paths)
    return(-priority)

#Deletes the worst path
def del_path(nodes):
    min = float('inf')
    second_worst = min
    node1 = None
    node2 = None
    for n1 in nodes: 
        for child in n1.children: #Checks all nodes that have direct access to each other to see if our search is able to come up with a good alternate solution in order to delete it
            d = n1.get_dist(child) #Finds the current distance 
            n1.del_child(child) #Deletes the path temporarily
            child.del_child(n1) 
            curr_d, path = BFS(n1, child) #Checks our paths to see we still have a good solution to get from a to be
            r = curr_d/d #Calculate ratio
            second_worst = min
            if r <= min: #Set worst ratio
                min = r
                node1 = n1
                node2 = child
            n1.add_child(child) #Re-add the path back in which was deleted on lines 33-34 
            child.add_child(n1)
    node1.del_child(node2) #Delete the worst path by the ratio
    node2.del_child(node1)
    return(second_worst)




