# Find the first cell that is zero.
def findEmpty(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0:
                return (i, j) 
                # row, col
    return None

# Checking if the num is in the row or col or block.
def isValid(board, num, pos):
    row, col = pos
    # Checking the row:
    for i in range(len(board[0])):
        if board[row][i] == num and row != i:
            return False

    # Checking the col:
    for i in range(len(board)):
        if board[i][col] == num and col != i:
            return False
    
    # Checking the block:
    blockStart_x = 3 * (row // 3)
    blockStart_y = 3 * (col // 3)

    blockEnd_x = blockStart_x + 3
    blockEnd_y = blockStart_y + 3

    for i in range(blockStart_x, blockEnd_x):
        for j in range(blockStart_y, blockEnd_y):
            if board[i][j] == num and (row, col) != (i,j):
                return False
    return True 

def solve(board):
    blank = findEmpty(board)
    
    if not blank:
        return True
    else:
        row, col = blank
    
    for i in range(1,10):
        if isValid(board, i, blank):
            board[row][col] = i

            if solve(board):
                return True

            board[row][col] = 0
    
    return False

def printSudoku(board):
    for i in range(len(board)):
        if i % 3 == 0 and i != 0:
            print(".....................")

        for j in range(len(board[0])):
            if j % 3 == 0 and j != 0:
                print("|", end=" ")

            if j == len(board[0])-1:
                print(board[i][j])
            else:
                print(str(board[i][j]) + " ", end="")

# Test
# Initializing a test board, empty cells are initialized with 0.
# def setBoard():
#     board = list()
#     sudokuBoard = '''200080300
# 060070084
# 030500209
# 000105408
# 000000000
# 402706000
# 301007040
# 720040060
# 004010003'''
#     rows = sudokuBoard.split('\n')
#     for row in rows:
#         column = list()
#         for character in row:
#             digit = int(character)
#             column.append(digit)
#         board.append(column)
#     return board

# board = setBoard()
# solve(board)
# printSudoku(board)
