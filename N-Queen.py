
#number of the queens and also the size of the board
import copy


N = 4

# create queen by x, y, and weight
class Queen:
    def __init__(self, x, y, weight):
        self.x = x
        self.y = y
        self.weight = weight
    
    def Print(self):
        print(self.x)
        print(self.y)

    def MoveRight(self):
        self.y = self.y + 1

    def MoveLeft(self):
        self.y = self.y - 1

    def MoveUp(self):
        self.x = self.x - 1

    def MoveDown(self):
        self.x = self.x + 1

# board has the current board state
class Board:
    def __init__(self, N):
        self.cols = N
        self.rows = N
        self.board = [[0 for i in range(self.rows)] for j in range(self.cols)]
        self.queens = []

    def AddQueen(self, queen):
        self.queens.append(queen)
        self.UpdateBoard()

    def UpdateBoard(self):
        #self.board[x][y] = weight
        #load the queens to the board
        self.board = [[0 for i in range(self.rows)] for j in range(self.cols)]
        for i in range(len(self.queens)):
            self.board[self.queens[i].x][self.queens[i].y] = self.queens[i].weight

    def PrintBoard(self):
        for x in self.board:  # outer loop  
            for i in x:  # inner loop  
                print(i, end = " ") # print the elements  
            print() 

    def PrintQueens(self):
        for i in range(len(self.queens)):  # outer loop  
            print(self.queens[i].x) # print the elements  
            print(self.queens[i].y) 

class Node:
    def __init__(self, level, board, currentCost, h):
        self.level = level
        self.board = board
        self.currentCost = currentCost
        self.h = h
        self.total = currentCost + h

        
class Tree:
    def __init__(self, startNode):
        self.tree = []
        self.tree.append(startNode)
        #self.frontier  = []

    def AddNode(self, node):
        self.tree.append(node)

    def CreateNodes(self, parentNode):
        childNodes = []
        #********************
        for i in range(len(parentNode.board.queens)):
            tmpNode1 = copy.deepcopy(parentNode)
            tmpNode2 = copy.deepcopy(parentNode)
            tmpNode1.level += 1
            tmpNode2.level += 1

            if tmpNode1.board.queens[i].x >= 0 and tmpNode2.board.queens[i].x != N-1:     #check if can move down
                tmpNode1.board.queens[i].MoveDown()
                tmpNode1.board.UpdateBoard()
                childNodes.append(copy.deepcopy(tmpNode1))

            if tmpNode2.board.queens[i].x <= N-1 and tmpNode2.board.queens[i].x != 0:     #check if can move up
                tmpNode2.board.queens[i].MoveUp()
                tmpNode2.board.UpdateBoard()
                childNodes.append(copy.deepcopy(tmpNode2))

        #**********************
        self.tree.extend(copy.deepcopy(childNodes))
        

    def PrintTree(self):
        for i in range(len(self.tree)):
            print(self.tree[i].level)
            self.tree[i].board.PrintBoard()

        
#create board
board = Board(N)

#****************************************************************************************
#create the queens list
#need a function to read from file, now I just manuelly input the queen
q1 = Queen(0,1,4)
q2 = Queen(0,2,1)

board.AddQueen(q1)
board.AddQueen(q2)
#queens[0].MoveUp()
#queens.append(Queen(1,1,2))
#queens.append(Queen(2,2,4))
#queens.append(Queen(3,3,8))
#*****************************************************************************************


#print the board
#board.PrintBoard()
#board.PrintQueens()

#create the first node
startNode = Node(0, board, 0, 0)

#start the tree with the starting node
tree = Tree(startNode)

#print(tree.tree[0].board.PrintBoard())
#create next level
tree.CreateNodes(tree.tree[0])
tree.CreateNodes(tree.tree[2])

tree.PrintTree()




