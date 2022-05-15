import numpy as np

"""sort the student id with increasing height of the students from given students id and height. 
Print the integer indices that describes the sort order by multiple columns and the sorted data. """
id = np.array([1000, 4292, 6230, 1500, 1600, 6000, 4532])
height = np.array([40., 42., 60., 41., 35., 39., 42.0])

indices = np.lexsort((id, height))

print(indices)
print([(id[indic], height[indic]) for indic in indices])
