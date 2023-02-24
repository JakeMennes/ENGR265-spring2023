# make a simple function to test for even or odd
def is_even(num):
    if num % 2 == 0:
        return True
    else:
        return False


# make a helper function to calculate the average of some list
def average(nums):
    total = 0
    for n in nums:
        total += n

    return total / len(nums)


if __name__ == "__main__":

    # create a new list of integers
    new_list = [2, 3, 4, 5, 6]

    # calculate the average
    avg = average(new_list)
    print("Average is: ", avg)

    # determine if even or odd and sum the result
    sum = 0
    for n in new_list:
        sum += n
        if is_even(n):
            print(n, " is even")
        else:
            print(n, " is odd")
