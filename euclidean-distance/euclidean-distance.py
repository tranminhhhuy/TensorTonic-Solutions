import numpy as np

def euclidean_distance(x, y):
    """
    Compute the Euclidean (L2) distance between vectors x and y.
    Must return a float.
    """
    # Write code here

    result=0
    if len(x)!=len(y):
        raise ValueError
    breakpoint
    
    for i in range(len(x)):
       result += np.square(x[i]-y[i])
    result=np.sqrt(result)
  
    return result                          
    pass