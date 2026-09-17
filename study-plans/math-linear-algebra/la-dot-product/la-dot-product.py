import numpy as np

def dot_product(x: list, y: list) -> float:
    """
    Returns the dot product as a float.
    """
    total=0
    for i in range (len(x)):
        
        a=x[i]*y[i]
        total +=a 

    total=float(total)
    return  total 
    
    




    
    pass