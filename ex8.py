import numpy as np


def replace(array:np.array, num:int, replacement:int):
    """
    This function replace all values in the given array that is equal, less and greater than the given number
    @param array : the given array
    @param num : the compared number
    @param replacement : the replacement number
    """
    print(np.where(array == num, replacement, array))
    print(np.where(array < num, replacement, array))
    print(np.where(array > num, replacement, array))
