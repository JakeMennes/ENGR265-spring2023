# The second type of loop is known as a while loop!
# The easy way to think of these is while some condition
# is true, keep running. Let's take a look:

iterations = 1

while iterations <= 5:
    # print("This has looped " + str(iterations) + " times.")
    iterations += 1

# Notice how after iterations got above 5 it stopped?
# That is because the while loop's condition was no
# longer true.

# In addition to having some condition in the creation
# of the loop, you can have a condition inside the loop
# to break out if need be.

# Comment out the above print statement and uncomment the next two.

exponential_growth = 1

while True:
    exponential_growth *= 2
    if exponential_growth > 200:
        print(str(exponential_growth) + " is too Big!!! Stopping!!!")
        break
    print(exponential_growth)

end_line = -1

# One thing to note: if a while loop is poorly defined it can
# easily become infinite and run forever. If this ever happens,
# press the red button in the terminal, or close PyCharm.
