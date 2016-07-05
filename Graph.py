# Node has indexes L , F and two dicts of in and out node
class Node:    
    def __getitem__(self, key):
        return self.Arrows[key]
    def __init__(self,name):
        self.L = ()
        self.F = ()
        self.Out = {}
        self.In = {}
        self.Name = name
    def add_arrow(b_node,e_node,weight):
        b_node.Out[e_node] = weight
        e_node.In[b_node] = -weight
