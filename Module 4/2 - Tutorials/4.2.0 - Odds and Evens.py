# For this tutorial, we will walk through how to find the odds and evens
# that are stored in a list, and count how many of each there are.

# Here are the two lists we will be working with:
list_one = [2, 23, 45, 64, 43, 3, 654, 57, 19, 38]
list_two = [1, -3, -64, 25, 70, 0, 74]

# Here are the counter variables for the evens and odds.
# In the For Loop, increase the appropriate one by one
# when an even or an odd is found!
one_evens = 0
one_odds = 0

odds_list = []
evens_list = []

# Hint: use if/else statements to set conditions in
# the For Loop to determine even or odd.

# Fill in this loop:
for element in list_one:
    if element % 2 == 1:
        odds_list.append(element)
        one_odds += 1
    elif element % 2 == 0:
        evens_list.append(element)
        one_evens += 1
    continue

# These statements can be used to check your work!
print("This is the even list: " + str(evens_list))
print("The number of evens in list_one is: " + str(one_evens))
print("This is the odd list: " + str(odds_list))
print("The number of odds in list_one is: " + str(one_odds))

# Here are the counters for list_two:
two_evens = 0
two_odds = 0

odds_2list = []
evens_2list = []

# Now you do the rest!
for element in list_two:
    if element % 2 == 1:
        odds_2list.append(element)
        two_odds += 1
    elif element % 2 == 0:
        evens_2list.append(element)
        two_evens += 1
    continue

# These statements can be used to check your work!

print("This is the even list: " + str(evens_2list))
print("The number of evens in list_one is: " + str(two_evens))

print("This is the odd list: " + str(odds_2list))
print("The number of odds in list_one is: " + str(two_odds))
















