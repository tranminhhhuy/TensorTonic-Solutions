import numpy as np

def softmax(x, axis=-1):
    e_x = np.exp(x - np.max(x, axis=axis, keepdims=True))
    return e_x / np.sum(e_x, axis=axis, keepdims=True)

def multi_head_attention(Q: np.ndarray, K: np.ndarray, V: np.ndarray,
                         W_q: np.ndarray, W_k: np.ndarray, W_v: np.ndarray,
                         W_o: np.ndarray, num_heads: int) -> np.ndarray:
    """
    Compute multi-head attention.
    """
    # Your code here
    Q_heads= np.split(Q@W_q,num_heads,axis=-1)
    K_heads= np.split (K@W_k,num_heads,axis=-1)
    V_heads= np.split (V@W_v, num_heads, axis=-1)
    attention=[]
    for q , k,v in zip(Q_heads, K_heads,V_heads):
        score=q @ k.transpose(0,2,1)/ np.sqrt(q.shape[-1])
        weight=softmax(score, axis=-1)
        attention_output=weight @ v
        attention.append(attention_output)    
    concatenation = np.concatenate(attention,axis=-1)
    output=concatenation@W_o
    return output
    pass
    