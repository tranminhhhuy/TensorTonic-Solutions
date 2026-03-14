import numpy as np

def matrix_transpose(A):
    """
    Return the transpose of matrix A (swap rows and columns).
    """
    # Write code here
    
    result=[]
    
    for m in range (len(A[0])):
        list=[]
        for n in range(len(A)):
            list.append(A[n][m])
        result.append(list)
    return np.array(result)

        
    pass
