def get_avg_brand_followers(all_handles, brand_name):
    count = 0
    for list in all_handles:
        for user in list:
            if brand_name in user:
                count += 1
    return (count / len(all_handles))
