import math

def abs(x):
    if x >= 0:
        return x
    else:
        return -x

def get_L1_norm(A, B):
    return abs(A[0]-B[0]) + abs(A[1] - B[1])
    
def get_L2_norm(A, B):
    return math.sqrt(((A[0]-B[0]) ** 2) + ((A[1]-B[1]) ** 2))
    
def get_boundary_distance(A, N, M):
    return min(M-A[1], A[1])