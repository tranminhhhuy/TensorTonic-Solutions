import numpy as np

def matrix_normalization(matrix, axis="null", norm_type="l2"):
    matrix = np.array(matrix)
    result = []
    sum = 0

    if norm_type not in ["l1", "l2", "max"]:
        return None
    if axis not in [0,1,None]:
        return None
    if matrix.ndim != 2:
        return None

    if axis == 0:
        matrix = np.transpose(matrix)

    for i in range(len(matrix)):
        for j in range(len(matrix[0])):

            
            if axis == None:
                if norm_type == "l1":
                    sum += matrix[i][j]

                elif norm_type == "l2":
                    sum += matrix[i][j] * matrix[i][j]

                else:  # max
                    if matrix[i][j] > sum:
                        sum = matrix[i][j]

            # ✅ ROW / COLUMN
            elif axis == 1 or axis == 0:

                if norm_type == "l1":
                    sum += matrix[i][j]
                    if j == len(matrix[0]) - 1:
                        s = matrix[i] / sum
                        result.append(s)
                        sum = 0

                elif norm_type == "l2":
                    sum += matrix[i][j] * matrix[i][j]
                    if j == len(matrix[0]) - 1:
                        sum = np.sqrt(sum)
                        if sum == 0:
                            s = matrix[i]   # giữ nguyên [0,0]
                        else:
                            s = matrix[i] / sum
                        result.append(s)
                        sum = 0

                else:  # max
                    if matrix[i][j] > sum:
                        sum = matrix[i][j]
                    if j == len(matrix[0]) - 1:
                        s = matrix[i] / sum
                        result.append(s)
                        sum = 0

    # ✅ xử lý sau loop
    result=np.array(result)
    if axis == 0:
        result = np.transpose(result)

    elif axis == None:
        if norm_type == "l2":
            sum = np.sqrt(sum)
        
        s = matrix / sum
        result=s
    return result
    pass