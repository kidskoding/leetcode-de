def group_anagrams(words):
    if not words:
        return []
    
    grouped_anagrams = {}
    
    for x in words:
        sorted_key = ''.join(sorted(x))
        
        if sorted(x) not in group_anagrams:
            grouped_anagrams[sorted_key] = []
            
        grouped_anagrams[sorted_key].append(x)
            
    return list(group_anagrams.values())