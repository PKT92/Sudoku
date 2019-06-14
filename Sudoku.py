import math

def checkRow(n, row):
    if n in row:
        print("Check row failed")
        return False
    else:
        return True

def checkCol(n, board, col):
    for i in board:
        if i[col] == n:
            print("Check col failed")
            return False
    return True

def checkSquare(n, board, col, row):
    rowMin = math.floor(row/3)*3
    colMin = math.floor(col/3)*3
    for i in range(rowMin, rowMin+3):
        for j in range(colMin, colMin+3):
            if board[i][j] == n:
                print("Check square failed")
                return False
    return True

def checkBoard(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] != "_":
                tmpVal = board[i][j]
                board[i][j] = '_'
                if not checkSquare(tmpVal, board, j, i) or not checkCol(tmpVal, board, j) or not checkRow(tmpVal, board[i]):
                    return False
                board[i][j] = tmpVal
    return True

path = 'test.txt'
inputFile = open(path, 'r')
test = [[] for i in range(9)]
for i in range(9):
    tmp = inputFile.readline().rstrip()
    for j in range(9):
        test[i].append(tmp[j])
validBoard = True
print(*test, sep='\n')
if checkBoard(test):
    print("Valid Board")
else:
    print("Invalid")