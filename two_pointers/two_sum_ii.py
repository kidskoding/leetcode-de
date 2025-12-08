def two_sum_ii(numbers, target):
    # create two pointers at the start and end of the array
    left = 0
    right = len(numbers) - 1
    
    while left < right:
        # if numbers[left] + numbers[right] is greater than target, 
        # move right back 1 to get a sum closer to target
        if numbers[left] + numbers[right] > target:
            right -= 1
        
        # if numbers[left] + numbers[right] is less than target,
        # move left up 1 to get a sum closer to target
        elif numbers[left] + numbers[right] < target:
            left += 1
            
        # return the two indices as a list if they equal target
        else:
            return [left + 1, right + 1]
    
    # to make code safe return an empty [] if no indices sum to target
    return []