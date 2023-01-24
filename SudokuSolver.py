# board is a 9*9 matrix
def findEmpty (board):
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:
                return (row, col)
    return None
