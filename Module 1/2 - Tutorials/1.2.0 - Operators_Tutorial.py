# Use Math here
import math
# Let's run through some simple operations:

# First, let's go through the steps to find the magnitude
# of two vectors:
# Define the vectors
vector_one = 16
print("Vector 1 = " + str(vector_one))
vector_two = 23
print("Vector 2 = " + str(vector_two))

# First, let's square each vector. Use whichever method you like:
vector_one_squared = math.pow(vector_one, 2)
print("Vector 1 squared = " + str(vector_one_squared))
vector_two_squared = math.pow(vector_two, 2)
print("Vector 2 squared = " + str(vector_two_squared))

# Next, let's add the two vectors together:
Added = vector_one_squared + vector_two_squared
print("The two vectors added = " + str(Added))

# Finally, find the square root of the sum. Use any method:
Squared = math.sqrt(Added)
print("The added vectors squared = " + str(Squared))

