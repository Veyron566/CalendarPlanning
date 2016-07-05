from graphviz import Digraph
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
    def stright_progn(self,initial_node):
        self.Begin.L = 0
        
        def change(node):
            node.L = mymax(initial_node.L+initial_node.Out[node],node.L)
        map(change, initial_node.Out)
        map(self.stright_progn , initial_node.Out.keys())
    def backward_progn (self,initial_node):
        self.End.F = self.End.L
        
        def change(node):
            node.F = mymin(initial_node.F+initial_node.In[node],node.F)
        map(change, initial_node.In)
        map(self.backward_progn ,initial_node.In)
    
    def get_arcs (self):
        def arcs_for_node(n):
            return map (lambda x:(n, x, n.Out[x]), n.Out)    
        return map (arcs_for_node,self.nodes)
   
    def to_file (self,d):
        f = Digraph('D',
                    filename = d, 
                    node_attr = {'shape': 'record'} )

        for i in self.nodes:
            f.node(str (i),(str (to_graphviz_record (i.Name,i.L,i.F,i.F-i.L))))
                   
      #to_graphviz_record(i.Name,i.L,i.F,i.F-i.L)             
        for i in sum (g.get_arcs(), []):
            f.edge(str ((i[0])),
                   str ((i[1])), 
                   label = str ( i[2]))
        return f

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

def to_graphviz_record (a,b,c,d):
    return str (a) + "|{" +  str(b) + "|" + str(c)+ "}|" + str (d)


# Some graph definition end output example
init = Node("init")
end = Node ("term")
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

g.stright_progn(g.Begin)
g.backward_progn(g.End)
g.to_file('mygraph.gv').view()
