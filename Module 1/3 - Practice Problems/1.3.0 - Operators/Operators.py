# # Math Module Here # #

# how well do you know your operators?
# you can add each variable into the print function below
# to check you work, like so:
# print(first_number)

# multiply two factors of 64
first_number = 8 * 8
print("First Number = " + str(first_number))

# divide first_number by 10
second_number = first_number / 10
print("Second Number = " + str(second_number))

# add second_number to first_number, then subtract 2
third_number = ((first_number + second_number) - 2)
print("Third Number = " + str(third_number))

# now, using parentheses, divide second_number by 2, then multiply it by 20, and finally add 2.4
fourth_number = (((second_number / 2) * 20) + 2.4)
print("Forth Number = " + str(fourth_number))

# think of two different ways to raise 8 to the 2nd power
# hint, for one of them you have to import a module discussed in class
# import math here
import math

squared_number_one = math.pow(8, 2)
print("8 squared is: " + str(squared_number_one))

squared_number_two = (8 ** 2)
print("8 squared is: " + str(squared_number_two))

