def insertion_sort(nums):
    for i in range (1, len(nums)):
        j = i
        while j > 0 and nums[j-1] > nums[j]:
            nums[j-1], nums[j] = nums[j], nums[j-1]
            j -= 1
    return nums

def insertion_sort(nums):
    count = 0
    for j in range (1, len(nums)):
        while j > 0 and nums[j-1] > nums[j]:
            nums[j-1], nums[j] = nums[j], nums[j-1]
            j -= 1
            count += 1
    return nums, count

if __name__ == "__main__":
    nums = [0, -2, -5, 3, 2, 1]
    result, iter = insertion_sort(nums)
    print(iter)
    print(result)