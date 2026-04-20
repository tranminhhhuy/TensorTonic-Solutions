import numpy as np

def manhattan_distance(x, y):
    """
    Compute the Manhattan (L1) distance between vectors x and y.
    Must return a float.
    """
    # Write code here
    result = 0 
    for i in range (len(x)):
        c=y[i]-x[i]
        if c < 0:
            c=c*-1
        result +=c 
    return result
    pass