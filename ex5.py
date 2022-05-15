import numpy as np


def add_vector(matrix: np.ndarray, vector: np.ndarray) -> np.ndarray:
    """
       The function add the vector for each row in the given matrix.
       @param matrix: The given matrix  
       @param vector: the given vector 
       @return: tuple contains the row and col of the matrix.
       """
    result = np.empty_like(matrix)
    for index in range(0, matrix.shape[0]):
        result[index, :] = matrix[index, :] + vector
    return result
