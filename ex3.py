import numpy as np


def get_matrix_size(matrix: np.ndarray) -> tuple:
    """
    The function find the number of rows and columns of a given matrix.
    @param matrix: The given matrix.
    @return: tuple that contains the size of the matrix.
    """
    return matrix.shape
