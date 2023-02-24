import numpy as np

# generate a random array. Max value is 10, length is 5
a = np.random.randint(10, size=5)

# generate a random array. Max value is 10, length is 5
b = np.random.randint(10, size=5)

# add the two arrays, piece-wise
c = a + b

# square each element of the array
squares = a ** 2

# square each element and then add piece-wise
added_squares = a ** 2 + b ** 2

# sum the resulting array to a single value
num = sum(added_squares)
