# Unlike in real life where we start counting elements
# at 1, in coding lists start at 0. So the first element
# is element 0.

# Here is a list:
new_list = [2, 3, 4, 5, 6]

# Here is how to access the first element of a list:
head = new_list[0]
print("The first element of new_list is: " + str(head))

# The last element of a list can be found by going backwards!
# You can index backwards if you want, but it's not really necessary.
tail = new_list[-1]
print("The last element of new_list is: " + str(tail))

# Colons can also be used to pull multiple elements from a list.
# Let's check out a few ways colons can be used:

# Access the Whole list:
whole_list = new_list[:]
print("The whole list is: " + str(whole_list))

# Access from the 3rd element to the end.
# Remember the list starts at 0, so the 3rd element is in the
# second spot:
three_end = new_list[2:]
print("Elements from 3 to the end are: " + str(three_end))

# Access only the first 2 elements:
# Notice that even though the third element position is used,
# it doesn't show up in the new list.
first_two = new_list[:2]
print("The first two elements are: " + str(first_two))

# Access the 2nd through 4th element:
middle_list = new_list[1:4]
print("The middle values are: " + str(middle_list))
