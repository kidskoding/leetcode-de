def max_area(height):
    # create a left pointer to store the leftmost element
    left = 0
    
    # create a right pointer to store the rightmost element
    right = len(height) - 1
    
    # create a variable to store the maximum possible area
    max_area = 0
    
    while left < right:
        # the width is the difference between right and left
        # the height is the minimum of height[left] and height[right]
        area = (right - left) * min(height[left], height[right])
        
        # compare max_area and area and pick the greater one to get the max area
        max_area = max(max_area, area)
        
        # remove the shorter line because a greater height indicates a greater area
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1
        
    return max_area
