import numpy as np

def feed_forward(x: np.ndarray, W1: np.ndarray, b1: np.ndarray,
                 W2: np.ndarray, b2: np.ndarray) -> np.ndarray:
    """
    Apply position-wise feed-forward network.
    """
    # Your code here
    #step 1 :inear transformation 
    hidden = (x@W1)+b1
    #step 2 :acitvition function 
    hidden=np.maximum(0,hidden)
    #step3 : linear transformation 
    output= hidden@W2 +b2
    return output   
    pass