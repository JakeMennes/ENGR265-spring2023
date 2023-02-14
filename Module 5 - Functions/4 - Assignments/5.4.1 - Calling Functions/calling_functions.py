from numpy import random
import numpy as np

# Parameters for distribution and samples to generate
# These values are fixed. Do not change.
mu = 0
std = 1

# Step 1: Set the number of samples you wish to take. This value is selected by you.
num_samples = 10

# Step 2: use normal to generate distribution samples
samples = None #edit this line

# Step 3: use mean() to determine the average of those samples
measured_mean = -1 #edit this line

# Step 4: use std() to determine the standard deviation of samples
measured_deviation = -1 #edit this line

# check if sufficient samples were taken. Do not modify below this line
print("mu=", measured_mean, "stdev=", measured_deviation)

mean_error = abs(mu - measured_mean)
deviation_error = abs(std - measured_deviation)

if measured_mean < 1E-3 and deviation_error < 1E-3:
    print('Solution within error tolerances')
else:
    print('Solution is not within error tolerances')
