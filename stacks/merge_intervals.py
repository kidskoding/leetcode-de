def merge_intervals(intervals):
    if not intervals:
        return []
    
    intervals = sorted(intervals, key=lambda x: x[0])
    result = [intervals[0]]
    
    for current in intervals[1:]:
        last_merged = result[-1]
        
        if current[0] <= last_merged[1]:
            last_merged[1] = max(last_merged[1], current[1])
        else:
            result.append(current)
            
    return result