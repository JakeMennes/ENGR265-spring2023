# Let's learn what a For Loop is!

# Lists are typically used to do certain operations
# over and over again. For the first example, we will
# go through a list and print out each number.

# The syntax for loops is like so: for "some variable" in
# "some range or container": do something.

list_one = [1, 2, 3, 4, 5]

for number in list_one:
    dummy = -1
    print(number)

# Notice how each number was printed in a new line? That shows
# that the operation happens once every "cycle" the program runs.

# Before your next run, comment out the above print statement, and
# uncomment the print statement below, that way the outputs make sense.

# This next loop shows how a range of numbers can be used for how many
# times a loop is run. In the bottom example, the loop will run 5 times.

for iteration in range(5):
    dummy = -1
    # print(iteration)

# Another common application for a for loop is to use the length of a list
# as the amount of times the loop runs. Same as before, comment out the
# previous print statement and uncomment the next print statement.

list_two = [5, 10, 15, 20, 25, 30]
list_two_looped = []

for number in range(len(list_two)):
    list_two_looped.append(list_two[number] - 5)
    # print(list_two_looped)

# As you can see, the "number" variable was used to represent the index of
# list_two, to be added to the previously empty list_two_looped! Notice how
# each print adds one more item to the new list.
