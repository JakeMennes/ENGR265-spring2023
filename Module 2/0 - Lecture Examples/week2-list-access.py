# create a new list of integers
new_list = [2, 3, 4, 5, 6]

# what is the first element?
head = new_list[0]

# what is the last element?
tail = new_list[-1]

# inefficient, old-style to access last element
tail = new_list[len(new_list)-1]

# do not iterate in this style...
for i in range(0,len(new_list)):
    print(new_list[i])

# do it this way...
for element in new_list:
    print(element)



