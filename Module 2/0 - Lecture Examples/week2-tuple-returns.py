import numpy as np
import random


def find_min_loc(array2D, x_dim, y_dim):
    """
    Find the (x,y) location and value for minimum in 2D array

    :param array2D: a two dimensional numpy array
    :param x_dim: length of x-dimension
    :param y_dim: length of y-dimension
    :return: (x location, y location, minimum value)
    """
    # temp value to hold minimum value and its location
    min_value = array2D[0][0]
    x_loc = 0
    y_loc = 0

    # manually search through all (x,y) locations in the matrix
    # to find the minimum value and its location
    for idx in range(0,x_dim):
        for idy in range(0,y_dim):
            if array2D[idx][idy] < min_value:
                min_value = array2D[idx][idy]
                x_loc = idx
                y_loc = idy

    # return results as tuple
    return x_loc, y_loc, min_value


# get random length from 2 to 10
length = random.randint(2, 6)

# create square array of random length
array = np.random.rand(length, length)

# function returns multiple results
(x, y, value) = find_min_loc(array, length, length)

print("For array: ")
print(array)
print("Min value is", value, " located at ("+str(x)+","+str(y)+")")

