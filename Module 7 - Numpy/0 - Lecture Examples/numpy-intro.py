import numpy as np

# make a basic array
arr2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# what's the array shape
shape = arr2d.shape

# what type of data is it holding
type = arr2d.dtype

# access single elements (0,0) and (2,2)
item = arr2d[0, 0]
item2 = arr2d[2, 2]

# get the first row, second row, and right column
first_row = arr2d[0, :]
second_row = arr2d[1, :]
right_column = arr2d[:, 2]

# get the first two rows
first_two = arr2d[:2]

# from row 1, grab first two columns
two_columns = arr2d[1, :2]

# from all rows, get the first column
first_column = arr2d[:, 0]

