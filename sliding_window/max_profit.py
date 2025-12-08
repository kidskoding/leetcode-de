def max_profit(prices):
    # create a variable to store the maximum profit that can be obtained
    max_profit = 0
    
    # create a variable to store the beginning of the sliding window (buy)
    left = 0
    
    # create a variable to store the end of the window (sell)
    right = 1
    
    while right < len(prices):
        # A profit is achieved when prices[right] > prices[left]
        if prices[right] > prices[left]:
            # compute the max_profit by taking the max value from the current max_profit
            # and the overall profit prices[right] - prices[left]
            max_profit = max(max_profit, prices[right] - prices[left])
        else:
            # shift the buy pointer to the current lowest price
            left = right
            
        right += 1
        
    return max_profit