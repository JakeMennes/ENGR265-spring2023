import numpy as np
import os
import math
import sys


def parse_tensile_file(path_to_file):
    file = open(path_to_file)
    # required meta-data
    gage_diameter = -1
    maximum_force = - 1
    maximum_strain = -1
    # determine when to begin reading into these files
    begin_reading = False
    time = []
    displacement = []
    force = []
    strain = []
    # begin iterating through file
    for line in file:
        if line == '' or line == '\n':
            continue

        splits = line.strip().split(",")

        if begin_reading == False:

            # gather various meta data
            if splits[0] == "Gage Diameter":
                cleaned = splits[2].replace('\"', '')
                gage_diameter = float(cleaned)
            if splits[0] == "Maximum Force":
                cleaned = splits[2].replace('\"', '')
                maximum_force = float(cleaned)
            if splits[0] == "Maximum Strain":
                cleaned = splits[2].replace('\"', '')
                maximum_strain = float(cleaned)

        else:
            # parse the actual data
            time.append(float(splits[0].replace('\"', '')))
            displacement.append(float(splits[1].replace('\"', '')))
            force.append(float(splits[2].replace('\"', '')))
            strain.append(float(splits[3].replace('\"', '')))

        # try to find start of data
        if splits[0] == "(s)":
            begin_reading = True
    file.close()

    return gage_diameter, np.asarray(time), np.asarray(displacement), np.asarray(force), np.asarray(strain)


def calculate_stress(force, sample_diameter):
    """
    Calculate the stress (MPa) experienced by the test given a series of forces/loads (kN) and
    a sample diameter (mm)
    :param force: An array of forces/loads applied to the sample in Kilo Newtons (kN)
    :param sample_diameter: The diameter of the sample in millimeters (mm)
    :return: An array of stresses experienced by the sample in Kilo Pascals (KPa)
    """

    # calculate the cross-section area (mm^2)
    ### your code here ###

    # calculate stress (MPa) from load (kN) and cross-sectional area
    ### your code here ###

    # delete this line and replace it with your own
    stress = None

    return stress



if __name__ == "__main__":
    import matplotlib.pyplot as plt

    # modify this line to select different materials/folders within tensile/
    material_folder = "1045CR"

    # modify this line to select different samples in the material folder
    sample_name = "C01A1045CR_1"


    ### Do not modify below this line ###

    path_to_directory = "../../../data/tensile/"
    path_to_samples = path_to_directory + material_folder + "/"

    # manually parse file to get gage diameter and then calculate cross-sectional area
    path_to_file = path_to_samples + sample_name + ".csv"

    # Step #1: Parse the file ane return based values
    # sample diameter (mm), time (s), displacement (mm), force (kN), and strain (%)
    sample_diameter, time, displacement, force, strain = parse_tensile_file(path_to_file)

    # Step #1: Given the forces and sample diameter, calculate the strain
    stress = calculate_stress(force, sample_diameter)

    if stress is None:
        print("Error! No stress returned. Did you fill in the calculate_stress() method?")
        sys.exit(-1)

    # use scatter plot so we don't assume a line (yet)
    plt.scatter(strain, stress, label="Stress - Strain")
    plt.xlabel('Strain (mm/mm)')
    plt.ylabel('Stress (MPa)')
    plt.title('Stress-Strain Curve for Sample ' + sample_name)
    plt.show()