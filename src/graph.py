from graphviz import Digraph
from node import Node
# Class contains:
# List of nodes
# Initial and terminal mode
#
# Description of some methods that could be useful
class Graph:
    Arrows= {}
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
    def simple_to_file (self,d):
        f = Digraph('D',
                    filename = d) 
        
        for i in self.nodes:
            f.node(str (i),str (i.Name))
                   
      #to_graphviz_record(i.Name,i.L,i.F,i.F-i.L)             
        for i in sum (self.get_arcs(), []):
            f.edge(str ((i[0])),
                   str ((i[1])), 
                   label = str ( i[2]))
        return f
    def to_file (self,d):
        f = Digraph('D',
                    filename = d, 
                    node_attr = {'shape': 'record'} )
        
        for i in self.nodes:
            f.node(str (i),(str (to_graphviz_record (i.Name,i.L,i.F,i.F-i.L))))
                   
      #to_graphviz_record(i.Name,i.L,i.F,i.F-i.L)             
        for i in sum (self.get_arcs(), []):
            f.edge(str ((i[0])),
                   str ((i[1])), 
                   label = str ( i[2]))
        return f
# Creating Graph From Data, where Data is List[(char, [Previous],time)]
    def __init__(self,Data):
        dat = ()
        nd = ()
        i = 1
        j = 0
        self.nodes = set()
        while  Data != []:
            dat = Data[j] # Data[j] is tuple like this ('A', ['C','D'], 3,5)
            prev = dat[1]
            name = dat[0]
            cost = dat[3]
            dur = dat [2]
            j =  j + 1
            if (prev == []):
                j = 0
                nd = Node(0)
                self.Begin = nd
                self.Arrows[name] = (nd,(),dur)
                Data.remove(dat)
                continue
            if(all (map (self.Arrows.has_key, prev))):
                j = 0
                Data.remove(dat)
                if (self.Arrows[prev[0]][1] == ()):
                    nd = Node(i)
                    i = i+1
                else:
                    nd = self.Arrows[prev[0]][1]
                
                self.Arrows[name] = (nd,(),dur)
                self.Arrows[prev[0]] =(self.Arrows[prev[0]][0],
                                       nd,
                                       self.Arrows[prev[0]][2])
                for n in prev[1:]:
                    
                    fict = Node (i)
                    self.add_node(fict)
                    i =  i + 1 
                    self.Arrows[n] = (self.Arrows[n][0],
                                       fict,
                                       self.Arrows[n][2])
                    Node.add_arrow (fict,nd,0)
                   
        term = Node(i)
        self.Arrows[name] = (self.Arrows[name][0],
                               term,
                               self.Arrows[name][2])
        self.End = term
        self.nodes.add(self.Begin)
        self.nodes.add(self.End)
        for a in self.Arrows.values():
            self.nodes.add(a[0])
            Node.add_arrow(a[0],a[1],a[2])
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



