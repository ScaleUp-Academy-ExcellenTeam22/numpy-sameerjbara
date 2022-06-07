import numpy as np

""" remove single-dimensional entries from a specified shape """


def reshape(array: np.array) -> np.ndarray:
    print(np.squeeze(array))


array = np.zeros((3, 1, 4))
reshape(array)
