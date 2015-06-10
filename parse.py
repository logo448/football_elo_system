import csv


def get_file_contents(path):
    output = []
    with open(path, "rb") as csvfile:
        reader = csv.reader(csvfile, dialect='excel')
        for row in reader:
            output.append(row)
    return output