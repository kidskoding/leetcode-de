def move_zeroes(nums):
    i = 0
    while i < len(nums):
        if nums[i] == 0:
            nums.append(nums[i])
            del nums[i]
        else:          
            i += 1