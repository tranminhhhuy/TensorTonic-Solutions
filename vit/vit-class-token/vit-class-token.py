from matplotlib import patches
import numpy as np

def prepend_class_token(patches: np.ndarray, embed_dim: int, cls_token: np.ndarray = None) -> np.ndarray:
    """
    Prepend learnable [CLS] token to patch sequence.
    cls_token: shape (1, 1, D). If None, initialize randomly.
    """
    # YOUR CODE HERE
    cls_token =np.broadcast_to(cls_token, (patches.shape[0], 1, embed_dim))
    result=np.concatenate((cls_token, patches), axis=1)
    return result
    pass