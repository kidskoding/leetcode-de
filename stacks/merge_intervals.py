def merge_intervals(intervals):
    # return an empty array ([]) if there are no intervals available
    if not intervals:
        return []
    
    # sort the intervals by the first value in each array in ascending order
    intervals.sort(key=lambda x: x[0])
    
    # initialize the merged intervals list with the first interval
    merged = [intervals[0]]
    
    for curr_interval in intervals[1:]:
        # get the last interval added to the result list
        last_merged = merged[-1]
        
        # check if the current interval starts before the last interval's end
        if curr_interval[0] <= last_merged[1]:
            # modify the merged result list directly
            last_merged[1] = max(last_merged[1], curr_interval[1])
        else:
            # no overlap just add it to the list
            merged.append(curr_interval)
            
    return merged
