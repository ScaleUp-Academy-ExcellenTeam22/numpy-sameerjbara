import numpy as np


def replace(array, num, replacement):
    """
    this function replace all numbers in a given array which is equal, less and greater to a given number
    @param array : the given array 
    @param num : the compared number
    @param replacement : the replacement number 
    """
    print(np.where(array == num, replacement, array))
    print(np.where(array < num, replacement, array))
    print(np.where(array > num, replacement, array))
