# In this assignment, you will be tasked with deciphering
# which outcome will occur within each If Else statement.

# Try and do this without any print statements as well!

# Case #1:

age_one = 22
age_two = 18

if age_one > 21 and age_two > 21:
    result = "Option One"
elif age_one > 18 and age_two > 18:
    result = "Option Two"
else:
    result = "Option Three"

# Write your expected outcome here as a string:
# It is case-sensitive, so make sure they are exactly the same!
case_one_answer = "Option Three"

# Case #2:

weather = "Clear"
temperature = 70

if weather == "Rainy" or temperature <= 60:
    weather_report = "It's gross out"
elif weather == "Clear" and 60 < temperature < 80:
    weather_report = "It's nice out"
elif weather == "Clear" and temperature >= 80:
    weather_report = "It's toasty out"
else:
    weather_report = "Unavailable"

# Write your expected answer here as a string:
case_two_answer = "It's nice out"
