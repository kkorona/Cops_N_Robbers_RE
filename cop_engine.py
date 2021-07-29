import random
import common_engine
def abs(x):
    if x >= 0:
        return x
    else:
        return -x

def action(G, cylinder_width, cylinder_height, inp_robber_state, inp_cops_state):
    
    
    robber_state = inp_robber_state[0]
    cops_state = inp_cops_state
    
    L1_norm_list = [common_engine.get_L1_norm(robber_state, cops) for cop in cops_state]
    L2_norm_list = [common_engine.get_L2_norm(robber_state, cops) for cop in cops_state]
    
    print(L1_norm_list)
    print(L2_norm_list)
    
    robber_boundary_distance = common_engine.get_boundary_distance(robber_state, cylinder_width, cylinder_height)
    cops_boundary_distance = [common_engine.get_boundary_distance(cops, cylinder_width, cylinder_height) for cops in cops_state)]
    
    print(robber_boundary_distance)
    print(cops_boundary_distance)
    
    robber_observe_area = common_engine.get_observe_area(robber_state, robber_state, cops_state, area_type = True)
    cops_observe_area = [common_engine.get_observe_area(cop, robber_state,cops_state, area_type="uniform") for cop in cops_state]
    
    print(robber_observe_area)
    print(cops_observe_area)
    
    for cop in cops_state:
        # calculate if moving current cop is the best
        continue
    
    return cops_state