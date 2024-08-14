matrix = [[1, 2, 4, 8], 
          [10, 11, 12, 13], 
          [14, 20, 30, 40]]

target = 111

# def searchMatrixInit(matrix, target):
#     for i in matrix:
#         if i[0] == target:
#             return True
#         else:
#             for j in i:
#                 l, r = 0, len(i)-1
#                 mid = (l+r)//2
#                 if target > i[mid]:
#                     l = mid + 1
#                 elif target < i[mid]:
#                     r = mid - 1
#                 else:
#                     return True
#     return False


def searchMatrix(matrix, target):
    ROWS, COLS = len(matrix), len(matrix[0])

    top, bot = 0, ROWS - 1


    while top <= bot:
        row = (top + bot) // 2
        if target > matrix[row][-1]:
            top = row + 1
        elif target < matrix[row][0]:
            bot = row - 1
        else:
            break
    
    if not (top <= bot):
        return False
    
    l, r = 0, COLS - 1
    
    while l <= r:
        m = (l + r) // 2
        if target > matrix[row][m]:
            l = m + 1
        elif target < matrix[row][m]:
            r = m - 1
        else:
            return True
    return False

print(searchMatrix(matrix, target))