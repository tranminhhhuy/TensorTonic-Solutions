import numpy as np

def linear_regression_closed_form(X, y):
    """
    Compute the optimal weight vector using the normal equation.
    """
    # Write code here
    X=np.array(X)
    y=np.array(y)


    
    X_tranpose=np.transpose(X)# X-t 
    
    X_square=np.dot(X_tranpose,X) #xT*x
    
    
    X_square_inv=np.linalg.inv(X_square)#(xTx)-1
    
    y_new=np.dot(X_tranpose,y) # xTy
    
    
    w=np.dot(X_square_inv,y_new)

    
    return  w
    pass