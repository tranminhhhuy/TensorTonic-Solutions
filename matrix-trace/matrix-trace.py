import numpy as np

def matrix_trace(A):
    """
    Compute the trace of a square matrix (sum of diagonal elements).
    """
    # Write code here
    result=0 
    for i in range(len(A)):
        
        if type(A[0]) is not list:
            result=None
            
        else: 
            result += A[i][i]
    
    return result
    pass
