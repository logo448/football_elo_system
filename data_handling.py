# Logan Stenzel
import csv


def get_elo_ratings(a, b):
    a_score, b_score = 0, 0
    with open("elo_scores.csv", "rb") as csvfile:
        reader = csv.reader(csvfile, dialect='excel')
        for row in reader:
            if row[0] == a or row[0] == b:
                if row[0] == a:
                    a_score = row[1]
                else:
                    b_score = row[1]
    return a_score, b_score


def write_elo_ratings(a, b, a_score, b_score):
    tmp_data = []
    with open("elo_scores.csv", "rb") as csvfile:
        reader = csv.reader(csvfile, dialect='excel')
        for row in reader:
            tmp_data.append(row)

    team_counter = 0
    for team in tmp_data:
        if team[0] == a or team[0] == b:
            print team[0]
            if team[0] == a:
                tmp_data[team_counter][1] = a_score
            elif team[0] == b:
                tmp_data[team_counter][1] = b_score
        team_counter += 1

    with open("elo_scores.csv", "wb") as csvfile:
        writer = csv.writer(csvfile, dialect='excel')
        writer.writerows(tmp_data)