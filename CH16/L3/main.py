def tsp(cities, paths, dist):
    perms = permutations(cities)
    for perm in perms:
        sum = 0
        for i in range(len(perm) - 1):
            curr_city, next_city = perm[i], perm[i+1]
            sum += paths[curr_city][next_city]
        if sum < dist:
            return True
    return False


# don't touch below this line


def permutations(arr):
    res = []
    res = helper(res, arr, len(arr))
    return res


def helper(res, arr, n):
    if n == 1:
        tmp = arr.copy()
        res.append(tmp)
    else:
        for i in range(n):
            res = helper(res, arr, n - 1)
            if n % 2 == 1:
                arr[n - 1], arr[i] = arr[i], arr[n - 1]
            else:
                arr[0], arr[n - 1] = arr[n - 1], arr[0]
    return res
