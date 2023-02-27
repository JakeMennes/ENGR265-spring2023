import math

A = 1
B = 1/(math.pow(2, (1/2)))
T = 1/4
P = 1
def my_pi(desired_error):
    """
    Implementation of Gauss–Legendre algorithm to approximate PI from https://en.wikipedia.org/wiki/Gauss%E2%80%93Legendre_algorithm

    :param target_error: Desired error for PI estimation
    :return: Approximation of PI to specified error bound
    """
    A = 1
    B = 1 / (math.pow(2, (1 / 2)))
    T = 1 / 4
    P = 1
    for i in range(0, 11):
        # New names
        aN = (A + B) / 2
        bN = math.pow(A * B, (1 / 2))
        tN = T - (P * (math.pow((A - aN), 2)))
        pN = 2 * P
        # Calculate Pie
        approximation = math.pow((aN + bN), 2) / (4 * tN)
        A = aN
        B = bN
        T = tN
        P = pN
    return approximation

desired_error = 1E-10

approximation = my_pi(desired_error)

print("Solution returned PI=", approximation)

error = abs(math.pi - approximation)

if error < abs(desired_error):
    print("Solution is acceptable")
else:
    print("Solution is not acceptable")
