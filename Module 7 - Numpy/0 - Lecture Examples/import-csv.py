import numpy as np

# Approach #1: do a manual import for the file
path = '../../data/ekg/mitdb_201.csv'

# open the file
file = open(path)

# read the first line to get the headers
header = file.readline()

# read the second line to get the units
units = file.readline()

# make a list to hold this information
points = list()

# iterate through remainder of file
for line in file:
    # split line based upon commas
    elements = line.strip().split(",")

    # manually assign time, ML2, and V2 values
    time = elements[0]
    ml2 = elements[1]
    v1 = elements[2]

    # add data points in list tuple
    points.append((time, ml2, v1))

# close file, we're done
file.close()

# Approach #2: import the CSV file using numpy
path = '../../data/ekg/mitdb_201.csv'

# load data in matrix from CSV file; skip first two rows
ekg_data = np.loadtxt(path, skiprows=2, delimiter=",")

