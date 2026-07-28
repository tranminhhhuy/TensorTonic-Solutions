import numpy as np

def add_position_embedding(patches: np.ndarray, num_patches: int, embed_dim: int, pos_embed: np.ndarray = None) -> np.ndarray:
    """
    Add position embeddings to patch embeddings.
    pos_embed: position embedding of shape (1, N, D). If None, initialize randomly.
    """
    # YOUR CODE HE # Reshape to (1, N, D )
    patches_with_pos = patches + pos_embed  # Add position embeddings
    return patches_with_pos
    pass 