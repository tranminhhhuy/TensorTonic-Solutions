
import numpy as np
from torch import cov

def conv(x, out_channels):
    batch, height, width, in_channels = x.shape
    return np.zeros((batch, height, width, out_channels))
def unet_encoder_block(x: np.ndarray, out_channels: int) :
    """
    Returns (pool_out, skip_out) as zero arrays with correct shapes.
    """
    # Your implementation here
    # minus 2 with width and height
    x=x[:,:-4,:-4,: ]
    pool_out=x[:,::2,::2 ,:]
    pool_out=conv(pool_out, out_channels)
    skip_out = np.repeat(pool_out, 2, axis=1)
    skip_out= np.repeat(skip_out, 2, axis=2)
    skip_out = conv(skip_out,out_channels)

    return pool_out, skip_out