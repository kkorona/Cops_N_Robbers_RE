import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Button
import networkx as nx
import copy

import gen_cylinder

import rob_engine
import cop_engine

def viz_cylinder(G):
    pos = dict( (n, n) for n in G.nodes() ) # pos=(위치, node 이름)
    # vlabels = dict( ((i, j), i * 10 + j) for i, j in G.nodes() ) # 사용안함.
    vlabels = dict( ((i, j), str(i)+","+str(j) ) for i, j in G.nodes() )

    nx.draw_networkx(G, pos=pos, node_size=900,  labels=vlabels,node_color='tan', edge_color='r', font_size = 10)
    nx.draw_networkx_edges (G, pos,  width=2, edge_color='tan' )

robber_state = []
cops_state = []

def draw_cops(G):
    nx.draw(G, pos=pos, nodelist=cops_state, \
                      node_size=900, node_color='yellow'  )

def draw_robber(G)
                      
def init_robber_state(G):
    pass

def init_cop_state(G):
    pass

def init():
    robber_state.append((1,5))
    cops_state.append((7,4))
    cops_state.append((9,11))

G = gen_cylinder.gen_cylinder(10,20)




viz_cylinder(G)

plt.show()