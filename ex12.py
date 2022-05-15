import numpy as np

""" remove single-dimensional entries from a specified shape """
array = np.zeros((3, 1, 4))
print(np.squeeze(array).shape)
