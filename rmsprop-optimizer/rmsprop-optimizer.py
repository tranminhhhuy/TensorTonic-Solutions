import numpy as np
import math
def rmsprop_step(w, g, s, lr=0.001, beta=0.9, eps=1e-8):
    """
    Perform one RMSProp update step.
    """
    # Write code here
    result=()
    w=np.array(w)
    g=np.array(g)
    s=np.array(s)


    s_new= (beta*s) +  (1 - beta) * (g**2)
    st=np.sqrt(s_new) + eps
    w_new= w - (lr / st)*g
    result=(w_new,s_new)
    
    return result

    
    pass