import torch
import torch.nn.functional as F
import math

def scaled_dot_product_attention(Q: torch.Tensor, K: torch.Tensor, V: torch.Tensor) -> torch.Tensor:
    """
    Compute scaled dot-product attention.
    """
    # Your code here
    K=torch.transpose(K,-2,-1)
    result = torch.matmul(torch.tensor(Q),torch.tensor(K))/math.sqrt((Q).size(-1))
    result = F.softmax(result, dim=-1) # each row probilities =1 
    V=torch.tensor(V, dtype=torch.float32)
    result=torch.matmul(result,V)
    return  result
    pass