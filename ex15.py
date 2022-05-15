import numpy as np

"""create a three-dimension array with shape (300,400,5)
Fill the array elements with values using unsigned integer (0 to 255)  """
array = np.random.randint(0, 256, (300, 400, 5), np.uint8)
print(array)
