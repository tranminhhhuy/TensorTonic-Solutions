import numpy as np

def outer_product(u: list, v: list) -> np.ndarray:
    """
    Returns the float64 outer-product matrix.

    
    """
    u=np.array(u)
    v=np.array(v)
    result=[]
    # make loops to take element in list 
    for i in range(len(u)):
        row= u[i]*v 
        result.append(row)
    result=np.array(result)
    return result.astype(np.float64)

    
    pass