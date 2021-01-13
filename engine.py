import matplotlib.pyplot as plt
import numpy as np
from matplotlib.widgets import Button

import rob_engine
import cop_engine

class Object:
    pos = [0,0]
    passable = False

class Rob(Object):
    def __init__(self, id, pos):
        self.id = id
        self.pos = pos
        
    def action(self, rob_pos_list, cop_pos_list):
        return rob_engine.action(self.pos, rob_pos_list, cop_pos_list)

class Cop(Object):
    def __init__(self, id, pos):
        self.id = id
        self.pos = pos
    
    def action(self, rob_pos_list, cop_pos_list):
        return cop_engine.action(self.pos, rob_pos_list, cop_pos_list)
        
class Board:
    Objects = []
    def __init__(self, rob_list, cop_list):
        self.Objects.append((rob_list,cop_list))
    
    def addState(self, rob_list, cop_list):
        self.Objects.append((rob_list, cop_list))

class Plt_Ctrl_Index(object):
    ind = 0
    def next(self, event):
        self.ind += 1
        i = self.ind % len(freqs)
        ydata = np.sin(2*np.pi*freqs[i]*t)
        l.set_ydata(ydata)
        plt.draw()

    def prev(self, event):
        self.ind -= 1
        plt.draw()

def graph_init():
    plt.grid(True)
    plt.xlim(-50,50)
    plt.ylim(-50,50)
    callback = Plt_Ctrl_Index()
    axprev = plt.axes([0.7, 0.05, 0.1, 0.075])
    axnext = plt.axes([0.81, 0.05, 0.1, 0.075])
    bnext = Button(axnext, 'Next')
    bnext.on_clicked(callback.next)
    bprev = Button(axprev, 'Previous')
    bprev.on_clicked(callback.prev)
    
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
    
def check_state(rob_list, cop_list):
    for rob in rob_list:
        for cop in cop_list:
            if(rob.pos[0] == cop.pos[0] and rob.pos[1] == cop.pos[1]):
                return True
    return False

def display(board, rob_list, cop_list):
    plt.plot([rob_pos[0] for rob_pos in rob_pos_list], [rob_pos[1] for rob_pos in rob_pos_list], 'ro')
    plt.plot([cop_pos[0] for cop_pos in cop_pos_list], [cop_pos[1] for cop_pos in cop_pos_list], 'bo')
    
def start_routine(rob_list,cop_list, board):
    turn = 0
    MAX_TURN = 100
    while turn < MAX_TURN:
        graph_init()
        turn += 1
        
        rob_pos_list = []
        cop_pos_list = []
        rob_next = []
        cop_next = []
        
        for rob in rob_list:
            rob_pos_list.append(rob.pos)
        for cop in cop_list:
            cop_pos_list.append(cop.pos)
        
        if(check_state(rob_list, cop_list)):
            break     

        #update to next states
        for rob in rob_list:
            rob_next.append(rob.action(rob_pos_list, cop_pos_list))
        for cop in cop_list:
            cop_next.append(cop.action(rob_pos_list, cop_pos_list))
        
        for i in range(0, len(rob_list)):
            rob_list[i].pos = rob_next[i]
        for i in range(0, len(cop_list)):
            cop_list[i].pos = cop_next[i]
        
        board.addState(rob_list, cop_list)
        
        #display board
        
        #display(board)
        
        plt.plot([rob_pos[0] for rob_pos in rob_pos_list], [rob_pos[1] for rob_pos in rob_pos_list], 'ro')
        plt.plot([cop_pos[0] for cop_pos in cop_pos_list], [cop_pos[1] for cop_pos in cop_pos_list], 'bo')
        plt.show()
        plt.draw()
        

def main():
    rob_list, cop_list = init()
    board = Board(rob_list, cop_list)
    start_routine(rob_list, cop_list, board)
    
if __name__ == '__main__':
    main()