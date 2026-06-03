import numpy as np

def pca_projection(X, k):
    """
    Project data onto the top-k principal components.
    """
    # Write code here
    
    
    
    # Write code here
    #  sum of each component vector and divide by the number of samples to get the mean
    X_mean = np.mean(X, axis=0)
    X_meaned = X - X_mean
    #compute variance matrix 
    cov_mat= np.cov(X_meaned, rowvar=False) 
    # like make make matrix transpose and then dot product with original matrix
    # find principal components  , The eigenvectors are the principal component directions.
    eigenvalues, eigenvectors = np.linalg.eig(cov_mat)
    # sort the eigenvalues and eigenvectors in descending order
    sorted_indices = np.argsort(eigenvalues)[::-1]
    #  sot the eigenvalues in descending order and get the indices    
    sorted_eigenvalues = eigenvalues[sorted_indices]#using index for sorted eigevalues 
    sorted__eigenvectors = eigenvectors[:, sorted_indices ] #using index for sorted eigenvectors
    # select the top-k eigenvectors
    eigenvector_subset = sorted__eigenvectors[:, 0:k] 
    # select the top-k eigenvectors
    # project the data onto the top-k eigenvectors 
    x_reduceced=np.dot(eigenvector_subset.T,X_meaned.T).T # project the data onto the top-k eigenvectors
    return x_reduceced