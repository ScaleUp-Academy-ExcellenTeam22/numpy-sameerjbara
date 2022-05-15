import numpy as np


def mul(array1: np.ndarray, array2: np.ndarray) -> np.ndarray:
    """
    this function multiply two given arrays of same size element-by-element
    @param array1: the first array
    @param array2: the second array
    return: the result of the multiply array
    """
    return np.multiply(array1, array2)
