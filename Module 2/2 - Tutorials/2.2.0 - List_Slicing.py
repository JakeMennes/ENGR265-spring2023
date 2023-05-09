# This is some practice on slicing arrays in Python.
# It will rely on the use of a colon, and the indexes of the list.

list_one = [5, 10, 15, 20, 25, 30]

# For the first task, copy list_one into List_one_copy
# Remember, to access elements in a list, use brackets
# at the end of the list's name: list_one[!!here!!]
list_one_copy = list_one

# Now use a print statement to check your work!
print(list_one_copy)

# Now, select all numbers greater than 10 from list_one!
over_10 = list_one_copy[2:]

# Now use a print statement to check your work!
print(over_10)

# Next, store all the numbers less than 20 in under_20.
# Recall that when using a colon, the number on the right when
# called is not included in the slice.
under_20 = list_one[0:3]

# Now use a print statement to check your work!
print("Numbers in the list Under " +str(under_20))

# For the last task, here is a list of names:
names_list = ["Frank", "Sally", "Grant", "Amelia", "Ricardo", "Rachelle"]

# Select the 2nd through the 4th names in names_list
median_names = names_list[1:4]

# Now use a print statement to check your work!
print("The Meadians of the list are " + str(median_names))