import numpy as np


def reshape(array1: np.array, array2: np.array) -> np.ndarray:
    """program to convert two 1-D arrays into a 2-D array"""
    combined = np.dstack((array1, array2))
    return combined


array1 = np.array([[10, 20, 30]])
array2 = np.array([[40, 50, 60]])
print(reshape(array1, array2))
