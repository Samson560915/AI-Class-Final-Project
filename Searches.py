from Node import Node
import heapq

#Implements Breadth First Search based off of how far away the nodes are
def BFS(start, goal): #Given a start and a goal point
    start.reset_cost() #Reset the cost of the start (We use cost to determine the distance)
    start.parent = None #Make sure that the start state has no parent
    frontier = [start] #Set up our frontier
    visited = set() #Set up the visited nodes
    while frontier: #While there are items in the frontier
        curr = heapq.heappop(frontier) #Get the top item in the frontier
        if isinstance(curr, tuple): #If it is a tuple make it a node (here because we initialize start without a priority)
            curr = curr[1]
        visited.add(curr) #We have visited the current node
        if curr.x == goal.x and curr.y == goal.y: #Check if we have reached the goal
            return(curr.cost, curr.get_path_from_root()) #Return how much distance it was and the path
        for child in curr.children: 
            if child not in visited and child not in frontier: #Make sure we haven't already seen the children
                child.reset_cost() #reset cost so we can track distance accurately
                child.cost = curr.cost + child.get_dist(curr) #track distance
                child.parent = curr #set parent in order to find the path back to the starting node
                heapq.heappush(frontier, (child.cost, child)) #Add to the frontier based on the distance from the starting node
    return(float('inf'), None) #If we can't find a path, make sure it is top priority to build one
    

# Weighted Local Search (sort of like a travelling salesman heuristic), to give us a place to start off
def weighted_local(points):
    x_avg = 0 #find the average location of the points
    y_avg = 0
    for a in points:
        x, y = a
        x_avg += x
        y_avg += y
    x_avg /= len(points)
    y_avg /= len(points)

    max_d = float('-inf') #set a max distance (we want to start from the furthest point from the center of the points)
    far_point = None
    for a in range(len(points)): 
        x, y = points[a]
        d = ((x_avg - x) ** 2 + (y_avg - y) ** 2) ** 0.5
        if d > max_d: #find the max distance
            max_d = d
            far_point = a
    
    nodes = [] #create a list of nodes

    nodes.append(Node(points[far_point][0], points[far_point][1], None)) #Add the furthest point

    cur = nodes[-1] #set our current node to be the last one in the list
    del points[far_point] #delete the furthest point from the list of points
    while points: #while there are still values in points
        min = float('inf') #set a minimum value
        next_point = None #set a point to go to next
        for i in range(len(points)): #check all remaining points
            x, y = points[i]
            x_avg = 0
            y_avg = 0
            for a in points: #find the average location of the remaining points
                x1, y1 = a
                x_avg += x1
                y_avg += y1
            x_avg /= len(points)
            y_avg /= len(points)
            d = ((cur.x - x) ** 2 + (cur.y - y) ** 2) ** 0.5 #weight for how far each point is from current location
            d2 = ((x_avg - x) ** 2 + (y_avg - y) ** 2) ** 0.5 #second weight for how far away it is from the average
            weighted_sum = d - 0.25 * d2 #Calculate weighted sum
            if weighted_sum < min: #find the best weight
                min = weighted_sum
                next_point = i
        temp = nodes[-1]
        temp.add_child(Node(points[next_point][0], points[next_point][1], cur)) #add the new node as a child of the old node
        nodes.append(Node(points[next_point][0], points[next_point][1], cur)) #add the new node to the list
        cur = nodes[-1] #go on to the next node
        del points[next_point] #delete the used point from the list

    return nodes #return the list of nodes
