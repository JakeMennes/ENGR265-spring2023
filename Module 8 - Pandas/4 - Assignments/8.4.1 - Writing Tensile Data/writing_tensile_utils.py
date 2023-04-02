import math

import numpy as np


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
    cross_sectional_area = math.pi * (sample_diameter / 2) ** 2

    # calculate stress (MPa) from load (kN) and cross-sectional area
    stress = force / cross_sectional_area * 1000

    return stress


def calculate_max_strength_strain(strain, stress):
    """
    Calculate the Ultimate Tensile Stress and Fracture Strain
    :param strain: An array of Strain data (MPa)
    :param stress: An array of Stress data
    :return:
    Ultimate Tensile Stress: the maximum stress experienced
    Fracture Strain: the maximum strain experienced before fracture
    """

    ultimate_tensile_stress = max(stress)

    fracture_strain = max(strain)

    return ultimate_tensile_stress, fracture_strain


def calculate_elastic_modulus(strain, stress):
    """
    Given a set of stress strain data, use the Secant Modulus at 40% method to determine
    the elastic modulus
    :param strain: An array of Strain data (MPa)
    :param stress: An array of Stress data
    :return:
    linear_index: the index within the strain/stress data that is the end of the linear region
    slope: the slope for the linear region of the strain/stress data
    intercept: y-intercept for linear region best fit of strain/stress data
    """

    # Step 3a: find the point that is 40% of peak strain
    # use from 0 to that value to create a linear plot
    secant_strain = max(stress) * 0.40

    # Step 3b: find the index closes to that
    # take the diff of the whole array and argmin
    diffs = np.abs(stress - secant_strain)
    linear_index = np.argmin(diffs)

    # Step 3c: down select to linear region for stress and strain
    linear_stress = stress[0:linear_index]
    linear_strain = strain[0:linear_index]

    # Step 3d: find least squares fit to a line in the linear region
    # use 1-degree polynominal fit (line)
    slope, intercept = np.polyfit(linear_strain, linear_stress, 1)

    return linear_index, slope, intercept

def calculate_yield_strength(strain, stress, modulus, offset=0.002):
    """
    Determine the yield strength via 0.2% offset method
    :param strain: An array of Strain data (mm/mm)
    :param stress: An array of Stress data (MPa)
    :param modulus: The elastic modulus of the material
    :param offset: Desired offset. Default is 0.002 (0.2%)
    :return: Y-intercept of line that originates at (0,.002) with modulus slope
    """

    # next to find point that intersects y=m(x-0.002) + 0
    # calculate the offset line
    offset_line = modulus * (strain - offset)

    # measure distance from all points on graph to this line
    distance = abs(stress - offset_line)
    intercept_index = np.argmin(distance)

    return stress[intercept_index]


class MaterialSample:
    """
    A simple class to hold results from materials tensile analysis
    """

    def __init__(self):
        self.name = ""
        self.material_type = ""
        self.tensile_strength = -1
        self.fracture_strain = -1
        self.elastic_modulus = -1
        self.yield_strength = -1
