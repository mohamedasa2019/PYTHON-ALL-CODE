import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()
# read file data
readfile = open("")
for line in readfile:
    spline=line.split(",")
    G.add_edge(spline[0],spline[1])

pos = nx.circular_layout(G)

nx.draw(G,pos)
plt.show()


