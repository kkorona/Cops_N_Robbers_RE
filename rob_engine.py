import random
def action(cur_pos, rob_pos_list, cop_pos_list):
    x_delta = random.randint(-1,1)
    y_delta = random.randint(-1,1)
    return [ cur_pos[0]+x_delta, cur_pos[1]+y_delta ]
    
def logging():
    return None