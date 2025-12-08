def coupon_pair(prices, budget):
    if prices == []:
        return []    

    price_to_index = {}
    
    for i, x in enumerate(prices):
        complement = budget - x
        
        if complement in price_to_index:
            return [price_to_index[complement], i]
        
        price_to_index[x] = i
        
    return []