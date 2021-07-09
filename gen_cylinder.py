import networkx as nx
import matplotlib.pyplot as plt

def gen_cylinder(N,M):
    G=nx.grid_2d_graph(N,M)

    for w in range(M) :
        G.add_edge( (0,w),(N-1,w) )
    return G