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

if __name__ == "__main__":
    nums = [9, 6, 2, 1, 8, 7]
    low = 0
    high = len(nums) - 1
    sorted_nums = quick_sort(nums, low, high)
    print(sorted_nums)