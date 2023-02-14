import random
import numpy as np


# copy in Dr. Forsyth's random list function for use
def generate_random_int_list(list_length, upper_bound):
    # given the length above, sample the Natural Numbers up to upper_bound that many times
    randoms = random.sample(range(upper_bound), list_length)

    # return the generated list
    return randoms

def dot_product(a,b):
    """
    A custom function to calculate the dot product of two lists
    :param a: List A of values
    :param b: List B of values
    :return: The dot product as a value between a * b
    """

    ### YOUR CODE HERE ###


    ### CHANGE THIS RETURN VALUE. IT IS HERE SO THE CODE DOES NOT ERROR
    return None

"""
Step 1: Generate two "vectors" of equal length but full of random values
"""
max_length = 10
maximum_value = 100
fixed_length = int(random.uniform(2, max_length))
vector_a = generate_random_int_list(fixed_length, maximum_value)
vector_b = generate_random_int_list(fixed_length, maximum_value)

"""
Step 2: Call your custom dot_product function
"""
result = dot_product(vector_a,vector_b)

"""
Step 3: Check your calculation against numpy
"""
true_result = np.dot(vector_a,vector_b)

"""
Step 4: See if you're correct....
"""
if result is None:
    print("Result is None. You didn't change the result statement in the function")

elif abs(result - true_result) < 0.0001:
    print("Correct!")

else:
    print("Result contains too much error!")