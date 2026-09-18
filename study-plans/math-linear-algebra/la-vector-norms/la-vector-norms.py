import numpy as np
import math 

def vector_norms(v: list) -> np.ndarray:
    """
    Returns a float64 array containing the L1, L2, and infinity norms.
    """

    result= []
    norm_1=0
    norm_2=0
    max=0
    # make loop  to take the  element in vector 
    for i in range(len(v)):
        # stag1 : make norm L1 
          #check negative number 
        if v[i] < 0:
            v[i]=v[i]* (-1)
        norm_1+= v[i]
        # stage  2 : make variable   norm_2 to summ each element in vector  and after  square us 
        norm_2+=  v[i]*v[i]
        # stage3 
        
        if v[i] > max :
            max =v[i]
    norm_2= math.sqrt(norm_2)
    norm_3 = max 
    result.append(norm_1)
    result.append(norm_2)
    result.append(norm_3)
    result=np.array(result)
    return result
            
    pass