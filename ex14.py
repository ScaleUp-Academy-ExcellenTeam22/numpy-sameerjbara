import numpy as np

"""combine a one and a two dimensional array together and display their elements"""
one_dimensional = np.arange(4)
two_dimensional = np.arange(8).reshape(2, 4)
for first_element, second_element in np.nditer([one_dimensional, two_dimensional]):
    print("%d:%d" % (first_element, second_element), )
