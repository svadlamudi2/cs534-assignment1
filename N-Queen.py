
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
        self.UnsafeQueens =[]
        self.safe = False

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
        print(self.safe) 
    
    def CheckBoard(self):
        for i in range(len(self.queens)):
            for j in range(len(self.queens)):
                if ((self.queens[i].x == self.queens[j].x and i != j) 
                    or (self.queens[i].y == self.queens[j].y and i != j) 
                    or ((self.queens[i].x - self.queens[j].x) == (self.queens[i].y - self.queens[j].y) and (i != j))
                    or ((self.queens[i].x - self.queens[j].x) == -(self.queens[i].y - self.queens[j].y)and (i != j))):
                        self.UnsafeQueens.append(self.queens[i])
        if len(self.UnsafeQueens) == 0:
            self.safe = True
        else:
            self.safe = False

          
            

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
    
    def PrintNode(self):
        print(self.level)
        self.board.PrintBoard()


        
class Tree:
    def __init__(self, startNode):
        self.tree = []
        self.tree.append(startNode)
        self.frontier = []
        self.frontier.append(startNode)

    def AddNode(self, node):
        self.tree.append(node)

    def CreateNodesFrom(self, parentNode):
        self.frontier.remove(parentNode)
        childNodes = []
        #********************
        for i in range(len(parentNode.board.queens)):
            tmpNode1 = copy.deepcopy(parentNode)
            tmpNode2 = copy.deepcopy(parentNode)

            if tmpNode1.board.queens[i].x >= 0 and tmpNode2.board.queens[i].x != N-1:     #check if can move down
                tmpNode1.level += 1
                tmpNode1.board.queens[i].MoveDown()
                tmpNode1.board.UpdateBoard()
                tmpNode1.board.CheckBoard()
                childNodes.append(copy.deepcopy(tmpNode1))
                tmpNode1.PrintNode()

            if tmpNode2.board.queens[i].x <= N-1 and tmpNode2.board.queens[i].x != 0:     #check if can move up
                tmpNode2.level += 1
                tmpNode2.board.queens[i].MoveUp()
                tmpNode2.board.UpdateBoard()
                tmpNode2.board.CheckBoard()
                childNodes.append(copy.deepcopy(tmpNode2))
                tmpNode2.PrintNode()


        #**********************
        self.tree.extend(copy.deepcopy(childNodes))
        self.frontier.extend(copy.deepcopy(childNodes))

    """
    def PrintTree(self):
        for i in range(len(self.tree)):
            print(self.tree[i].level)
            print(self.tree[i].board.safe)
            self.tree[i].board.PrintBoard()
    """

        
        
#create board
board = Board(N)

#****************************************************************************************
#create the queens list
#need a function to read from file, now I just manuelly input the queen
q1 = Queen(1,0,4)
q2 = Queen(2,1,1)
q3 = Queen(0,2,3)
q4 = Queen(2,3,2)

board.AddQueen(q1)
board.AddQueen(q2)
board.AddQueen(q3)
board.AddQueen(q4)

#queens[0].MoveUp()
#queens.append(Queen(1,1,2))
#queens.append(Queen(2,2,4))
#queens.append(Queen(3,3,8))
#*****************************************************************************************

#print the board
#board.PrintBoard()
#board.PrintQueens()
board.UpdateBoard()
board.CheckBoard()

#create the first node
startNode = Node(0, board, 0, 0)



#start the tree with the starting node
tree = Tree(startNode)

#tree.tree[0].PrintNode()

for i in range(len(tree.frontier)):
    tree.frontier[i].board.CheckBoard()
    tree.frontier[i].PrintNode()

tree.CreateNodesFrom(tree.frontier[0])

for i in range(len(tree.frontier)):
    tree.frontier[i].board.CheckBoard()
    tree.frontier[i].PrintNode()


notDone = True

"""
while notDone:
    for i in range(len(tree.frontier)):
        tree.frontier[i].board.CheckBoard()
        if tree.frontier[i].board.safe == True:
            tree.frontier[i].PrintNode()
            notDone = False
            break

        else:
            tree.CreateNodesFrom(tree.frontier[i])
"""




