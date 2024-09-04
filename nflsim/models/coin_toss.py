from nflsim import teambase
import random


def model(home_team, away_team):
    rng = random.random()
    if rng > 0.5:
        return home_team
    else:
        return away_team
