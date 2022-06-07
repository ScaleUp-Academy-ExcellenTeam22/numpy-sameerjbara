import numpy as np


def sort_array(array: np.ndarray):
    """
    this function sort the first, last axis of an array
    param array:the given array
    return: none
    """
    array = np.sort(array, axis=0)
    print(array)
    array = np.sort(array, axis=1)
    print(array)
