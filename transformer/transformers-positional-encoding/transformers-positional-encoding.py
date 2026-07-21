
import numpy as np
def positional_encoding(seq_length: int, d_model: int) -> np.ndarray:
    """
    Generate sinusoidal positional encodings.
    """
    # Your code here
    output = np.zeros((seq_length, d_model))    
    for i in range(seq_length):
        #  condition to check if the index is odd and even 
        for j in range(d_model):
            if j % 2 == 0:
                output[i, j] = np.sin(i / (10000 ** (j / d_model)))
            else:
                output[i, j] = np.cos(i / (10000 ** ((j - 1) / d_model)))
    return output
    pass