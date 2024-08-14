def binarySearch(low, high):
    while low <= high:
        mid = (low + high) // 2

        if isCorrect(mid) > 0:
            high = mid - 1
        elif isCorrect(mid) < 0:
            low = mid + 1
        else:
            return mid
    return -1
        

def isCorrect(n):
    if n > 10:
        return 1
    elif n < 10:
        return -1
    else:
        return 0
    
