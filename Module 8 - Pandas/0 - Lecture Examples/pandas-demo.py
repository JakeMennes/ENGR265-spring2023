import pandas as pd

if __name__ == "__main__":

    # copy in the data frame from the DataCamp guide
    data = {'Country': ['Belgium', 'India', 'Brazil'],
            'Capital': ['Brussels', 'New Delhi', 'Brasilia'],
            'Population': [11190846, 1303171035, 207847528]}

    # load raw data as data frame
    df = pd.DataFrame(data)

    # print out the whole data frame
    print(df)

    # print out the columns
    for c in df.columns:
        print(c)

    # select the 'Country' column, should generate a Series
    countries = df['Country']

    # print out all countries
    print(countries)

    # can perform more complex selection. Choose all countries where the capital population
    # is greater than 15 Million people. Should result in New Delhi and Brasilia
    large_capitals = df[df['Population'] > 15000000]

    # print out cities with large capitals
    print(large_capitals)

    # for another boolean selection, grab all data where the country is Brazil
    brazil_data = df[df['Country'] == 'Brazil']

    # print out brazil information
    print(brazil_data)

    # once an column of interest is identified, it is easy enough to convert into a numpy array
    np_array = df['Population'].to_numpy()

    # should result in column vector. Print out.
    print(np_array)


