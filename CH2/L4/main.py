def get_follower_prediction(follower_count, influencer_type, num_months):
    dict = {
        "fitness": 4,
        "cosmetic": 3
    }

    base = 2

    if dict.get(influencer_type) != None:
        base = dict[influencer_type]
    total = follower_count * (base ** num_months)
    return total
