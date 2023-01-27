# create a string
sentence = "This is a random string."

# iterate through string and print characters
for c in sentence:
    print(c)

# add some excitement to the sentence. Make a new sentence
# where final character is '!'
excited = sentence[0:-1]+'!'

# print out the new string
print(excited)

# break the sentence into its subwords
words = excited.split(" ")
for w in words:
    print(w)




