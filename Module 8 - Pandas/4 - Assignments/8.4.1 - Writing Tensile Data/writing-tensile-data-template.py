from writing_tensile_utils import *
import os
import sys


def generate_csv_file(filename, results):
    """
    A function to take a list of material strength results and print to a CSV file
    :param filename: File that should be written to
    :param results: Material strength results as list of Material Sample objects
    :return: True if data was written out to the file successfully, false otherwise
    """

    # Step 1: create a variable to hold the file name

    # uncomment this line
    # output_file_name = ### your code here ###

    # Step 2: use open() to open the file in write mode. Set the return of open()
    # to a variable name that will be your file handle

    # uncomment the line below
    # file = ### your code here ###

    # Step 3: write out the header for the CSV file. This string is provided for you so
    # your data can be loaded and checked. Use write().
    file_header = "Sample_Name,Material_Type,Tensile_Strength,Fracture_Strain,Elastic_Modulus,Yield_Strength\n"

    # write header string out to file
    # file.### your code here ###

    # Step 4: Iterate through the list of results. Each sample will contain the data for an individual test
    # The Materials Object will contain sample name, type, tensile strength, fracture strain, elastic modulus,
    # and yield strength data
    for r in results:
        # Each object in the results list is of class SampleMaterial. This is just a dummy class to hold variables
        # in a single object. For your ease they have been broken out into individual variable names
        name = r.name
        material_type = r.material_type
        tensile_strength = r.tensile_strength
        fracture_strain = r.fracture_strain
        modulus = r.elastic_modulus
        yield_strength = r.yield_strength

        # Step 5: Stitch together a string, then write out the string via write().
        # Many variables above must be converted to a string via (). Commas also must be manually
        # stitched between each variable in the output. Do not round the data
        # Make sure an endline character '\n' is always at the end of your string!

        # uncomment the line below
        # string_to_write = ### your code here ###

        # Finally, given that long string, write it to a file

        ### your code here ###

    # close the file once all writing is complete
    # uncomment this line before you're done
    ##file.close()

    # since we got here, it must have worked.
    return True


if __name__ == "__main__":

    # get path to data/ folder
    path_to_tensile_folder = "../../../data/tensile/"

    # list to hold all sample results
    results = []

    # each folder in data/ is a different material
    materials = list()
    for root, dirs, files in os.walk(path_to_tensile_folder):
        materials.extend(dirs)
        break

    # now walk through each material and file
    for material in materials:
        print("Parsing material: ", material)

        # walk through folder
        path_to_material_folder = path_to_tensile_folder + material + "/"
        for root, dirs, files in os.walk(path_to_material_folder):

            # parse each file that was found
            for file_name in files:
                print("\tLoad sample: ", file_name)

                # create path to sample file
                path_to_sample = path_to_material_folder + file_name

                # Parse the file ane return based values
                # sample diameter (mm), time (s), displacement (mm), force (kN), and strain (%)
                sample_diameter, time, displacement, force, strain = parse_tensile_file(path_to_sample)

                # Given the forces and sample diameter, calculate the strain
                stress = calculate_stress(force, sample_diameter)

                if stress is None:
                    print("Error! No stress returned. Did you fill in the calculate_stress() method?")
                    sys.exit(-1)

                # calculate easy variables
                ultimate_tensile_strength, fracture_strain = calculate_max_strength_strain(strain, stress)

                if ultimate_tensile_strength == -1 or fracture_strain == -1:
                    print(
                        "Error! Tensile Strength or Fracture Strain returned as -1. Did you complete the calculate_max_strength() method?")
                    sys.exit(-1)

                # Use the Secant Modulus at 40% of Peak Stress
                # to determine elastic modulus
                linear_index, slope, intercept = calculate_elastic_modulus(strain, stress)

                elastic_modulus = slope / 1000

                # Calculate Yield Strength
                yield_strength = calculate_yield_strength(strain, stress, slope)

                # create a new material sample
                sample = MaterialSample()
                sample.name = file_name.split(".")[0]
                sample.material_type = material
                sample.tensile_strength = ultimate_tensile_strength
                sample.fracture_strain = fracture_strain
                sample.elastic_modulus = elastic_modulus
                sample.yield_strength = yield_strength

                # place in list
                results.append(sample)

    # manually print out the results to see what you have
    for r in results:
        print("Sample Name: ", r.name)
        print("\tMaterial Type: ", r.material_type)
        print("\tTensile Strength: ", r.tensile_strength)
        print("\tFracture Strain: ", r.fracture_strain)
        print("\tElastic Modulus: ", r.elastic_modulus)
        print("\tYield Strength: ", r.yield_strength)

    generate_csv_file('tensile_data.csv', results)

    print("Done!")
