import numpy as np

def positional_encoding(seq_length: int, d_model: int) -> np.ndarray:
    """
    Generate sinusoidal positional encodings.
    """
    # Your code here
    pos_vector =np.zeros((seq_length, d_model))
    for pos in range(seq_length):
        for i in range(d_model):
            if i %2 ==0:
                pos_vector[pos,i]=np.sin(pos/( 10000**(i/d_model)  ))
            else:
                pos_vector[pos,i]=np.cos(pos/(10000**((i-1)/d_model)))
    return pos_vector
    pass