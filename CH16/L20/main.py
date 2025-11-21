def subset_sum(nums, target):
    result = find_subset_sum(nums, target, len(nums) - 1)
    return result


def find_subset_sum(nums, target, index):
    if target == 0:
        return True
    if index < 0 and target != 0:
        return False
    if nums[index] > target:
        return find_subset_sum(nums, target, index - 1)
    else:
        result1 = find_subset_sum(nums, target, index - 1)
    new_target = target - nums[index]
    
    result2 = find_subset_sum(nums, new_target, index - 1)
    if result1 or result2:
        return True
    else:
        return False

if __name__ == "__main__":
    nums = [1, 2, 3, 8, 9, 10]
    target = 12
    print(subset_sum(nums, target))
