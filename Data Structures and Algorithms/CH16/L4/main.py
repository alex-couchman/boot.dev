def verify_tsp(paths, dist, actual_path):
    sum = 0
    for i in range(len(actual_path) - 1):
        curr_city, next_city = actual_path[i], actual_path[i+1]
        sum += paths[curr_city][next_city]
    if sum < dist:
        return True
    return False
