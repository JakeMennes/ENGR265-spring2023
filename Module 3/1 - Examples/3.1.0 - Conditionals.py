# Let's dig into some conditional statements!

# If statements are used if you want code to execute
# only if some condition is met. Let's check one out:

number = 10
if number > 5:
    print("number is greater than 5.")

# Since number is greater than 5, the statement was printed.

# Some things to note: there was a colon at the end of the
# statement. This is needed for it to function. Also note that
# the print statement was indented. This shows that it "belongs"
# to the if statement.

# Else statements can be used to catch any operations that don't
# satisfy the if statement. Here's an example:

number_two = 25
if number_two == 30:
    print("number_two is equal to 30.")
else:
    print("number_two is not equal to 30.")

# Since number_two is not equal to 30, the second statement was
# printed. To show equality, two equals signs are used. Make note of this.

# Elif statements are secondary if statements that can work as a second check
# before an else statement executes. Let's check out an example

number_three = 75
if number_three == 100:
    print("number_three is equal to 100")
elif number_three >= 50:
    print("number_three is pretty big.")
else:
    print("number_three is too small.")

# number_three didn't satisfy the first condition, but it did satisfy
# the second condition, which is why the else statement wasn't printed.
