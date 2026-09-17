import numpy as np
import math 
def cosine_similarity(a: list, b: list) -> float:
    """
    Returns the cosine similarity as a float.
    """
    #  
    
    total_A= 0 # gain  variable  during process  loops 
    total_B=0 
    total_dot=0
    result = 0 
    # make loop to calculate each element  for process 
    
    # check numberous of  two vector 
    if  len (a)== len(b):
        for i in range (len(a)):
        # step 1  compute dot_product  :
            c= a[i]*b[i]
            total_dot+= c 

        #step2  calculate magitude 
            total_A+= a[i]*a[i]
            total_B+= b[i]*b[i]

    total_A=math.sqrt(total_A)
    total_B=math.sqrt(total_B)
    if total_A==0 or  total_B==0:
        result= 0
        result=float(result)
        return result
        breakpoint
    result +=   ( total_dot/(total_A*total_B)) 
    result= float(result) 
    return result
    pass
    