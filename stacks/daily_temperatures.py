def daily_temperatures(temperatures):
    # initialize the result with 0s
    answer = [0] * len(temperatures) 
    
    # create a stack to store the indicies for the days a warmer day has not been found yet
    stack = []
    
    # loop through the entire array
    for current_day, current_temp in enumerate(temperatures):
        # check if the daily temperature is greater than the temperature of the index at the top of the stack
        while stack and current_temp > temperatures[stack[-1]]:
            # pop this index from the stack since we already found the days since the warmest temperature
            past_day = stack.pop()
            
            # calculate the wait time for that past day
            answer[past_day] = current_day - past_day
        
        # push today onto the stack
        stack.append(current_day)
    
    # return the final answer array
    return answer
        