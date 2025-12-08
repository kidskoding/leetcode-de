def valid_anagram(s, t):
    # create a frequency map to store the frequencies of s
    frequency = {}
    
    for x in s:
        # add the count of each character in s to the frequency map
        frequency[x] = frequency.get(x, 0) + 1
        
    for x in t:
        # if the character is not in the frequency, return false
        if x not in frequency:
            return False
        
        # get the frequency of a character and subtract its value by 1
        frequency[x] -= 1
        
        # if the frequency of a character becomes 0, remove it from the map
        if frequency[x] == 0:
            del frequency[x]
            
    # check if frequency's length is 0
    # If all characters have been removed from the map, then both characters must be anagrams
    return len(frequency) == 0