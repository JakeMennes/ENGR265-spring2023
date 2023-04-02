import os


class EKGAnnotation:

    def __init__(self, _time, _sample, _annotation, _ch, _num, _db_extra, _rhythm_annotation=''):
        self.time = self.__convert_to_seconds__(_time)
        self.sample = int(_sample)
        self.annotation = _annotation
        self.channel = int(_ch)
        self.number = int(_num)
        self.extra = _db_extra
        self.rhythm_annotation = _rhythm_annotation

        return

    def __convert_to_seconds__(self, time):
        # find all the colons
        elements = time.split(":")

        # convert into seconds
        if len(elements) == 2:
            minutes = float(elements[0]) * 60
            seconds = float(elements[1])

            return minutes * 60 + seconds

        # default handler
        return time


class EKGTestBench:

    def __init__(self, filepath):

        file_exists = os.path.exists(filepath)

        # check file file path is good
        if file_exists is False:
            print("Path to file is invalid: ", filepath, ". File does no exist.")
            return None

        # store the path to file
        self.file_path = filepath

        # store annotations list
        self.annotations = list()

        # store annotation indices as this is useful
        self.annotation_indices = list()

        # open path to annotation file
        file = open(filepath)

        # parse each line individually
        for line in file:
            line = line.replace("\t", " ")
            elements = line.rstrip().split(" ")

            values = list()
            for e in elements:
                if e == '':
                    continue
                else:
                    values.append(e)

            # check to see if an optional rhythm is present
            rhythm = ''
            if len(values) == 7:
                rhythm = values[6]

            # create an annotation object
            ann = EKGAnnotation(values[0], values[1], values[2], values[3], values[4], values[5], rhythm)

            # store object in own list and indices in another
            self.annotations.append(ann)
            self.annotation_indices.append(ann.sample)

        file.close()

    def generate_stats(self, detector_responses):

        # double check that responses are sorted; do not assume
        detector_responses.sort()

        # acceptable solutions are within 5% of the annotation
        delta = 90

        # pair of responses and annotations that have been acceptable matched
        matched = list()

        # responses that were unmatched to an annotation
        unmatched = list()

        # create copy of annotations list so we can modify
        annotations = self.annotations.copy()

        # go through the response list
        for r in detector_responses:
            annotation_to_be_removed = None

            # for this response, search through annotations for a match within delta
            for a in annotations:

                # this is matched positive event
                if abs(r - a.sample) < delta:
                    annotation_to_be_removed = a
                    matched.append((r, a.sample))
                    break

                # event is unmatched in list, stop scanning
                if a.sample > r + delta:
                    unmatched.append(r)
                    break

            if annotation_to_be_removed is not None:
                annotations.remove(annotation_to_be_removed)

        return matched, unmatched, annotations
