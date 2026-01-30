def product_of_array_except_self(nums):
    # create the resulting list of 1s to build the prefix and suffix sums
    # 1 helps because it doesn't affect multiplication
    lst = [1] * len(nums)
    
    # build the prefix sum
    for i in range(1, len(nums)):
        lst[i] = lst[i - 1] * nums[i - 1]
        
    # build the suffix sum
    suffix = 1
    for i in range(len(nums) - 1, -1, -1):
        lst[i] *= suffix
        suffix *= nums[i]
    
    # return the resulting list    
    return lst
