myArray = [0,1,2,3,4]

def removeEnd(arr, lenght):
    if lenght > 0:
        arr[lenght -1] = 0
    return arr

def removeMiddle(arr, i, lenght):
    for index in range(i+1, lenght):
        arr[index -1] = arr[index]
    return arr

def insertEnd(arr, n, length, capacity):
    if length < capacity:
        arr[length] = n
    return arr

def insertMiddle(arr, i, n):
    l = len(arr)
    arr.append(None)
    for index in range(l - 1, i - 1, -1):
        arr[index + 1] = arr[index]
    
    arr[i] = n
    return arr