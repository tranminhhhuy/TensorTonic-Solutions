import numpy as np
import math
def entropy_node(y):
    """
    Compute entropy for a single node using stable logarithms.
    """

    data = np.array(y)
    values,counts = np.unique(data,return_counts=True)
    result = 0
    for  i in range(len(values)):
            result -=  (counts[i]/len(data)) * math.log2(counts[i]/len(data))  
    return float(result)
    pass