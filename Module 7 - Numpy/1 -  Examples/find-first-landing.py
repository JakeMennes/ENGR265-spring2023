import numpy as np
from os import path
import scipy.constants as constants


def main(full_path_to_file):
    """
    Given a file containing force plate drop jump data, find the first index/point upon which the participant lands
    on the plate

    :param full_path_to_file: A file path to a text file
    :return: signal,index: The signal data from the force plate file and the index of the first landing

    """

    # perform a basic check to see if the file exists. If not, exit the program
    if not path.exists(full_path_to_file):
        print("File does not exist", full_path_to_file)
        return None

    # load the data from the file
    data = np.loadtxt(full_path_to_file, delimiter=",")

    # select the 8th column as the force plate data
    force_plate = data[:, 8]

    # save the sampling rate for this data (samples/second)
    sampling_rate = 1000

    # set an amount of time to average and find the baseline
    baseline_length = 20

    # Step 1: Establish a baseline by examining the the after for first ~20 points
    baseline = np.average(force_plate[0:baseline_length])

    # Step 2: After the baseline, find the first point that rises above that value
    # given some acceptable delta

    # when the signal exceeds the baseline plus delta, that is the landing point
    delta = 5

    # make a variable to hold the INDEX of that landing point. We will later convert that
    # index to time based upon the force plate sample rate
    first_landing_index = -1

    # Approach 1: Make the array a list so we can iterate through it. There will be better and
    # more Python friendly ways to do this but this is a general approach.
    force_plate_list = force_plate.tolist()

    # walk through the list but start at the end of our baseline
    for index in range(baseline_length, len(force_plate_list)):
        value = force_plate_list[index]

        # if signal is rising
        if value > baseline + delta:
            # mark this index as the landing point
            first_landing_index = index

            # break out of the loop to end iterating
            break

    #### do not modify code below here ###

    # normalize the force plate data so that it will plot correctly when complete
    signal = force_plate - baseline

    return signal, first_landing_index


if __name__ == "__main__":
    # need to import this here so it won't eventually affect the autograder
    import matplotlib.pyplot as plt

    # change this file name to load other datasets
    filename = "FP1.txt"

    # load force plate data (this path may change based upon where you place this file in your project)
    path_to_data_folder = "../../data/drop-jump/force-plate/"

    ### Do not modify below this line ###

    # put together directory and file to make a single relative path
    full_path_to_file = path_to_data_folder + filename

    # call the student function to return the signal and jump/landing indices
    (signal, first_landing_index) = main(full_path_to_file)

    # print out some debug information
    print("First landing: ", first_landing_index)

    # plot the data with matplotlib
    # make a nice plt of results
    plt.title('RSI Force Plate Data for Trial ' + filename)

    # plot the signal itself
    plt.plot(signal, label="Force Plate Data")

    # plot the various landing points
    plt.plot(first_landing_index, signal[first_landing_index], 'v', label="First Landing")

    # show the legend
    plt.legend()

    # uncomment line to show the plot
    plt.show()
