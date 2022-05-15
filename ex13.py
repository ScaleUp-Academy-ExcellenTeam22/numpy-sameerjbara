import numpy as np

"""program to convert two 1-D arrays into a 2-D array"""
array1 = np.array([[10, 20, 30]])
array2 = np.array([[40, 50, 60]])
combined = np.dstack((array1, array2))
