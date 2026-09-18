import numpy as np

def matrix_transpose(A: list) -> np.ndarray:
    """
    Returns the transpose as a float64 array.
    """
    # transform column to  row  
    result= [] # to  split 
    for i in range(len(A[0])):
        temp=[]
        for j in  range(len(A)):
            temp.append(A[j][i])
        result.append(temp)
    result=np.array(result)
    return result.astype(np.float64)
            



            

    pass