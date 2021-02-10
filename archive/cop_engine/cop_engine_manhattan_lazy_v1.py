import random

def abs(x):
    if x >= 0:
        return x
    else:
        return -x

def get_manhattan_dist (pos_A, pos_B):
    return abs(pos_A[0] - pos_B[0]) + abs(pos_A[1] - pos_B[1])

def boundary_violation(XX, YY, BOARD_OPTIONS):
    if BOARD_OPTIONS[0][0] > XX:
        return True
    elif BOARD_OPTIONS[1][0] < XX:
        return True
    elif BOARD_OPTIONS[0][1] > YY:
        return True
    elif BOARD_OPTIONS[1][1] < YY:
        return True
    else:
        return False
    
def action(cur_pos, rob_pos_list, cop_pos_list, BOARD_OPTIONS):
    # x_delta = random.randint(-1,1)
    # y_delta = random.randint(-1,1)
    
    cop_x = cur_pos[0]
    cop_y = cur_pos[1]
    diff_x = [0,0,1,-1]
    diff_y = [1,-1,0,0]
    
    max_dist = 999
    x_delta = 0
    y_delta = 0
    
    
    # Lazy Cop에서는 cop_pos_list가 동일할때 현재 포지션과 상관없이 출력이 일정함
    # 따라서 cur_pos는 움직이는 cop의 위치가 아닌 이상 stay로 구성되야함
    
    for ii in range(0,4):
        XX = cop_x + diff_x[ii]
        YY = cop_y + diff_y[ii]
        # boundary check & update
        if(boundary_violation(XX, YY, BOARD_OPTIONS)):
            continue
        cur_mdist = 0
        for rob in rob_pos_list:
            rob_x = rob[0]
            rob_y = rob[1]
            cur_mdist += get_manhattan_dist([rob_x, rob_y], [XX,YY])
        if cur_mdist < max_dist:
            max_dist = cur_mdist
            x_delta = diff_x[ii]
            y_delta = diff_y[ii]
        # if current option is best_movement
        #     renew best_movement
    
    # if cur_pos is best_movement:
    #    return best_movement
    # else
    return [ cur_pos[0]+x_delta, cur_pos[1]+y_delta ]
    
def logging():
    return None