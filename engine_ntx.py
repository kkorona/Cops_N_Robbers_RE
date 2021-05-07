import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Button
import networkx as nx
import copy

import rob_engine
import cop_engine

# Set system variables for engine

XMIN = 0
YMIN = 0

XMAX = 20
YMAX = 10
PADDING = 3
turn = 0
BOARD_OPTIONS = [[XMIN,YMIN],[XMAX,YMAX]]

G = grid_graph(dim=[XMAX - XMIN, YMAX-YMIN])
# Class definitions
class Object:
    pos = [0,0]
    passable = False

class Rob(Object):
    def __init__(self, id, pos):
        self.id = id
        self.pos = pos

class Cop(Object):
    def __init__(self, id, pos):
        self.id = id
        self.pos = pos
        
class Board:
    states = []
    robplot = None
    copplot = None
    def __init__(self, rob_list, cop_list):
        self.states.append((rob_list,cop_list))
    
    def addState(self, turn):
        if turn >= len(self.states):
            self.addState(turn-1)
        else:
            return
        rob_pos_list = []
        cop_pos_list = []
        rob_list = []
        cop_list = []
        for rob in self.states[turn-1][0]:
            rob_pos_list.append(rob.pos)
        for cop in self.states[turn-1][1]:
            cop_pos_list.append(cop.pos)
        if turn % 2 == 1 : # rob turn
            print("rob")
            for rob in self.states[turn-1][0]:
                rob_list.append(Rob(rob.id, rob_engine.action(rob.pos, rob_pos_list, cop_pos_list, BOARD_OPTIONS)))
            for cop in self.states[turn-1][1]:
                cop_list.append(copy.deepcopy(cop))
        else : # cop turn
            print("cop")
            for cop in self.states[turn-1][1]:
                cop_list.append(Cop(cop.id, cop_engine.action(cop.pos, rob_pos_list, cop_pos_list, BOARD_OPTIONS)))
            for rob in self.states[turn-1][0]:
                rob_list.append(copy.deepcopy(rob))
        
        self.states.append((rob_list, cop_list))

def init():
    rob_pos_data = [[1,1]]
    cop_pos_data = [[7,7],[6,7]]
    rob_list = []
    cop_list = []
    for i in range(0, len(rob_pos_data)):
        rob_list.append(Rob(id=i+1, pos=rob_pos_data[i]))
    for i in range(0, len(cop_pos_data)):
        cop_list.append(Cop(id=i+1, pos=cop_pos_data[i]))
    return rob_list,cop_list

fig = plt.figure(figsize=(8,8))
ax = fig.add_subplot(1,1,1)

x_major_ticks = np.arange(XMIN, XMAX, 5)
x_minor_ticks = np.arange(XMIN, XMAX, 1)
y_major_ticks = np.arange(YMIN, YMAX, 5)
y_minor_ticks = np.arange(YMIN, YMAX, 1)
ax.set_xticks(x_major_ticks)
ax.set_xticks(x_minor_ticks, minor=True)
ax.set_yticks(y_major_ticks)
ax.set_yticks(y_minor_ticks, minor=True)

ax.grid(which='both')

ax.grid(which='minor', alpha=1)
ax.grid(which='major', alpha=1)
plt.axis([XMIN,XMAX,YMIN,YMAX], 'equal')
# ax.set_xlim(XMIN,XMAX)
# ax.set_ylim(YMIN,YMAX)

plt.gca().set_aspect("equal")

rob_list, cop_list = init()
board = Board(rob_list, cop_list)



l1, = ax.plot([rob.pos[0] for rob in rob_list], [rob.pos[1] for rob in rob_list], 'ro', markersize = 20)
l2, = ax.plot([cop.pos[0] for cop in cop_list], [cop.pos[1] for cop in cop_list], 'bo', markersize = 20)

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

callback = Index()
axpprev = plt.axes([0.5, 0, 0.09, 0.05])
axprev = plt.axes([0.6, 0, 0.09, 0.05])
axnext = plt.axes([0.7, 0, 0.09, 0.05])
axnnext = plt.axes([0.8, 0, 0.09, 0.05])
bpprev = Button(axpprev, '<<')
# bpprev.on_clicked(callback.pprev)
bprev = Button(axprev, '<')
bprev.on_clicked(callback.prev)
bnext = Button(axnext, '>')
bnext.on_clicked(callback.next)
bnnext = Button(axnnext, '>>')
# bnnext.on_clicked(callback.next)


plt.show()