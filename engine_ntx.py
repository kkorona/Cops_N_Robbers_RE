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

    nx.draw(G, pos=pos, nodelist=[(0,0), (1,1)], \
                      node_size=900, node_color='yellow'  )
                      

robber_state = []
cops_state = []

def init_robber_state(G):
    pass

def init_cop_state(G):
    pass

def init():
    robber_state.append((1,5))
    cops_state.append((7,4))
    cops_state.append((9,11))

G = gen_cylinder.gen_cylinder(10,20)

class Index(object):
    def next(self, event):
        global board, turn
        turn += 1
        print("next : %d" % (turn))
        if turn >= len(board.states):
            board.addState(turn)
        rob_xdata = [ x.pos[0] for x in board.states[turn][0] ]
        rob_ydata = [ x.pos[1] for x in board.states[turn][0] ]
        cop_xdata = [ x.pos[0] for x in board.states[turn][1] ]
        cop_ydata = [ x.pos[1] for x in board.states[turn][1] ]
        l1.set_xdata(rob_xdata)
        l1.set_ydata(rob_ydata)
        l2.set_xdata(cop_xdata)
        l2.set_ydata(cop_ydata)
        plt.draw()

    def prev(self, event):
        global board, turn
        if turn > 0: 
            turn -= 1
            print("prev : %d" % (turn))
            rob_xdata = [ x.pos[0] for x in board.states[turn][0] ]
            rob_ydata = [ x.pos[1] for x in board.states[turn][0] ]
            cop_xdata = [ x.pos[0] for x in board.states[turn][1] ]
            cop_ydata = [ x.pos[1] for x in board.states[turn][1] ]
            l1.set_xdata(rob_xdata)
            l1.set_ydata(rob_ydata)
            l2.set_xdata(cop_xdata)
            l2.set_ydata(cop_ydata)
            plt.draw()
    
def check_capture_state(rob_list, cop_list):
    for rob in rob_list:
        for cop in cop_list:
            if(rob.pos[0] == cop.pos[0] and rob.pos[1] == cop.pos[1]):
                return True
    return False


viz_cylinder(G)
callback = Index()
axpprev = plt.axes([0.5, 0, 0.09, 0.05])
axprev = plt.axes([0.6, 0, 0.09, 0.05])
axnext = plt.axes([0.7, 0, 0.09, 0.05])
axnnext = plt.axes([0.8, 0, 0.09, 0.05])
bpprev = Button(axpprev, '<<')
# bpprev.on_clicked(callback.pprev)
bprev = Button(axprev, '<')
# bprev.on_clicked(callback.prev)
bnext = Button(axnext, '>')
# bnext.on_clicked(callback.next)
bnnext = Button(axnnext, '>>')
# bnnext.on_clicked(callback.next)

plt.show()