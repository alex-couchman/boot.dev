import math


def get_influencer_score(num_followers, average_engagement_percentage):
    influencer_score = average_engagement_percentage * math.log(num_followers, 2)
    return influencer_score
