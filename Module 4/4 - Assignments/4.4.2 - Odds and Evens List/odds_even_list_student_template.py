# bring in randomness cause we need it in our lives
import random


# copy in Dr. Forsyth's random list function for use
def generate_random_int_list(max_length, upper_bound):
    # generate random length between 2 and max_length
    list_length = int(random.uniform(2, max_length))

    # given the length above, sample the Natural Numbers up to upper_bound that many times
    random_vars = random.sample(range(upper_bound), list_length)

    # return the generated list
    return random_vars


"""
Given a random list of integers, return two lists of only even and odd values from that random list
"""
# generate two random lists of integers
max_length = 20
upper_bound = 100
nums = generate_random_int_list(max_length, upper_bound)

# lists to hold the even and odd numbers
# do not modify their names
evens_list = []
odds_list = []

"""
Step 1: Write a FOR loop to iterate through the list nums
"""


"""
Step 2: Inside the FOR loop, examine the contents of nums. If the
value is even, place it in the evens_list. If it is odd, place it in the 
odds_list
"""

print("The evens list contains: ", evens_list)
print("The odds list contains: ", odds_list)


