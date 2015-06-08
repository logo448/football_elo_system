# Logan Stenzel
# NFL Elo rating system main file
# the a and b variables represent team a and team b in the code
import math


def win_probability(a, b):
    return 1.0/(10**(-(a-b)/400.0)+1)


def margin_victory_multiplier(win, lose, pd):
    return (math.log(abs(pd)+1)) * (2.2/((win-lose)*.001+2.2))
