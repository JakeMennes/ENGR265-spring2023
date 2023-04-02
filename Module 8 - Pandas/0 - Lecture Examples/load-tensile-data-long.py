import pandas as pd

if __name__ == "__main__":

    # path to overall file
    path_to_file = "../../data/tensile/tensile_data.csv"

    # load data into dataframe
    df = pd.read_csv(path_to_file)

    # print out data frame just for fun
    print(df)

    # get all results from one type
    cold_rolled = df[df['Material_Type'] == '1045CR']

    stainless_steel = df[df['Material_Type'] == '2024']

    plastic = df[df['Material_Type'] == 'PMMA']

    # print out each material type
    print(cold_rolled)

    print(stainless_steel)

    print(plastic)



    # Approach 1: Parse all columns to get print out a decent table
    # of all mean +/- std of all materials

    # determine averages/deviations on elastic modulus of each material
    cr_modulus_avg = cold_rolled['Elastic_Modulus'].mean()
    cr_modulus_std = cold_rolled['Elastic_Modulus'].std()

    ss_modulus_avg = stainless_steel['Elastic_Modulus'].mean()
    ss_modulus_std = stainless_steel['Elastic_Modulus'].std()

    pmma_modulus_avg = plastic['Elastic_Modulus'].mean()
    pmma_modulus_std = plastic['Elastic_Modulus'].std()

    # determine averages/deviations on yield strength of each material
    cr_yieldstrength_avg = cold_rolled['Yield_Strength'].mean()
    cr_yieldstrength_std = cold_rolled['Yield_Strength'].std()

    ss_yieldstrength_avg = stainless_steel['Yield_Strength'].mean()
    ss_yieldstrength_std = stainless_steel['Yield_Strength'].std()

    pmma_yieldstrength_avg = plastic['Yield_Strength'].mean()
    pmma_yieldstrength_std = plastic['Yield_Strength'].std()

    # print out results
    print("Material\tElastic Modulus\tYield Strength")

    print("1045CR\t", round(cr_modulus_avg, 2), "+/-", round(cr_modulus_std, 2),
          "\t", round(cr_yieldstrength_avg, 2), "+/-", round(cr_yieldstrength_std, 2))

    print("2024\t", round(ss_modulus_avg, 2), "+/-", round(ss_modulus_std, 2),
          "\t", round(ss_yieldstrength_avg, 2), "+/-", round(ss_yieldstrength_std, 2))

    print("PMMA\t", round(pmma_modulus_avg, 2), "+/-", round(pmma_modulus_std, 2),
          "\t", round(pmma_yieldstrength_avg, 2), "+/-", round(pmma_yieldstrength_std, 2))

    # add some space after the table
    print("\n")

