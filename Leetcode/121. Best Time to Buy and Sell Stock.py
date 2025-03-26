def maxProfit(prices):
    min_val = min(prices)
    min_idx = prices.index(min_val)
    
    max_val = 0

    for i in range(min_idx, len(prices)):
        if prices[i] > max_val:
            max_val = prices[i]
    
    max_profit = max_val - min_val if max_val > 0 else 0
    return max_profit

print(maxProfit([2,4,1]))