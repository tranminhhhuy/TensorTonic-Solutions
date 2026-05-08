import numpy as np

def cosine_similarity(a,b):
    """
    Compute cosine similarity between two 1D NumPy arrays.
    Returns: float in [-1, 1]
    """
    # Write code here
    #Cosine Similarity is calculated as the dot product of two vectors divided by the product of their magnitudes.
    dot_product=np.dot(a,b)
    
    
    a_distance=np.linalg.norm(a)
    b_distance=np.linalg.norm(b)
    
    
    Euclidean_norms =a_distance*b_distance
            
    resutl=dot_product/Euclidean_norms
    if np.isnan(resutl).any():
        resutl = 0
    return resutl
    pass