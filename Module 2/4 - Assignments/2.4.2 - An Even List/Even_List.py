import random

"""
THIS SECTION IS DR. FORSYTH'S CODE. DO NOT MODIFY. BUT KEEP READING.
"""

# randomly sample a distribution between 2 and 6
random_number = int(random.uniform(2, 6))

# any number times 2 is even
an_odd_number = 2 * random_number

# generate a random list of odd length containing values up to 100
even_list = random.sample(range(100), an_odd_number)

# print out the list contents
print("Your list is: ", even_list)

"""
YOUR CODE BEGINS BELOW HERE. FILL IN THE MISSING OPERATIONS / CODE
"""

# find the length of the list
length = len(even_list)
print("The length of the list is " + str(length))

# find the middle number
first_middle = length//2
print("The first middle number is " + str(first_middle))

# find the middle number + 1
second_middle = first_middle - 1
print("The second middle number is " + str(second_middle))

# finding the numbers in the list and giving them names
first = even_list[first_middle]
second = even_list[second_middle]

# Adding the two middle numbers from the list up
# Dividing them by 2 to find the median
middle_average = (first + second)/2

# the average of middle elements is
print("The average of the middle numbers are: " + str(middle_average))
