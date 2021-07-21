import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Button
import networkx as nx
import copy

import gen_cylinder

import rob_engine
import cop_engine

N = 20
M = 10

ncolor="gainsboro"
ccolor="limegreen"
rcolor="tomato"
ecolor='gray'

G = gen_cylinder.gen_cylinder(N,M)
pos = dict( (n, n) for n in G.nodes() ) # pos=(위치, node 이름)
vlabels = dict( ((i, j), str(i)+","+str(j) ) for i, j in G.nodes() )

def viz_cylinder(G):
    nx.draw_networkx(G, pos=pos, node_size=800,  labels=vlabels,node_color='tan', edge_color='r', font_size = 8)
    nx.draw_networkx_edges (G, pos,  width=2, edge_color='tan' )

robber_state = []
cops_state = []

def draw_agent(P, color):
    nx.draw(G, pos=pos, nodelist=P, \
                      node_size=800, node_color=color  )
    

def draw_robber():
    draw_agent(robber_state, rcolor)

def draw_cops():
    draw_agent(cops_state, ccolor)
                      
def init_robber_state():
    robber_state.append((1,5))

def init_cop_state():
    cops_state.append((7,4))
    cops_state.append((11,9))

def init():
    init_robber_state()
    init_cop_state()

init()
viz_cylinder(G)


draw_cops()
draw_robber()

plt.show()