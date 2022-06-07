import numpy as np


def arrayinit() -> np.ndarray:
    array = np.empty((4, 4), np.int64)
    swapped_array = array[::-1]

    return swapped_array


arrayinit()
