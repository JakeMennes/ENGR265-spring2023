import numpy as np
from scipy.stats import norm, expon
import matplotlib
import matplotlib.pyplot as plt
import pandas as pd
import platform

# a fix for Dr. Forsyth's computer
# https://stackoverflow.com/questions/56013105/matplotlib-plot-window-is-white-blank-without-showing-any-image
if platform.system() == 'Darwin':
    matplotlib.use('MacOSX')

"""
Part 1: Do something simple. Sample the normal distribution and see how many points
are needed to make a "good" fit.
Normal distribution refresher: https://en.wikipedia.org/wiki/Normal_distribution
"""

# desired average of normal distribution
desired_mu = 0

# desired standard deviation
desired_std = 1

# number of samples to take
num_samples = 100

# generate those samples with numpy
# https://numpy.org/doc/stable/reference/random/generated/numpy.random.normal.html
normal_samples = np.random.normal(loc=desired_mu, scale=desired_std, size=num_samples)

# now, find the mean and std of this distribution
sample_mean = np.mean(normal_samples)
sample_std_dev = np.std(normal_samples)

# given this sample mean and std, get a probability distribution function and plot it
# use lin space to make a vector with a linear spacing of points between start and stop
# https://numpy.org/doc/stable/reference/generated/numpy.linspace.html
x = np.linspace(start=-3, stop=3, num=10000)

# use the normal distribution probability density function to generate results
# https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.norm.html#scipy.stats.norm
y = norm.pdf(x, loc=sample_mean, scale=sample_std_dev)

# plot the sampled distribution
plt.plot(x, y, label='Fitted Normal')
plt.title('Fitted Normal Distribution for ' + str(num_samples) + ' Sampled Points')
plt.xlabel('X')
plt.ylabel('Probability of X')

# sample the 'correct' distribution to generate another plot
x = np.linspace(start=-3, stop=3, num=10000)
y = norm.pdf(x, loc=desired_mu, scale=desired_std)
plt.plot(x, y, label='Ideal Normal')

# include a legend
plt.legend()

# show the plot
plt.show()

# Future work: show histogram of points as well....

"""
Part 2: Try the same thing but with the exponential distribution. See if the same process works...
Exponential distribution refresher: https://en.wikipedia.org/wiki/Exponential_distribution
"""

# desired shape parameter for exponential distribution
desired_lambda = 0.2

# translate into desired beta
desired_beta = 1 / desired_lambda

# number of samples to take
num_samples = 50

# generate those samples with numpy
# https://numpy.org/doc/stable/reference/random/generated/numpy.random.exponential.html
exponential_samples = np.random.exponential(scale=desired_beta, size=num_samples)

# we can't now just find the mean and standard deviation. The points must be 'fit' to the curve
# use the fit() method to estimate the shape parameters for the exponential distribution
# https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.rv_continuous.fit.html#scipy.stats.rv_continuous.fit
(fit_loc, fit_scale) = expon.fit(exponential_samples)

# pull out beta from the fitted distribution
fit_beta = fit_scale

# given this sample beta, get a probability distribution function and plot it
# use lin space to make a vector with a linear spacing of points between start and stop
# https://numpy.org/doc/stable/reference/generated/numpy.linspace.html
x = np.linspace(start=0, stop=50, num=10000)

# use the exponent distribution probability density function to generate results
# https://numpy.org/doc/stable/reference/random/generated/numpy.random.exponential.html
y = expon.pdf(x, scale=fit_beta)

# plot the sampled distribution
plt.plot(x, y, label='Fitted Exponential')
plt.title('Fitted Exponential for ' + str(num_samples) + ' Sampled Points')
plt.xlabel('X')
plt.ylabel('Probability of X')

# same the 'correct' distribution to generate another plot
x = np.linspace(start=0, stop=50, num=10000)
y = expon.pdf(x, scale=desired_beta)
plt.plot(x, y, label='Ideal Exponential')

# include a legend
plt.legend()

# show the plot
plt.show()

"""
Part 3: Load up some data and fit it to a distribution
"""

# load up the RSI data results with force plate and accelerometer results
df = pd.read_csv('../../data/drop-jump/all_participant_data_rsi.csv')

# pull out the force plate column
force_plate_rsi = df['force_plate_rsi'].to_numpy()

# pull out the accelerometer column
accel_rsi = df['accelerometer_rsi'].to_numpy()

# calculate error assuming that force plate was computed correctly
error = force_plate_rsi - accel_rsi

# generate a histogram to see what the data looks like
plt.hist(error, bins=15, label='RSI Error')
plt.xlabel('Relative RSI Error')
plt.ylabel('Counts')
plt.title('Distribution of RSI Error')
plt.show()

# now, let's map the RSI error to the normal distribution with scipy fit
(fitted_mean, fitted_std) = norm.fit(error)

# same the 'correct' distribution to generate another plot
x = np.linspace(start=-2, stop=2, num=10000)
y = norm.pdf(x, loc=fitted_mean, scale=fitted_std)
plt.plot(x, y, label='Fitted Normal Curve')

# include a legend
plt.legend()

# show the plot
plt.show()

# print out the results
print('Parameters for fitted distribution are mu=', fitted_mean, ' and std=', fitted_std)

# since we have the fitted data, we can now determine useful parameters such as the 95%
# confidence interval with scipy
# Note: ALPHA parameter has been depreciated as of scipy 1.10.0. May throw warning.
(lower_ci, upper_ci) = norm.interval(alpha=0.95, loc=fitted_mean, scale=fitted_std)

# print out the results
print('For the fitted RSI data. The 95% confidence interval is: (', lower_ci, ",", upper_ci, ")")
