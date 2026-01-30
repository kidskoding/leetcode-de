def sort_array_with_odd_numbers(nums):
    nums.sort()
    return [x for x in nums if x % 2 == 1]