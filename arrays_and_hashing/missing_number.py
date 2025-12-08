def find_missing_number(lst):
    expected_sum = len(lst) * (len(lst) + 1) // 2
    actual_sum = sum(lst)
    
    return expected_sum - actual_sum

def find_missing_number_v2(nums):
    nums.sort()
    
    for i, num in enumerate(nums):
        if num != i:
            return i
        
    return len(nums)