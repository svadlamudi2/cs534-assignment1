# number of the queens and also the size of the board
import copy
import Board

board = Board.Board()

N = 4
Counter = 0



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
# class Board:
#     def __init__(self, N):
#         self.cols = N
#         self.rows = N
#         self.board = [[0 for i in range(self.rows)] for j in range(self.cols)]
#         self.queens = []
#         self.UnsafeQueens = []
#         self.safe = False

#     def AddQueen(self, queen):
#         self.queens.append(queen)
#         self.UpdateBoard()
#
#     def UpdateBoard(self):
#         # self.board[x][y] = weight
#         # load the queens to the board
#         self.board = [[0 for i in range(self.rows)] for j in range(self.cols)]
#         for i in range(len(self.queens)):
#             self.board[self.queens[i].x][self.queens[i].y] = self.queens[i].weight
#
#     def PrintBoard(self):
#         for x in self.board:  # outer loop
#             for i in x:  # inner loop
#                 print(i, end=" ")  # print the elements
#             print()
#         global Counter
#         print("Node Number: ", Counter)
#         Counter = Counter + 1
#
#     def CheckBoard(self):
#         self.UnsafeQueens.clear()
#         for i in range(len(self.queens)):
#             for j in range(len(self.queens)):
#                 if ((self.queens[i].x == self.queens[j].x and i != j)
#                         or (self.queens[i].y == self.queens[j].y and i != j)
#                         or ((self.queens[i].x - self.queens[j].x) == (self.queens[i].y - self.queens[j].y) and (i != j))
#                         or ((self.queens[i].x - self.queens[j].x) == -(self.queens[i].y - self.queens[j].y) and (
#                                 i != j))):
#                     self.UnsafeQueens.append(self.queens[i])
#         if len(self.UnsafeQueens) == 0:
#             self.safe = True
#         else:
#             self.safe = False
#
#     def PrintQueens(self):
#         for i in range(len(self.queens)):  # outer loop
#             print(self.queens[i].x)  # print the elements
#             print(self.queens[i].y)
#
#             # returns a list of the attacking pairs weights
#
#     # update for new layout @ANE
#     def returnAttackingPairs(self):
#         pairs = [];
#         cost = 0;
#
#         # traverse the full board
#         for i in range(len(self.board)):
#             for j in range(len(self.board[i])):
#
#                 if self.board[i][j] > 0:
#                     # look to the right for attacking pairs
#                     for k in range(j + 1, len(self.board[i])):
#                         if self.board[i][k] > 0:
#                             pairs.append([self.board[i][j], self.board[i][k]]);
#                             # look down for attacking pairs
#                     for k in range(i + 1, len(self.board)):
#                         if self.board[k][j] > 0:
#                             pairs.append([self.board[i][j], self.board[k][j]]);
#
#                             # insert check for diagonal
#                     rcDiff = i - j;
#
#                     # if board[i][j] > 0:
#                     #     print(rcDiff);
#
#                     # checks the right side of the board for diagonal attacking queens
#                     for h in range(0, len(self.board)):  # i+1, len(board)):
#                         for k in range(j + 1, len(self.board[i])):  # j+1, len(board[i])):
#                             newRCDiff = h - k;
#                             # checks if on the down-right diagonal
#                             if newRCDiff == rcDiff and h != i and k != j and self.board[h][k] > 0:
#                                 pairs.append([self.board[i][j], self.board[h][k]]);
#                             # checks if on the up-right diagonal
#                             elif (rcDiff - newRCDiff) % 2 == 0 and h != i and k != j and self.board[h][k] > 0:
#                                 pairs.append([self.board[i][j], self.board[h][k]]);
#
#         return pairs
#
#     # takes in a list of attacking pairs weights and calculates the estimated cost to solve the position
#     # by assuming for each pair of attacking queens will need to have the lower queen move 1 space
#     # this heuristic is inadmissible since it is posssible to have one queen that is attacking two other
#     # queens move one spot and resolve both pairs of attacking queens
#     def costFromAttackingPairs(self):
#         attackingPairs = self.returnAttackingPairs()
#         cost = 0;
#         for pair in attackingPairs:
#             cost += pow(min(pair[0], pair[1]), 2);
#         print(cost);
#         return cost;
#
#
class Node:
    def __init__(self, level, board, currentCost, h):
        self.level = level
        self.board = board
        self.currentCost = currentCost
        self.h = h
        self.total = currentCost + h

    def PrintNode(self):
        print("level:", self.level, "UnsafeQueensNum:", len(self.board.UnsafeQueens), "issafe?:", self.board.safe)
        self.board.PrintBoard()


class Tree:
    def __init__(self, startNode):
        self.frontier = []
        self.frontier.append(startNode)

    def AddNode(self, node):
        self.tree.append(node)

    def CreateNodesFrom(self, frontier, index):
        tmpNode = copy.deepcopy(frontier[index])
        del (self.frontier[index])
        # ********************
        for i in range(len(tmpNode.board.queens)):
            tmpNode1 = copy.deepcopy(tmpNode)
            tmpNode2 = copy.deepcopy(tmpNode)

            if tmpNode1.board.queens[i].x >= 0 and tmpNode2.board.queens[i].x != N - 1:  # check if can move down
                self.frontier.append(tmpNode1)
                tmpNode1.level += 1
                tmpNode1.board.queens[i].MoveDown()
                tmpNode1.board.UpdateBoard()
                tmpNode1.board.CheckBoard()
                tmpNode1.PrintNode()

            if tmpNode2.board.queens[i].x <= N - 1 and tmpNode2.board.queens[i].x != 0:  # check if can move up
                self.frontier.append(tmpNode2)
                tmpNode2.level += 1
                tmpNode2.board.queens[i].MoveUp()
                tmpNode2.board.UpdateBoard()
                tmpNode2.board.CheckBoard()
                tmpNode2.PrintNode()
        # **********************

    """
    def PrintTree(self):
        for i in range(len(self.tree)):
            print(self.tree[i].level)
            print(self.tree[i].board.safe)
            self.tree[i].board.PrintBoard()
    """

    def PrintFrontier(self):
        for i in range(len(self.frontier)):
            self.frontier[i].PrintNode()


# create board

print(board.findAllQueens())


# ****************************************************************************************
# create the queens list
# need a function to read from file, now I just manuelly input the queen

# q1 = Queen(1,0,4)
# q2 = Queen(2,1,1)
# q3 = Queen(0,2,3)
# q4 = Queen(2,3,2)
#
# board.AddQueen(q1)
# board.AddQueen(q2)
# board.AddQueen(q3)
# board.AddQueen(q4)


# queens[0].MoveUp()
# queens.append(Queen(1,1,2))
# queens.append(Queen(2,2,4))
# queens.append(Queen(3,3,8))
# *****************************************************************************************

# print the board
# board.PrintQueens()

queens = board.findAllQueens()

board.UpdateBoard()
# board.CheckBoard()
print("Starting", "unsafeQueens:", board.findNumQueensAttacking(), "isSafe?", board.isSafe())
board.PrintBoard()

# create the first node
startNode = Node(0, board, 0, 0)

# start the tree with the starting node
tree = Tree(startNode)

# tree.tree[0].PrintNode()

"""for i in range(len(tree.frontier)):
    tree.frontier[i].board.CheckBoard()
    tree.frontier[i].PrintNode()"""

tree.CreateNodesFrom(tree.frontier, 0)

tree.PrintFrontier()

# for i in range(len(tree.frontier)):
#    tree.frontier[i].PrintNode()


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
