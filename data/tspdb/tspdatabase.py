import fileutils

# importing the requests library
import requests


class Attraction:
    def __init__(self):
        self.id = -1

    def __init__(self, _name: str, _id: int):
        self.name = _name
        self.id = _id


class TSPDatabase:
    attractions = list()
    distancesDict = dict()

    # api-endpoint
    _attractionsURL = "http://34.68.99.74/disney_api/alpha/get_att"
    _waitTimeURL = "http://34.68.99.74/disney_api/alpha/get_wait"
    _operatingHoursURL = "http://34.68.99.74/disney_api/alpha/get_hours"

    # load a list of attractions from a JSON file specified as a string with an absolute path
    def load_attractions_from_file(self, filename: str):
        data = fileutils.loadWithJSON(filename)

        for item in data:
            var = Attraction(item['name'], item['id'])
            TSPDatabase.attractions.append(var)

    # return a list of attractions
    def get_attractions_list(self):
        return TSPDatabase.attractions

    # load distances from a JSON file specified as a string with an absolute path
    def load_distances_from_file(self, filename: str):
        data = fileutils.loadWithJSON(filename)
        TSPDatabase.distancesDict = data

    # get the distance in meters between two attractions, each specified by their attraction ID (int)
    def get_attraction_distance(self, id1: int, id2: int):
        key_ij = str(id1) + "," + str(id2)
        key_ji = str(id2) + "," + str(id1)

        # FIX: some distances are zero or not symetric
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

    # get the wait time (minutes) for an attraction ID (int) on a given date (string formated as YYYY-MM-DD)
    def get_wait_time(self, date: str, id: int):
        PARAMS = {"att": id, "date": date}

        # TODO: check to see if reqest is valid and return a null/error response
        # TODO: remove this HTTP request and make it a call to a local file
        r = requests.get(url=self._waitTimeURL, params=PARAMS)

        data = r.json()

        return data['average wait']

    # get the park's open hours
    def get_open_hours_by_date(self, date: str):
        PARAMS = {"date": date}

        # TODO: check to see if reqest is valid and return a null/error response
        # TODO: remove this HTTP request and make it a call to a local file
        r = requests.get(url=self._operatingHoursURL, params=PARAMS)

        data = r.json()

        # TODO: Fix situation where total hours may be negative if open past midnight
        return data['total hours']


if __name__ == "__main__":
    import os

    print("Database for Traveling Salesman Problem.\nWill now attempt to self-build....")

    db = TSPDatabase()

    filePath = os.path.abspath(__file__)

    splits = os.path.split(filePath)

    attractionsPath = splits[0] + os.sep + "attractions.json"

    distancesPath = splits[0] + os.sep + "distances.json"

    db.load_attractions_from_file(attractionsPath)

    db.load_distances_from_file(distancesPath)

    print("Database built!")
