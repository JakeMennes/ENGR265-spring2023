import numpy as np
import pandas as pd
from scipy.stats import ttest_1samp, norm, ttest_ind

"""
Part 1: Perform a simple one-sided t-test to determine if sample means match an expected population means.
Test and data are pulled from Example: Left-Tailed Test 
at https://online.stat.psu.edu/statprogram/reviews/statistical-concepts/hypothesis-testing/examples
"""

print('Testing sample hardness...')

# build python example based off: https://online.stat.psu.edu/statprogram/reviews/statistical-concepts/hypothesis-testing/examples
hardness = [170, 167, 174, 179, 179, 187, 179, 183, 179, 156, 163, 156, 187, 156, 167, 156, 174, 170, 183, 179, 174,
            179, 170, 159, 187]

# convert to numpy array
hardness = np.asarray(hardness)

# generate some stats from sample
mean = np.mean(hardness)
stdev = np.std(hardness)

# write down our expected values
expected_mean = 170

# establish a level of significance
alpha = 0.05

# hypothesis H0: mean hardness is 170
# alternative H1: mean hardness is > 170
(stat, p_value) = ttest_1samp(hardness, popmean=expected_mean, alternative='greater')

# based upon the results of our t-test, determine whether means are equal or not....
if p_value < alpha:
    print('Reject H0: sample means and population means are not equal!')

else:
    print('Accept H0: sample means and population means are equivalent')

"""
Part 2: Perform a simple one-sided t-test to determine if sample means match an expected population means.
Test and data are pulled from Example: Right-Tailed Test 
at https://online.stat.psu.edu/statprogram/reviews/statistical-concepts/hypothesis-testing/examples
"""

print('\nTesting plant height...')

# build python example based off: https://online.stat.psu.edu/statprogram/reviews/statistical-concepts/hypothesis-testing/examples
heights = [11.5, 11.8, 15.7, 16.1, 14.1, 10.5, 9.3, 15.0, 11.1, 15.2, 19.0, 12.8, 12.4, 19.2, 13.5, 12.2, 13.3, 16.5,
           13.5, 14.4, 16.7, 10.9, 13.0, 10.3, 15.8, 15.1, 17.1, 13.3, 12.4, 8.5, 14.3, 12.9, 13.5]

# convert to numpy array
heights = np.asarray(heights)

# generate some stats from sample
mean = np.mean(heights)
stdev = np.std(heights)

# write down our expected values
expected_mean = 15.7

# establish a level of significance
alpha = 0.05

# hypothesis H0: mean hardness is 15.7
# alternative H1: mean hardness is < 15.7
(stat, p_value) = ttest_1samp(heights, popmean=expected_mean, alternative='less')

# based upon the results of our t-test, determine whether means are equal or not....
if p_value < alpha:
    print('Reject H0: sample means and population means are not equal!')

else:
    print('Accept H0: sample means and population means are equivalent')

"""
Part 3: Perform a simple two-sided t-test to determine if sample means match an expected population means.
Test and data are pulled from Example: Two-Tailed Test 
at https://online.stat.psu.edu/statprogram/reviews/statistical-concepts/hypothesis-testing/examples
"""
print('\nTesting gum thickness...')

# load sample thickness
thickness = [7.65, 7.60, 7.65, 7.70, 7.55, 7.55, 7.40, 7.40, 7.50, 7.50]

# convert to numpy array
thickness = np.asarray(thickness)

# generate some stats from sample
mean = np.mean(thickness)
stdev = np.std(thickness)

# write down our expected values
expected_mean = 7.5

# establish a level of significance
alpha = 0.05

# hypothesis H0: mean thickness is 7.5
# alternative H1: mean hardness is not 7.5
(stat, p_value) = ttest_1samp(thickness, popmean=expected_mean, alternative='two-sided')

# based upon the results of our t-test, determine whether means are equal or not....
if p_value < alpha:
    print('Reject H0: sample means and population means are not equal!')

else:
    print('Accept H0: sample means and population means are equivalent')

"""
Part 4: Attempt t-test again but with tensile data. Determine if 1045CR steel has
yield strength of at least 500 MPa
"""

print('\nTesting yield strength...')

# path to raw tensile data
path_to_file = '../../data/tensile/tensile_data.csv'

# load all tensile data into data frame
df = pd.read_csv(path_to_file)

# get all results from one type of material
cold_rolled = df[df['Material_Type'] == '1045CR']

# pull out the yield strength information
yield_strength = cold_rolled['Yield_Strength']

# generate some stats
mean = yield_strength.mean()
stdev = yield_strength.std()

# Note: ALPHA parameter has been depreciated as of scipy 1.10.0. May throw warning.
(lower_ci, upper_ci) = norm.interval(alpha=0.95, loc=mean, scale=stdev)

# print out the results
print('For the 1045CR. The 95% confidence interval on yield strength is: (', lower_ci, ",", upper_ci, ")")

# write down our expected values
expected_yield_strength = 500

# establish a level of significance
alpha = 0.05

# hypothesis H0: mean yield strength is 500 MPa
# alternative H1: mean yield strength is > 500 MPa
(stat, p_value) = ttest_1samp(yield_strength, popmean=expected_yield_strength, alternative='greater')

# based upon the results of our t-test, determine whether means are equal or not....
if p_value < alpha:
    print('Reject H0: sample means and population means are not equal!')

else:
    print('Accept H0: sample means and population means are equivalent')

"""
Part 5: Perform random samples from two independent distributions. Determine if their means are equal.
Will use independent / two-sample T-test on two exact distributions to show equivalence. 
"""
print('\nComparing two equivalent random distributions. Should be equal means.')
num_samples = 100

# parameters for distribution 1
dist1_mean = 0
dist1_std = 1

# take samples from distribution
dist1 = np.random.normal(loc=dist1_mean, scale=dist1_std, size=num_samples)

# parameters for distribution 2
dist2_mean = 0
dist2_std = 1

# take samples from distribution
dist2 = np.random.normal(loc=dist2_mean, scale=dist2_std, size=num_samples)

# hypothesis H0: means are equivalent between population samples
# alternative H1: means are NOT equivalent between population samples
(stat, p_value) = ttest_ind(dist1, dist2, alternative='two-sided')

# establish a level of significance
alpha = 0.05

# based upon the results of our t-test, determine whether means are equal or not....
if p_value < alpha:
    print('Reject H0: two sampled population means are NOT equivalent!')

else:
    print('Accept H0: two sampled population means are equivalent')

"""
Part 6: Perform random samples from two independent distributions. Determine if their means are equal.
Will use independent / two-sample T-test on two different distributions to show not equivalence. 
"""
print('\nComparing two not equivalent random distributions. Should not be equal means.')
num_samples = 100

# parameters for distribution 1
dist1_mean = 0
dist1_std = 1

# take samples from distribution
dist1 = np.random.normal(loc=dist1_mean, scale=dist1_std, size=num_samples)

# parameters for distribution 2
dist2_mean = 5
dist2_std = 3

# take samples from distribution
dist2 = np.random.normal(loc=dist2_mean, scale=dist2_std, size=num_samples)

# hypothesis H0: means are equivalent between population samples
# alternative H1: means are NOT equivalent between population samples
(stat, p_value) = ttest_ind(dist1, dist2, alternative='two-sided')

# establish a level of significance
alpha = 0.05

# based upon the results of our t-test, determine whether means are equal or not....
if p_value < alpha:
    print('Reject H0: two sampled population means are NOT equivalent!')

else:
    print('Accept H0: two sampled population means are equivalent')