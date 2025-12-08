def longest_substring_length_without_repeating_characters(s):
    # create a hash set to store the unique characters
    char_set = set()
    
    left = 0
    
    # create a variable to store the max length of a unique substring
    max_len = 0
    
    for right in range(len(s)):
        # while s[right] is in the char set, remove the characters from the char_set
        while s[right] in char_set:
            char_set.remove(s[right])
            left += 1
            
        # add s[right] to the char_set
        char_set.add(s[right])        
            
        # calculate the size (the window length is right - left + 1)
        max_len = max(max_len, right - left + 1)
    
    # return the max length of the substring
    return max_len