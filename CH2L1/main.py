import numpy as np


def get_estimated_spread(audiences_followers):
    if audiences_followers == []:
        return 0

    average_audience_followers = np.mean(audiences_followers)
    num_followers = len(audiences_followers)
    estimated_spread = average_audience_followers * (num_followers ** 1.2)
    print(type(audiences_followers[0]))
    print(type(average_audience_followers))
    print(type(estimated_spread))
    return estimated_spread
