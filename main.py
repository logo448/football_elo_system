# Logan Stenzel
# NFL Elo rating system main file
# the a and b variables represent team a and team b in the code


def win_probability(a, b):
    return 1.0/(10**(-(a-b)/400.0)+1)