# Let's dive into making some lists!

# Here is how to create a list in Python:
# First Step is to pick a name, then we will set
# that variable equal to a bracket filled with numbers.
first_list = [1, 2, 3, 4]

# Note that the values are separated by commas, very important.
# Printing the list will show all of its contents:
print(first_list)

# If you're curious about the length of a list, or need it for
# some parameter, the len() function will be useful.
# Let's check out the length of first_list:
list_length = len(first_list)
print("The length of first_list is: " + str(list_length))

# Creating an empty list is also an option.
# Here are two ways to make empty lists:
empty_list = []
empty_list_two = list()

# Now let's get into some functions we can do with lists!
# The first one we will use is append. All this does is add an
# element to the end of a list. Let's see it!
first_list.append(5)
print(first_list)

# As you can see, the number 5 was added to the list.
# You can also add an element to a specific spot using insert.
first_list.insert(0, 0)
print(first_list)

# From this you can see that a 0 was added to the beginning of the list!
# The first value determines where, the second value determines what
# The next example will explain why a 0 was used for the first spot of the list
