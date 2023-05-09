import json
import os


class Attraction:
    def __init__(self):
        self.id = -1

    def __init__(self, _name: str, _id: int):
        self.name = _name
        self.id = _id


class TSPDatabase:

    attractions = list()
    distancesDict = dict()

    def __init__(self):
        filePath = os.path.abspath(__file__)

        splits = os.path.split(filePath)

        attractionsPath = splits[0] + os.sep + "attractions.json"

        distancesPath = splits[0] + os.sep + "distances.json"

        self.load_attractions_from_file(attractionsPath)

        self.load_distances_from_file(distancesPath)

    # load a list of attractions from a JSON file specified as a string with an absolute path
    def load_attractions_from_file(self, filename: str):
        file = open(filename, "r")
        data = json.load(file)
        file.close()

        for item in data:
            var = Attraction(item['name'], item['id'])
            TSPDatabase.attractions.append(var)

    # return a list of attractions
    def get_attractions_list(self):
        return TSPDatabase.attractions

    # load distances from a JSON file specified as a string with an absolute path
    def load_distances_from_file(self, filename: str):
        file = open(filename, "r")
        data = json.load(file)
        file.close()
        TSPDatabase.distancesDict = data

    # get the distance in meters between two attractions, each specified by their attraction ID (int)
    def get_attraction_distance(self, id1: int, id2: int):
        key_ij = str(id1) + "," + str(id2)
        key_ji = str(id2) + "," + str(id1)

        # FIX: some distances are zero or not symmetric
        # compute both and report the max or a minimum of 30 feet
        distance_ij = TSPDatabase.distancesDict[key_ij]
        distance_ji = TSPDatabase.distancesDict[key_ji]

        return max(distance_ij, distance_ji, 30)

    # return the name of an attraction as a string when specified by an attraction ID (int)
    def get_attraction_name(self, id: int):
        return self.get_attraction_by_id(id).name

    # return an Attraction object for a provided attraction ID (int)
    def get_attraction_by_id(self, id: int):
        for attr in TSPDatabase.attractions:
            if attr.id == id:
                return attr
        return None
