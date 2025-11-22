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

if __name__ == "__main__":
    nums = [10, 9, 8]
    sorted_nums = selection_sort(nums)
    # print(sorted_nums)