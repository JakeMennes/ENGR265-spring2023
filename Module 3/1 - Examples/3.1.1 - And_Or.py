# Multiple conditions can be used in one if statement@
# The most common ways to do this are through the use
# of the AND and OR operators.

# Say for example I want two conditions to be met for
# an operation to execute. Here is an example:

temperature = 70
elevation = 1000
if temperature > 60 and elevation < 2000:
    print("Nice place to be!")

# Note that the statement printed. However, if one
# of the conditions isn't met, the statement won't print.

if temperature > 80 and elevation < 750:
    print("Where am I?")

# If you only need one condition to be satisfied,
# an or statement can be used.

fish_color = "Blue"
fish_size = "Large"
if fish_color == "Blue" or fish_size == "Small":
    print("This is an acceptable fish.")

# With this statement, both conditions have to be false to
# not work. True and False can also be used as inputs.

# Let's check out a situation where multiple comparison operators are used:
if (fish_size == "Large" or fish_size == "Small") and fish_color == "Blue":
    print("This is a blue fish!")

# Note that for the multiple comparison to work, the OR statement was in parentheses!
