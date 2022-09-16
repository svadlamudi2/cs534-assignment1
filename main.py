import ReadCSV as csv
from Board import Board
from queue import PriorityQueue
from copy import deepcopy

initialBoard = csv.readCSV('board.csv')

q = PriorityQueue()
nodeCount = 0

board = Board(initialBoard, 0)
print("initial Board")
board.printBoard()

if not board.isSafe(board):

    for moves in board.findPossibleMovesFromBoard():
        newBoard = deepcopy(board.board)
        newBoard[moves[0]][moves[1]] = 0
        newBoard[moves[2]][moves[3]] = moves[4]
        q.put((moves[4] ** 2, newBoard, 1))
        nodeCount += 1

    nextNode = q.get()
    cost = nextNode[0]
    nextBoard = Board(nextNode[1], 1)

    while not nextBoard.isSafe(nextBoard) and not q.empty():
        level = nextBoard.level
        for moves in nextBoard.findPossibleMovesFromBoard():
            newBoard = deepcopy(nextBoard.board)
            newBoard[moves[0]][moves[1]] = 0
            newBoard[moves[2]][moves[3]] = moves[4]
            q.put((cost + moves[4] ** 2, newBoard, level + 1))
            nodeCount += 1

        nextNode = q.get()
        cost = nextNode[0]
        nextBoard = Board(nextNode[1], nextNode[2])
        cost += nextBoard.findNumQueensAttacking(nextBoard)

    print("Final Board, Cost: ", cost)
    print("Final Node Count: ", nodeCount)
    print("Final Level: ", nextBoard.level)
    nextBoard.printBoard()
