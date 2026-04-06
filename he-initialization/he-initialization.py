def he_initialization(W, fan_in):
    """
    Scale raw weights to He uniform initialization.
    """
    # Write code here

    loss = np.sqrt(6/fan_in)# calculate loss
    W=np.array(W)
    W=W *2*loss-loss
    return W