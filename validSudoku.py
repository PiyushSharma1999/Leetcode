from collections import defaultdict

board = [["7",".",".",".","4",".",".",".","."],
         [".",".",".","8","6","5",".",".","."],
         [".","1",".","2",".",".",".",".","."],
         [".",".",".",".",".","9",".",".","."],
         [".",".",".",".","5",".","5",".","."],
         [".",".",".",".",".",".",".",".","."],
         [".",".",".",".",".",".","2",".","."],
         [".",".",".",".",".",".",".",".","."],
         [".",".",".",".",".",".",".",".","."]]

# board = [[".",".",".",".","5",".",".","1","."],
#          [".","4",".","3",".",".",".",".","."],
#          [".",".",".",".",".","3",".",".","1"],
#          ["8",".",".",".",".",".",".","2","."],
#          [".",".","2",".","7",".",".",".","."],
#          [".","1","5",".",".",".",".",".","."],
#          [".",".",".",".",".","2",".",".","."],
#          [".","2",".","9",".",".",".",".","."],
#          [".",".","4",".",".",".",".",".","."]]

# for row in board:
#     for index, n in enumerate(row):
#         if tuple([index, n]) not in h_map:
#             h_map[tuple([index, n])] = 1
#         else:
#             h_map[tuple([index, n])] += 1

# for k, v in h_map.items():
#     if k[1] != '.' and v > 1:
#         print(True)
#     else:
#         print(False)

def validSudoku(board):
    cols = defaultdict(set)
    rows = defaultdict(set)
    squares = defaultdict(set)

    for r in range(9):
        for c in range(9):
            if board[r][c] == ".":
                continue
            if (board[r][c] in rows[r] or
                board[r][c] in cols[c] or
                board[r][c] in squares[(r // 3, c // 3)]):
                return False
            cols[c].add(board[r][c])
            rows[r].add(board[r][c])
            squares[(r // 3, c // 3)].add(board[r][c])
    return True

print(validSudoku(board))