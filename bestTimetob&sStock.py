prices = [10, 1, 5, 6, 7, 1]

def bestBnSTime(nums):
    
    currMin = nums[0]
    res = 0

    for price in prices:
        if price < currMin:
            currMin = price
        res = max(res, price - currMin)

    return res

print(bestBnSTime(prices))
        