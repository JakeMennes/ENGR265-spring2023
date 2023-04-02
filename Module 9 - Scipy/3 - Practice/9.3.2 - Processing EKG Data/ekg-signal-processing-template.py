import matplotlib.pyplot as plt
import numpy as np

# database name
database_name = 'mitdb_201'

# path to ekg folder
path_to_folder = "../../../data/ekg/"

# select a signal file to run
signal_filepath = path_to_folder + database_name + ".csv"

# load data in matrix from CSV file; skip first two rows
raw_ekg_data = np.loadtxt(signal_filepath, skiprows=2, delimiter=",")

# pull out each column as a vector
time = raw_ekg_data[:, 0]
v5 = raw_ekg_data[:, 1]
v2 = raw_ekg_data[:, 2]

# select a signal to operate on
signal = v2


# pass data through weighted differentiator
# I think this is incorrect as it does not look "forward" but should work
diff = None

# pass data through square function
squared = None

#@TODO: remove this language in future revisions.
# pass through moving average of 150ms window @ 250 Hz => 38 samples
filtered = None

# make a plot of the results. Can change the plot() parameter below to show different intermediate signals
plt.title('Signal for ' + database_name + " with detections")
plt.plot(filtered)
plt.show()