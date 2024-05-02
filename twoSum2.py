numbers = [5,25,75]
target = 100

l, r = 0, len(numbers) - 1

while l < r:
    currSum = numbers[l] + numbers[r]

    if currSum > target:
        r -= 1
    elif currSum < target:
        l += 1
    else:
        print( [l+1, r+1])
 