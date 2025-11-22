def exponential_growth(n, factor, days):
    followers = [n]
    day = 0
    while day < days:
        followers.append(followers[-1] * (factor))
        day += 1
    return followers
