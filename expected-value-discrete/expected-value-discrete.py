import numpy as np

def expected_value_discrete(x, p):
    """
    Returns: float expected value
    """
    # Write code here
    result=0
    total=0
    for i in range(len(p)):
        total += p[i]
    if total==1 :
        for i in range(len(x)):
            result+= x[i]*p[i]
    else:
            raise ValueError("Invalid probabilities")
    return  result
                                
    pass
