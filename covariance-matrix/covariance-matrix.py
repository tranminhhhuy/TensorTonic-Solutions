import numpy as np

def covariance_matrix(X):
    """
    Compute covariance matrix from dataset X.
    """
    # Write code here
   
    xT=np.transpose(X)
    X=np.array(X)
    if X.ndim != 2:
        return None
    a=X[0]
    result =[]
    for i in range(1,len(X) ):
        a+=X[i]
        if i == len(X)-1:
            a=a/len(X)
            for j in range(len(a)):
                s=xT[j]-a[j]
                result.append(s)
    result_T=np.transpose(result)
    cov=np.dot( result, result_T)/(len(X)-1)
    if np.isnan(cov).any():
        cov = None
    return cov
    pass