import torch
import torch.nn as nn
import math

def create_embedding_layer(vocab_size: int, d_model: int) -> nn.Embedding:
    """
    Create an embedding layer.
    """
    # Your code here
    embedding_matrix = nn.Embedding(vocab_size, d_model)
    # Initialize the embedding matrix with random values
    nn.init.uniform_(embedding_matrix.weight, -0.6, 0.6)# number create random values between -0.1 and 0.1
    return embedding_matrix

def embed_tokens(embedding: nn.Embedding, tokens: torch.Tensor, d_model: int) -> torch.Tensor:
    """
    Convert token indices to scaled embeddings.
    """
    # Your code here
    embeddings= embedding(tokens) * math.sqrt(d_model)
    return embeddings
    pass