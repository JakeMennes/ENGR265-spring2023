import os
import random

if __name__ == "__main__":

    # to open a file, first we need a file name
    file_name = "my_data.txt"

    # If you attempt to open a file and that file does not exists
    # an error will be returned. It is always good to check if the file
    # actually exists before opening it. We will use os.path() for this

    print("Does this file exist: ", file_name)
    if os.path.exists(file_name) == False:
        print("File does not exist! Error!")
    else:
        print("It does exist!")

    # Typically files are accessed with open(). If our file is new, we can create
    # it as we open the file by passing the 'w' parameter to open()
    my_new_file = open(file_name, 'w')

    # now that we have created the file. This code should not error.
    print("Attempting to open file: ", file_name)
    if os.path.exists(file_name) == False:
        print("File does not exist! Error!")
    else:
        print("It does exist!")

    # Having opened the file, we now have a 'handle' object through which we can read/write/modify the file
    # we will leave this file alone for now. So let's close it.
    my_new_file.close()

    # To practice writing to a file, let's create a file called 'hello_world.txt' and write the
    # string "Hello world!" in it.
    hello_world_file = open("hello_world.txt", 'w')

    # use the write method from the handle to write to the file
    string_to_be_written = "Hello world!"

    # given a string, write it out to the file
    hello_world_file.write(string_to_be_written)

    # now we're done writing, close the file
    hello_world_file.close()


    # when writing a CSV file it is important to follow ensure values are separated by commas
    # and that each new value is on a different line.

    # following from the examples above, the file should be opened
    my_csv = open('my_data.csv','w')

    # to enable the data to be easily parsed, write out the header row
    # Note: it is important to ensure a new line character '\n' is included at the end of this line

    # construct a silly string as headers for printing out a vector in 3-space <x,y,z>
    header_string = "x,y,z\n"

    # write header to file
    my_csv.write(header_string)

    # fill the remainder of the file with random x,y,z values for several lines
    num_lines_to_write = random.randint(5,10)

    # for each line, generate random ints and write to file
    for idx in range(0,num_lines_to_write):

        # generate three random integers
        x=random.randint(-100,100)
        y=random.randint(-100,100)
        z=random.randint(-100,100)

        # stitch those integers into a string to write
        # each integer must be manually converted to a string and
        # each element must be separated by a comma and end with a new line '\n'
        string_to_write = str(x)+","+str(y)+","+str(z)+'\n'

        # write the CSV line to the file
        my_csv.write(string_to_write)

    # after we're done, close the file
    my_csv.close()
