import numpy as np

def layer_norm(x: np.ndarray, gamma: np.ndarray, beta: np.ndarray, eps: float = 1e-6) -> np.ndarray:
    """
    Returns: Normalized array of same shape as x
    """
    # Your code here
    mean= np.sum(x, axis=-1, keepdims=True) / x.shape[-1]# compute mean data 
    var=np.sum(x**2, axis=-1 ,keepdims=True)/ x.shape[-1]-mean **2# compute variacnce data 
    normalize=(x-mean)/np.sqrt(var+eps)# compute  normalize data 
    out= gamma*normalize+beta# compute output data
    return out 


    pass