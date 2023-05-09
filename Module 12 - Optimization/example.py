from tspdb import TSPDatabase

db = TSPDatabase()

# print out all attractions
for attr in db.get_attractions_list():
    print(str(attr.id) + " " + attr.name)

print("Attempting to find the distance between " + db.get_attraction_name(4) + " and " + db.get_attraction_name(16))

distance = db.get_attraction_distance(4, 16)

print("Distance is " + str(distance) + " meters")
