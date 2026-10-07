import numpy as np

def matrix_trace(A: list) -> float:
    """
    Returns the trace as a Python float.
    """

    result = 0
    for i in range(len(A)):
        result+=A[i][i]
    result = float(result)            
    return result
    pass