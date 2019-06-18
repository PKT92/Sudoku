import math
import copy

class Node:
    def __init__(self, value):
        self.dataval = value
        self.sudokuVal = 1
        self.nextNode = None
        self.prevNode = None

    def getValue(self):
        return self.dataval
    
    def getNextNode(self):
        return self.nextNode
    
    def getPrevNode(self):
        return self.prevNode

class LinkedList:
    def __init__(self):
        self.head = None
        self.last = None
        self.size = 0

    def addNode(self, Node):
        if self.head == None:
            self.head = Node
            self.last = Node
        else:
            self.last.nextNode = Node
            Node.prevNode = self.last
            self.last = Node
        self.size += 1
    
    def printList(self):
        node = self.head
        while(node != None):
            print(node.dataval)
            node = node.nextNode
    
    def printListRev(self):
        node = self.last
        while(node != None):
            print(node.dataval)
            node = node.prevNode

    def getHead(self):
        return self.head

def checkRow(n, row):
    if n in row:
        # print("Check row failed")
        return False
    else:
        return True

def checkCol(n, board, col):
    for i in board:
        if i[col] == n:
            # print("Check col failed")
            return False
    return True

def checkSquare(n, board, col, row):
    rowMin = math.floor(row/3)*3
    colMin = math.floor(col/3)*3
    for i in range(rowMin, rowMin+3):
        for j in range(colMin, colMin+3):
            if board[i][j] == n:
                # print("Check square failed")
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
sudoku = [[] for i in range(9)]
empties = LinkedList()
for i in range(9):
    tmp = inputFile.readline().rstrip()
    for j in range(9):
        if tmp[j] == "_":
            empties.addNode(Node([i,j]))
        sudoku[i].append(tmp[j])
solved = copy.deepcopy(sudoku)
print(*sudoku, sep='\n')
validBoard = True
currentNode = empties.getHead()
while(currentNode != None):
    row = currentNode.getValue()[0]
    col = currentNode.getValue()[1]
    tmpVal = str(currentNode.sudokuVal)
    if checkCol(tmpVal, solved, col) and checkRow(tmpVal, solved[row]) and checkSquare(tmpVal, solved, col, row):
        currentNode = currentNode.getNextNode()
        solved[row][col] = tmpVal
    else:
        if currentNode.sudokuVal < 9:
            currentNode.sudokuVal += 1
        else:
            currentNode.sudokuVal = 1
            currentNode = currentNode.getPrevNode()
            solved[row][col] = "_"
print()
if checkBoard(solved):
    print(*solved, sep='\n')
else:
    print("Invalid")