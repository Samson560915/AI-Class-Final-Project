class Node:
    def __init__(self, pos_x, pos_y, parent):
        self.x = pos_x
        self.y = pos_y
        self.parent = parent
        self.children = []
        self.cost = 0
        if parent:
            self.children.append(parent)
    
    def cost(self):
        edge_cost = ((self.parent.x - self.x) ** 2 + (self.parent.y - self.y) ** 2) ** 0.5
        self.cost = self.parent.cost + edge_cost
    
    def reset_cost(self):
        self.cost = 0
    
    def get_dist(self, other):
        return (((self.x - other.x) ** 2 + (self.y - other.y) ** 2) ** 0.5)
    
    def add_child(self, child):
        self.children.append(child)
    
    def get_path_from_root(self, start):
        node = self
        path = [node]
        while not node == start:
            node = node.parent
            path.append(node)
        path.reverse()
        return(path)