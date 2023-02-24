import numpy as np
from os import path
import scipy.constants as constants


def main(full_path_to_file):
    """
    Given a file containing force plate drop jump data, find the first/second landings and take off point

    :param full_path_to_file: A file path to a text file
    :return: signal, first_landing_index, take_off_index, second_landing_index, RSI:
    signal: The signal data from the force plate file
    first_landing_index: Index within the signal of the first landing point
    take_off_index: Index within the signal of the take-off point
    second_landing_index: Index within the signal of the first landing point
    RSI: Calculated reactive strength index
    """


    # perform a basic check to see if the file exists. If not, exit the program
    if not path.exists(full_path_to_file):
        print("File does not exist", full_path_to_file)

    # load the data from the file
    data = np.loadtxt(full_path_to_file, delimiter=",")

    # select the 8th column as the force plate data
    force_plate = data[:, 8]

    # save the sampling rate for this data (samples/second)
    sampling_rate = 1000

    # Step 1: Establish a baseline by examining the the after for first ~20 points

    # set an amount of time to average and find the baseline
    baseline_length = 0 ### your code here ###

    # over the baseline, determine the average signal value
    baseline = 0 ### your code here ###

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
        # grab the current value in the list
        value = force_plate_list[index]

        # if signal is rising
        if value > baseline + delta:
            # mark this index as the landing point

            ### your code here ###

            # break out of the loop to end iterating
            break

    # Step 3: When force measurements return to the initial baseline the user has left the plate.
    # Consider this the take off point.

    # when the signal falls below the baseline plus delta, that is the take off point
    delta = 5

    # make a variable to hold the INDEX of that take-off point. We will later convert that
    # index to time based upon the force plate sample rate
    take_off_index = -1

    # iterate through force plate data but do not begin at the start of the array
    # being after the user has taken off. If the searching starts at the beginning again
    # then may accidentally find a point that is "too early" in the data

    # walk through the list but start a few moments after the at the landing index
    # since we know the take off point will be afterwards.
    for index in range(first_landing_index + 10, len(force_plate_list)):

        ### your code here ###
        delete_me = 0


    # Step 4: The plate should remain near baseline while the user is in the air (there is no load).
    # Once it rises above the baseline again, the user has landed. Consider this the second landing.
    # This code block should be the same (functionally) as Step 2 but starting at a different point

    # when the signal falls above the baseline plus delta, that is the take off point
    delta = 5

    # variable to hold the index for the second landing
    second_landing_index = -1

    # walk through the list but start a few moment after the takeoff point
    for index in range(take_off_index + 10, len(force_plate_list)):

        ### your code here ###
        delete_me = 0

    # Step 5: calculate the time of contact on plate and time of flight in air

    # calculate tc and convert to seconds using the sampling rate
    time_of_contact = 0 ### your code here ###

    # calculate tf and convert to seconds using the sampling rate
    time_of_flight = 0 ### your code here ###

    # Step 6: Calculate the Reactive Strength Index

    # pull the local gravitational acceleration from scipy
    g = constants.g

    # RSI = (g*tf^2) / (8*tc)
    RSI = 0 ### your code here ###

    ### Do not modify below this line ###

    # normalize the force plate data so that it will plot correctly when complete
    signal = force_plate - baseline

    return signal, first_landing_index, take_off_index, second_landing_index, RSI


if __name__ == "__main__":
    # need to import this here so it won't eventually affect the autograder
    import matplotlib.pyplot as plt

    # change this file name to load other datasets
    filename = "FP1.txt"

    # load force plate data (this path may change based upon where you place this file in your project)
    path_to_data_folder = "../../../data/drop-jump/force-plate/"

    ### Do not modify below this line ###

    # put together directory and file to make a single relative path
    full_path_to_file = path_to_data_folder + filename

    # call the student function to return the signal and jump/landing indices
    (signal, first_landing_index, take_off_index, second_landing_index, RSI) = main(full_path_to_file)

    # print out some debug information
    print("First landing: ", first_landing_index)
    print("Take off: ", take_off_index)
    print("Second landing: ", second_landing_index)
    print("Calculated RSI: ", RSI)

    # plot the data with matplotlib
    # make a nice plt of results
    plt.title('RSI Force Plate Data for Trial ' + filename)

    # plot the signal itself
    plt.plot(signal, label="Force Plate Data")

    # plot the various landing points
    plt.plot(first_landing_index, signal[first_landing_index], 'v', label="First Landing")
    plt.plot(take_off_index, signal[take_off_index], 'v', label="Jump / Take-Off")
    plt.plot(second_landing_index, signal[second_landing_index], 'v', label="Second Landing")

    # show the legend
    plt.legend()

    # uncomment line to show the plot
    plt.show()
