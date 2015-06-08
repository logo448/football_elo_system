# Logan Stenzel
import csv


def get_elo_rating(a, b):
    a_score, b_score = 0, 0
    with open("elo_scores.csv", "rb") as csvfile:
        reader = csv.reader(csvfile, dialect='excel')
        for row in reader:
            print row[0]
            if row[0] == a or b:
                if row[0] == a:
                    a_score = row[1]
                else:
                    b_score = row[1]
    return a_score, b_score