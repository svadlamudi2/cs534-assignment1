import ReadCSV as csv
from Board import Board
from queue import PriorityQueue
from copy import deepcopy

initialBoard = csv.readCSV('testBoard.csv')

q = PriorityQueue()

board = Board(initialBoard)
print(board.findNumQueensAttacking())
print("initial Board")
board.printBoard()

for moves in board.findPossibleMovesFromBoard():
    newBoard = deepcopy(board.board)
    newBoard[moves[0]][moves[1]] = 0
    newBoard[moves[2]][moves[3]] = moves[4]
    q.put((moves[4] ** 2, newBoard))

print("printing next board")
nextNode = q.get()
cost = nextNode[0]
nextBoard = Board(nextNode[1])
nextBoard.printBoard()
print("printing cost: ", cost)


# while not nextBoard.isSafe() and not q.empty():
#     for moves in nextBoard.findPossibleMovesFromBoard():
#         newBoard = deepcopy(nextBoard.board)
#         newBoard[moves[0]][moves[1]] = 0
#         newBoard[moves[2]][moves[3]] = moves[4]
#         q.put((cost + moves[4] ** 2, newBoard))
#
#     print("printing next board")
#     nextNode = q.get()
#     cost = nextNode[0]
#     nextBoard = Board(nextNode[1])
#     nextBoard.printBoard()
#     print("printing cost: ", cost)











