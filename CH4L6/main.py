def merge_sort(nums):
    length = len(nums)
    if length < 2:
        return nums
    mid = length // 2
    first_half, second_half = nums[:mid], nums[mid:]
    sorted_left_side = merge_sort(first_half)
    sorted_right_side = merge_sort(second_half)
    return merge(sorted_left_side, sorted_right_side)


def merge(first, second):
    final = []
    while first != [] and second != []:  # while both are NOT empty
        if first[0] <= second[0]:  # compare first elements
            # remove first element of "first" and append it to "final"
            final.append(first.pop(0))
        else:
            # remove first element of "second" append it to "final"
            final.append(second.pop(0))
    if first != []:  # when either "first" or "second" becomes empty, add the other to the end of "final"
        final += first
    else:
        final += second
    return final


# note
if __name__ == "__main__":
    lst = [3, 2, 1]
    sorted_list = merge_sort(lst)
    print(sorted_list)
