import numpy as np

def dot_product(x, y):
    """
    Compute the dot product of two 1D arrays x and y.
    Must return a float.
    """
    # Write code here
    result=0
    for i in range(len(x)):
        if len(x)  !=len(y):
            raise ValueError("x and y must have same length")
        else:
            result+= x[i]*y[i]

    return result
    pass