import numpy as np
import matplotlib.pyplot as plt


def calculate_sin_points():
    """
    this function compute the x and y coordinates for points on a sine curve and plot the points using matplotlib
    return: none
    """
    x_points = np.arange(-6, 6 * np.pi, 0.1)
    y_points = np.sin(x_points)

    plt.plot(x_points, y_points)
    plt.show()
