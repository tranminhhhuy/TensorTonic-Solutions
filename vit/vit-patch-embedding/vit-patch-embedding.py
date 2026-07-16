import numpy as np

def patch_embed(image: np.ndarray, patch_size: int, embed_dim: int, W_proj: np.ndarray = None) -> np.ndarray:
    """
    Convert image to patch embeddings.
    W_proj: projection matrix of shape (patch_dim, embed_dim). If None, initialize randomly.
    """
    # YOUR CODE HERE
    B,H,W,C=image.shape
    assert H % patch_size == 0 and W % patch_size == 0, "Image dimensions must be divisible by patch size."


    # first stage  : count patches 
    count_patches = (H // patch_size) * (W // patch_size)
    # second stage  : reshape image to patches  and flatten
    patches=image.reshape(B,H//patch_size,patch_size,W//patch_size,patch_size,C)
    patches=patches.transpose(0,1,3,2,4,5)
    pathches=patches.reshape(B,count_patches,patch_size*patch_size*C)



    
    # thrid stage : project patches to embedding dimension
    if W_proj is None:
        W_proj = np.random.randn(patch_size*patch_size*image.shape[3], embed_dim) * 0.02 
    z = pathches @ W_proj
    return z



    pass