class Node:
    def __init__(self, pos_x, pos_y, parent):
        self.x = pos_x
        self.y = pos_y
        self.parent = parent

    def cost(self):
        edge_cost = ((self.parent.x - self.x) ** 2 + (self.parent.y - self.y) ** 2) ** 0.5
        self.cost = self.parent.cost + edge_cost
    