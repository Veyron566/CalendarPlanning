from src.node import *
from src.graph import *
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
g.to_file('mygraph.gv')
