import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import find_peaks

"""
Step 1: Load pre-processed data that has already been filtered through the PT process
"""

# list of available pre-processed datasets in the data/ekg folder
available_datasets = ["mitdb_201", "mitdb213", "mitdb219", "nstdb_118e00", "qtdb_118e06"]

# select a data set from the enumerated list above
dataset = available_datasets[0]

# load saved data from numpy array
filepath = '../../../data/ekg/processed_'+dataset+'.npy'

# once loaded, place in an array called filtered
signal = np.load(filepath)

"""
Step 2: Determine how much data to use...
"""
# If you wish to only run on ~10s of data uncomment the line below
# if you wish to run on all data, comment out this line
signal = signal[0:3300]

"""
Step 3: Attempt simple thresholding with timeout to detect the signal
Adjust the values for threshold and timeout to change the detection method/approach
"""

# set a detection threshold
detection_threshold = 2.0

# set a heart beat time out
detection_time_out = 50

# track the last time we found a beat
last_detected_index = -1

# keep not of where we are in the data
current_index = 0

# store indices of all found beats
beats_detected = list()

"""
Step 4: Use Find Peaks
"""

# you may want to explore various parameters for the function that will help you!
peaks, _ = find_peaks(signal)
print("Within the sample we found ", len(peaks), " heart beats with find_peaks!")

# plot all the find_peaks results on the same graph
plt.plot(signal)
plt.title('Filtered ECG Signal with Beat Annotations')

plt.plot(peaks, signal[peaks], 'X')
plt.show()
