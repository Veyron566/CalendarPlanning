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

# Class contains:
# List of nodes
# Initial and terminal mode
#
# Description of some methods that could be useful
class Graph:
    def __init__(self,b,e):
        self.Begin = b
        self.End = e
        self.nodes = {e,b}        
    def add_node (self,node):
        self.nodes.add(node)
    def stright_progn(self):
        self.Begin.L = 0
        initial_node = self.Begin
        def change(node):
            node.L = mymax(initial_node.L+initial_node.Out[node],node.L)
        map(change, initial_node.Out)
        map(stright_progn,initial_node.Out)
    def backward_progn (self):
        self.End.F = self.End.L
        initial_node = self.End
        def change(node):
            node.F = mymin(initial_node.F+initial_node.In[node],node.F)
        map(change, initial_node.In)
        map(backward_progn,initial_node.In)
    def get_arcs (self):
        def arcs_for_node(n):
            return map (lambda x:str (n.Name) +
                    "->" +str( x.Name),n.Out)    
        return map (arcs_for_node,self.nodes)

# Some procedures 
def mymax (a,b):
    if a == ():
        return b
    if b == ():
        return a
    return max(a,b)
def mymin (a,b):
    if a == ():
        return b
    if b == ():
        return a
    return min(a,b)

def fillfile (d):
    f = open(d, 'w')
    f.write("digraph mygraph \n{\n")
    for i in (map (lambda x: x.Name, g.nodes)):
        f.write(" "+str(i)+";\n")
    for i in sum ((g.get_arcs()),[]):
        f.write(" "+str (i)+";\n")
    f.write("}")

# Some graph definition end output example
init = Node("state_before_time")
end = Node ("state_after_time")
a = Node(1)
b = Node(2)
c = Node(3)
d = Node(4)
e = Node(5)
g = Graph(init,end)
map (g.add_node ,[a,b,c,d,e] )
Node.add_arrow(init,a,0)
Node.add_arrow(a,b,10)
Node.add_arrow(b,c,12)
Node.add_arrow(b,d,7)
Node.add_arrow(d,e,5)
Node.add_arrow(c,e,6)
Node.add_arrow(e,end,0)

fillfile('mygraph.dot')
