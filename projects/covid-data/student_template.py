class CovidRecord:
    """
    A simple class to hold record data from NYT database
    """

    def __init__(self, _date='', _county='', _state='', _fips=0, _cases=0, _death=0):
        """
        Default constructor for transforming each line of the file into data point

        :param _date: Date covid case was recorded
        :param _county: County in which data was recorded
        :param _state: State in which data was recorded
        :param _fips: Federal Information Processing Standards code
        :param _cases: Number of total cases recorded
        :param _death: Number of total deaths recorded
        """
        self.date = _date
        self.county = _county
        self.state = _state

        if _fips == '':
            self.fips = 0
        else:
            self.fips = int(_fips)
        self.cases = int(_cases)

        if _death == '':
            self.death = 0
        else:
            self.death = int(_death)


def parse_nyt_data(file_path=''):
    """
    Parse the NYT covid database and return a list of points
    :param file_path: Path to data file
    :return: List of CovidRecord points
    """
    # data point list
    covid_data = list()

    # open the NYT file path
    fin = open(file_path)

    # get rid of the headers
    fin.readline()

    done = False

    while not done:
        line = fin.readline()

        if line == '':
            done = True
            continue

        elements = line.strip().split(",")

        new_point = CovidRecord((elements[0]), (elements[1]), (elements[2]),
                                (elements[3]), (elements[4]), (elements[5]))

        # to reduce file sizes, only grab Virginia points
        if new_point.state == 'Virginia':
            covid_data.append(new_point)

    return covid_data

h_cases = 0
r_cases = 0

if __name__ == "__main__":
    # load covid data as list of CovidRecord objects
    data = parse_nyt_data('us-counties.csv')
    # write code to address the following question:
    # When was the first positive COVID case in Rockingham County? When was the first in Harrisonburg?
    for point in data:
        if point.county == "Harrisonburg city" and point.cases >= h_cases:
            num = point.cases
            date = point.date
            break
    for point in data:
        if point.county == "Rockingham" and point.cases >= r_cases:
            r_num = point.cases
            r_date = point.date
            break
print("The first case in Harrisonburg was on: " + str(date) + " with " + str(num) + " case!!")
print("The first case in Rockingham was on: " + str(r_date) + " with " + str(r_num) + " case!!")

old_cases = 0
curr_case = 0
curr_date = ""
if __name__ == "__main__":
    # load covid data as list of CovidRecord objects
    data = parse_nyt_data('us-counties.csv')
    # write code to address the following question:
    # What day was the greatest number of new daily cases recorded in Harrisonburg? When was the greatest day in Rockingham County?
    for point in data:
        if point.county == "Harrisonburg city":
            great = point.cases - old_cases
            old_cases = point.cases
            if curr_case < great:
                curr_date = point.date
                curr_case = great
        continue
    print("The greatest number of daily cases in Harrisonburg was on " + str(curr_date) + " with " + str(curr_case) + " total cases!!")

old_cases = 0
curr_case = 0
curr_date = ""
if __name__ == "__main__":
    # load covid data as list of CovidRecord objects
    data = parse_nyt_data('us-counties.csv')
    # write code to address the following question:
    # What day was the greatest number of new daily cases recorded in Harrisonburg? When was the greatest day in Rockingham County?
    for point in data:
        if point.county == "Rockingham":
            great = point.cases - old_cases
            old_cases = point.cases
            if curr_case < great:
                curr_date = point.date
                curr_case = great
        continue
    print("The greatest number of daily cases in Rockingham was on " + str(curr_date) + " with " + str(curr_case) + " total cases!!")



