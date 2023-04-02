import numpy as np
import pandas as pd

if __name__ == "__main__":
    # path to overall file
    path_to_file = "../data/tensile/tensile_data.csv"

    # load data into dataframe
    df = pd.read_csv(path_to_file)

    # Approach 2: Use the unique() function in pandas to get a list of
    # all materials. Do not need to manually specify

    # get all materials as numpy array
    materials = df['Material_Type'].unique()

    # convert to a list for easy iteration
    materials = materials.tolist()

    # being printing table while we iterate
    print("Material\tElastic Modulus\tYield Strength")

    for mat in materials:
        material_statistics = df[df['Material_Type'] == mat]
        yield_strength = material_statistics['Yield_Strength']
        elastic_modulus = material_statistics['Elastic_Modulus']

        yield_avg = yield_strength.mean()
        yield_std = yield_strength.std()

        modulus_avg = elastic_modulus.mean()
        modulus_std = elastic_modulus.std()

        print(mat, "\t", round(modulus_avg, 2), "+/-", round(modulus_std, 2),
              "\t", round(yield_avg, 2), "+/-", round(yield_std, 2))

    print("Done!")