import numpy as np

def mean_squared_error(y_pred, y_true):
    """
    Returns: float MSE
    """
    # Write code here
    result=0
    for i in range(len(y_pred)):
        a=((y_pred[i]-y_true[i])**2)/len(y_true)
        result+=a
    return result
    pass
