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
        for i in range(len(self.children)):
            if child == self.children[i]:
                return False
        self.children.append(child)
        return True

    def del_child(self, child):
        for i in range(len(self.children)):
            if child == self.children[i]:
                del self.children[i]
                return True
        return False
    
    def get_path_from_root(self):
        node = self
        path = [node]
        while node.parent is not None:
            node = node.parent
            path.append(node)
        path.reverse()
        return(path)
    
    def __eq__(self, other):
        if not isinstance(other, Node):
            return False
        return self.x == other.x and self.y == other.y
    
    def __lt__(self, other):
        if not isinstance(other, Node):
            return NotImplemented
        # Define how to sort nodes (e.g., alphabetically by name, or by ID)
        return self.x < other.x
    
    def __hash__(self):
        # 1. Combine your identifying attributes into a tuple
        # 2. Pass that tuple into the built-in hash() function
        return hash((self.x, self.y))
    
