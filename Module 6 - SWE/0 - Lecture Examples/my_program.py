from os.path import exists

# check to see if we can see "train_data.txt" via relative path
relative_path = "train_data.txt"
if exists(relative_path):
    print("Can see train_data!")
else:
    print("Cannot locate train_data at path: ", relative_path)

# check if we can see "test_data.txt" via relative path option #1
relative_path = "subfolder/test_data.txt"
if exists(relative_path):
    print("Can see test_data!")
else:
    print("Cannot locate test_data at path: ", relative_path)

# check if we can see "test_data.txt" via relative path option #2
relative_path = "./subfolder/test_data.txt"
if exists(relative_path):
    print("Can see test_data!")
else:
    print("Cannot locate test_data at path: ", relative_path)

# check an absolute path based upon Windows notation
absolute_path = r"C:\Users\Jason Work\Documents\GitHub\ENGR298-2022-Private\lecture-examples\week8-file-paths\train_data.txt"
if exists(absolute_path):
    print("Can see train_data!")
else:
    print("Cannot locate train_data at path: ", absolute_path)

