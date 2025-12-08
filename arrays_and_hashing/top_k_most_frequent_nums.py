def top_k_frequent_nums(nums, k):
    # create a frequencies map storing the frequencies of each element
    frequencies = {}
    
    # go through each element in `nums`
    for x in nums:
        # update the frequency map based on the number of times x appears in nums
        frequencies[x] = frequencies.get(x, 0) + 1
        
    # sort the values of map in descending order by frequencies, 
    # where the highest frequency is the first key and so on
    sorted_values = sorted(frequencies.items(), key=lambda x: x[1], reverse=True)
    
    # return all the elements of the list up to k
    return [x[0] for x in sorted_values][:k]