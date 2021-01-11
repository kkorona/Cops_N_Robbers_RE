import matplotlib as plt
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
    
def init():
    plt.grid(True)
    rob_pos_data = [[1,1]]
    cop_pos_data = [[7,7],[6,7]]
    rob_list = []
    cop_list = []
    for i in range(1, len(rob_pos_data)+1):
        rob_list.append(Rob(id=i, pos=rob_pos_data[i-1]))
    for i in range(1, len(cop_pos_data)+1):
        cop_list.append(Cop(id=i, pos=cop_pos_data[i-1]))
    return rob_list,cop_list
    
def start_routine():
    turn = 0
    rob_list = []
    cop_list = []
    while turn < MAX_TURN:
        turn += 1
        
        rob_pos_list = []
        cop_pos_list = []
        
        for rob in rob_list:
            rob_pos_list.append(rob.pos)
        for cop in cop_list:
            cop_pos_list.append(cop.pos)
        
        check_state(rob_pos_list, cop_pos_list)
        for rob in rob_list:
            rob_next.append(rob.action(rob_pos_list, cop_pos_list))
        for cop in cop_list:
            cop_next.append(cop.action(rob_pos_list, cop_pos_list))
            
        plt.plot([rob_pos[0] for rob_pos in rob_pos_list], [rob_pos[1] for rob_pos in rob_pos_list], 'ro')
        plt.plot([cop_pos[0] for cop_pos in cop_pos_list], [cop_pos[1] for cop_pos in cop_pos_list], 'bo')

def main():
    rob_list, cop_list = init()
    start_routine(rob_list, cop_list)