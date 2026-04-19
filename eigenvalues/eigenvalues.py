import numpy as np

def calculate_eigenvalues(matrix):
    """
    Calculate eigenvalues of a square matrix.
    """
    # Write code here
    
    if len(matrix )==0:
        eigenvalues= None
    elif type(matrix[0]) is not list:
        eigenvalues=None
    elif len(matrix) != len(matrix[0]):
        eigenvalues = None  
    else:
        det_matrix=np.linalg.det(matrix)
        if det_matrix == 0:                    
            for i in range(len(matrix[0])):
                eigenvalues=[]
                c=0
                eigenvalues.append(c)
                eigenvalues=np.array(eigenvalues)

        else:
            eigenvalues, _ = np.linalg.eig(matrix)
    return eigenvalues

    # we have condition to check matrix have inverse  because A_INV have detect eigenvalue, eigenvcetor 
    pass