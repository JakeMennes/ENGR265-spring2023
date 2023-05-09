from tspdb.tspdatabase import TSPDatabase

import os

db = TSPDatabase()

filePath = os.path.abspath(__file__)

splits = os.path.split(filePath)

attractionsPath = splits[0] + os.sep + "attractions.json"

distancesPath = splits[0] + os.sep + "distances.json"

db.load_attractions_from_file(attractionsPath)

db.load_distances_from_file(distancesPath)