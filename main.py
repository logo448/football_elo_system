# Logan Stenzel
# NFL Elo rating system main file
# the a and b variables represent team a and team b in the code
import math

_k = 20


def win_probability(a, b):
    return 1.0/(10**(-(a-b)/400.0)+1)


def margin_victory_multiplier(win, lose, pd):
    return (math.log(abs(pd)+1)) * (2.2/((win-lose)*.001+2.2))


def new_elo(a, b, a_win_bool, pd):
    if a_win_bool == 1:
        win = a
        lose = b
        change = _k*margin_victory_multiplier(win, lose, pd)
        return a + change, b + (1-change)
    else:
        win = b
        lose = a
        change = _k*margin_victory_multiplier(win, lose, pd)
        return a + (1-change), b + change