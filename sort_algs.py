def bubble_sort(nums):
    swapping = True
    end = len(nums)
    while swapping:
        swapping = False
        for i in range(1, end):
            if nums[i-1] > nums[i]:
                nums[i-1], nums[i] = nums[i], nums[i-1]
                swapping = True
        end -= 1
    return nums

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

def insertion_sort(nums):
    for i in range (1, len(nums)):
        j = i
        while j > 0 and nums[j-1] > nums[j]:
            nums[j-1], nums[j] = nums[j], nums[j-1]
            j -= 1
    return nums

def quick_sort(nums, low, high):
    if low < high:
        middle = partition(nums, low, high)
        quick_sort(nums, low, middle-1) # left half
        quick_sort(nums, middle+1, high) # right half
        return nums

def partition(nums, low, high):
    pivot = nums[high]
    i = low - 1
    for j in range(low, high):
        if nums[j] < pivot:
            i += 1
            nums[i], nums[j] = nums[j], nums[i]
    nums[i+1], nums[high] = nums[high], nums[i+1]
    return i+1

def selection_sort(nums):
    n = len(nums)
    n_count = 0
    print(nums)
    for i in range(n):
        smallest_idx = i
        for j in range(i+1, n):
            if nums[j] < nums[smallest_idx]:
                smallest_idx = j
                n_count +=1
        nums[i], nums[smallest_idx] = nums[smallest_idx], nums[i]
        print(i, nums)
    print(n_count)
    return nums
