import numpy as np

def matrix_inverse(A):
    """
    eturns: A_inv of shape (n, n) such that A @ A_inv ≈ I
    """
    # Write code here
    for i in range(len(A)):
        if type(A[0]) is not list: 
            result=None
        elif len(A) ==1 :    
            A_inv=np.linalg.inv(A)
            result=np.array(A_inv) 
        elif (A[0][0]*A[1][1])-(A[0][1]*A[1][0] ) == 0 :
            result= None        
        else:
            A_inv=np.linalg.inv(A)
            result=np.array(A_inv)            
       
    return result
    pass
