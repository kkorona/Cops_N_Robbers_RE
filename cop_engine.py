import random
import common_engine
def abs(x):
    if x >= 0:
        return x
    else:
        return -x



def action(G, N, M, inp_robber_state, inp_cops_state):

    robber_state = inp_robber_state[0]
    cops_state = inp_cops_state
    
    L1_norm_list = [common_engine.get_L1_norm(robber_state, cops) for cop in cops_state]
    L2_norm_list = [common_engine.get_L2_norm(robber_state, cops) for cop in cops_state]
    
    robber_boundary_distance = common_engine.get_boundary_distance(robber_state, N, M)
    cops_boundary_distance = [common_engine.get_boundary_distance(cops, N, M) for cops in cops_state)]
    
    robber_observe_area = common_engine.get_observe_area(robber_state, robber_state, cops_state, area_type = True)
    cops_observe_area = [common_engine.get_observe_area(cop, robber_state, cops_state, area_type="uniform") for cop in cops_state]
    
    
    
    
    
    