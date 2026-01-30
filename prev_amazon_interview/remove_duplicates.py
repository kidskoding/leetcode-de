def remove_duplicates(nums):
    duplicates = set()
    result = []
    
    for x in nums:
        if x in duplicates:
            continue
        
        duplicates.add(x)
        result.append(x)
        
    return result