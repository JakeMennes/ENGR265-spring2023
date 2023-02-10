"""
Given two lists, use the standard deviation function from numpy to determine
which language has the largest standard deviation. Usage will be np.std()
https://numpy.org/doc/stable/reference/generated/numpy.std.html
"""

"""
Dr. Forsyth's Code. Do Not Modify.
"""
# bring in randomness because we need it in our lives
import random
import numpy as np
import numpy

# randomly sample a distribution between 20 and 100
random_length = int(random.uniform(20, 100))

# generate a random list of random length containing values up to 100
random_list_A = random.sample(range(100), random_length)

# generate a random list of random length containing values up to 100
random_list_B = random.sample(range(100), random_length)

# use the std() method from numpy to determine which list has the largest standard deviation

### YOUR CODE HERE

# set this variable equal to the list with the largest standard deviation
# do not modify this variable's name, you can/should adjust the contents ;)
# e.g. longest_list_is = myList
#longest_list_is = myList
### YOUR CODE HERE

#import math function into interface

#Print both of the list so that you can the contents of the list
print("Print The Contents of Random List One" + str(random_list_A))
print("Print The Contents of Random List Two" + str(random_list_B))

#take the starndard deviation of both of the list
Standard_deviation_list_A = np.std(random_list_A)
Standard_deviation_list_B = np.std(random_list_B)

#Print the standard deviation of both of the list
print("The Standard Deviation of List A is: " + str(Standard_deviation_list_A))
print("The Standard Deviation of List B is: " + str(Standard_deviation_list_B))

#Find the greater standard deviation value
#Write a statement to see if A is larger than B
if Standard_deviation_list_A >= Standard_deviation_list_B:
    print("The Longest List is A")
    #Write a statement to see if B is bigger than A
else:
    print("The Longest List is B")






