from src.node import *
from src.graph import *
# Some graph definition end output example
Data = [('A',[], 5,5),
        ('B',['A'],4,4),
        ('C', ['A'],3,3),
        ('D',['B','C'],2,2),
        ('E',['D'],1,1)]

g = Graph(Data)

g.stright_progn(g.Begin)
g.backward_progn(g.End)

g.to_file("mygraph.gv").view()

