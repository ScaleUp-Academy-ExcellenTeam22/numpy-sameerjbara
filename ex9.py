import numpy as np


def mul(array1: np.ndarray, array2: np.ndarray) -> np.ndarray:
    """
    This function multiply two given arrays of the same size element-by-element
    @param array1: the first array
    @param array2: the second array
    return: the result of the multiplication 
    """
    return np.multiply(array1, array2)
