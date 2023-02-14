# make a simple function to test for even or odd
def is_even(num):
    """
    Test whether a value is an even
    :param num: A value
    :return: True is the value is even, otherwise False
    """
    if num % 2 == 0:
        return True
    else:
        return False


# make a helper function to calculate the average of some list
def average(nums):
    """
    Calculate the average value for a list of numbers
    :param nums: A list of numbers
    :return: The average value
    """
    total = 0
    for n in nums:
        total += n

    return total / len(nums)


# create a new list of integers
new_list = [2, 3, 4, 5, 6]

# calculate the average
avg = average(new_list)
print("Average is: ", avg)

# determine if even or odd
for n in new_list:
    if is_even(n):
        print(n, " is even")
    else:
        print(n, " is odd")
