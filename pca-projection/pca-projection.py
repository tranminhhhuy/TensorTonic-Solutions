import numpy as np

def pca_projection(X, k):
    """
    Project data onto the top-k principal components.
    """
    X=np.array(X)
    u=X[0]
    result=[]
    # Center data find
    for i  in range (len(X) -1 ):
        u=u+X[i+1]
    
    u=u/len(X)
    Center_DaTa= X-u
    Center_DaTa_Transpose=np.transpose(Center_DaTa)
    # find covariance of data 
    cov_DaTa=np.dot(Center_DaTa_Transpose,Center_DaTa)/len(X)
            
    # find eigenvector dont change direction when we scale it with number and eigenvalue to arrange to find principal component according in order to  decending 
    eigenvalues ,eigenvectors =np.linalg.eig(cov_DaTa) 
    idx= np.argsort(eigenvalues)[::-1]
    eigvals_sorted = eigenvalues[idx]# data set we have base on to select principal components 
    eigenvectors_sorted=eigenvectors[:,idx]
    
    w=eigenvectors_sorted[:, : k]
    result= Center_DaTa @ w

    return (result[:, : k])