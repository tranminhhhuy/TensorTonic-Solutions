import numpy as np

def linear_combination(vectors: list, coefficients: list) -> np.ndarray:
    """
    Returns the weighted sum as a float64 vector.
    """
    # make sure transform any list to anything type array  to easy for flexibility  calculate 
    vectors=np.array(vectors)
    sum=np.zeros(vectors[0].shape)  
    # make loops  to take any vector  in list  multiply  with coffecient 
    for i in range(len(vectors)):
        col=vectors[i]* coefficients[i]
        sum+= col
    sum=np.array(sum)   
    return sum.astype(np.float64)
    pass