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
def add_path(nodes, limit = 3.1, use_limit = False):
    possible_paths = check_paths(nodes) #Find possible paths to add
    priority, path = heapq.heappop(possible_paths) #Get the highest priority path (remember that it is negative so it is stored as the lowest)
    if (-priority >= limit and use_limit) or not use_limit:
        path[0].add_child(path[1]) #Add the paths 
        path[1].add_child(path[0])
        return True
    return False

#Deletes the worst path
def del_path(nodes, limit = 3.1, use_limit = False):
    paths_to_delete = []
    for n1 in nodes: 
        for child in n1.children: #Checks all nodes that have direct access to each other to see if our search is able to come up with a good alternate solution in order to delete it
            d = n1.get_dist(child) #Finds the current distance 
            n1.del_child(child) #Deletes the path temporarily
            child.del_child(n1) 
            curr_d, path = BFS(n1, child) #Checks our paths to see we still have a good solution to get from node 1 to node 2
            r = curr_d/d #Calculate ratio
            heapq.heappush(paths_to_delete, (r, (n1, child))) #Add the paths to a priority queue based on which one is the worst
            n1.add_child(child) #Re-add the path back in which was deleted on lines 33-34 
            child.add_child(n1)
    priority, path = heapq.heappop(paths_to_delete) #get the most useless path
    if (priority <= limit and use_limit) or not use_limit:
        path[0].del_child(path[1]) #Delete the worst path by the ratio
        path[1].del_child(path[0])
        return True
    return False

#make a function that is able to replace paths with better paths
def replace_path(nodes):
    replaced_paths = [] #create a priority queue of tuples with two tuples, the path deleted and the path added
    for n1 in nodes:
        for child in n1.children: #get all the children of a node
            to_child = n1.get_dist(child) #find the distance between the child and the original node     
            for n2 in nodes:
                not_a_child = True
                for c in n2.children: # check if n2 is a child of n1 #TODO: add check for if n2 == n1
                    if c == n1:
                        not_a_child = False
                if not_a_child: #if n2 is not a child of n1
                    pos_dist = n1.get_dist(n2) #get the distance between n2 and n1
                    if pos_dist < to_child: #make sure that this distance is less than that of the distance between n1 and the child
                        old_path_length, path = BFS(n1, child) #get the old path length of going from n1 to child
                        n1.del_child(child) #temporarily replace the path
                        child.del_child(n1)
                        n1.add_child(n2)
                        n2.add_child(n1)
                        new_path_length, path = BFS(n1, child) #get the new length of going from n1 to child
                        r = -(old_path_length/new_path_length) #create priority
                        heapq.heappush(replaced_paths, (r, ((n1, child), (n1, n2)))) #add this "replacement" to a priority queue
                        n1.add_child(child) #undo the temporary replacement
                        child.add_child(n1)
                        n1.del_child(n2)
                        n2.del_child(n1)
    priority, path = heapq.heappop(replaced_paths) #get the best possible replacement
    path[0][0].del_child(path[0][1]) #and push through the replacement
    path[0][1].del_child(path[0][0])
    path[1][0].add_child(path[1][1])
    path[1][1].add_child(path[1][0])
    priority, temp = heapq.heappop(replaced_paths) #get the priority of the next best replacement
    print(f"Parent: {path[0][0].x}, {path[0][0].y}, Original Destination: {path[0][1].x}, {path[0][1].y}, New Destination: {path[1][1].x}, {path[1][1].y}")
    return(-priority) #return the priority (because we made it negative earlier we must change it back)
                        


            




