import numpy as np

def layer_norm(x: np.ndarray, gamma: np.ndarray, beta: np.ndarray, eps: float = 1e-6) -> np.ndarray:
    """
    Returns: Normalized array of same shape as x
    """
    # Your code here

    # compute mean across all dimension features:
    x_mean =np.mean(x,axis=-1, keepdims=True)
    # compute variance across all dimension features:
    x_var=np.var(x,axis=-1,keepdims=True)
    # compute normalized x:
    x_normalized =(x-x_mean)/np.sqrt(x_var+eps)
    # scale and shift:
    out= gamma * x_normalized + beta
    return out
pass
