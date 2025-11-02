def find_minimum(nums):
    minimum = float("inf")
    if nums == []:
        return None
    else:
        for item in nums:
            if item < minimum:
                minimum = item
        return minimum
