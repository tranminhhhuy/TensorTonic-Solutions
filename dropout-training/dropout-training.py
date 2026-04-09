import numpy as np

def dropout(x, p=0.5, rng=None):
    """
    Apply dropout to input x with probability p.
    Return (output, dropout_pattern).
    """
    # Write code here
    x = np.array(x)
    if rng is None:
        rng=np.random.default_rng()
    mask= rng.random(x.shape ) >= p   #keep the remaining percentage
    drop= x*mask # mutiple remaing  pertentage with x = percentage of x input  
    dropout= mask/(1-p) 
    result = drop/(1-p) # You lose some fearture, and have to make up for it with the remaining features
    tuple=( result, dropout)
    return  tuple
    pass