# What if you want to perform a certain action in a loop
# when a condition is met? That's what "continue" and
# "break" are for!

# Let's create a loop that will walk through a list and
# stop everything if it finds a 4!

list_one = [12, 13, 5, 7, 4, 28, 42, 67]

for number in list_one:
    print(number)
    if number == 4:
        print("Found a 4, stopping.")
        break

# Notice how as soon as the 4 was found, the loop stopped?
# What if we wanted the loop to notice something, but keep going?
# That's where the "continue" keyword comes in.

# Just like tha last example, comment out the above print statements
# and uncomment the next one.

num_one = 1
for iteration in range(10):
    num_one *= 2
    if num_one > 24:
        # print(str(num_one) + " is greater than 24!")
        continue

# You can also use continue and break in the same loop!
# Continue statements in this instance aren't necessarily
# needed, but can help to remind you what will happen!

# Now, comment out the above print statements
# and uncomment the next few.

list_two = [3, 8, 13, 18, 23, 28]
num_two = 2

for items in list_two:
    new_num = items + num_two
    if new_num > 20:
        # print(str(new_num) + " is too big, stopping.")
        break
    elif new_num > 10:
        # print(str(new_num) + " is greater than 10!")
        continue
    else:
        # print(str(new_num) + " is pretty small.")
        continue

end_line = -1
