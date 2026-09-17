import numpy as np
import math 

def euclidean_distance(x: list, y: list) -> float:
    """
    Returns the Euclidean distance as a float.
    """
    total = 0 # gain variable for  result 


    if len(x)==len(y):
        for i in range(len(x)):
            a= x[i]-y[i]
            a=a*a
            total+=a 


    # use tool np.sqrt 
    total=math.sqrt(total)
    # transform type total = float
    total=float(total)
    return total



    
    pass