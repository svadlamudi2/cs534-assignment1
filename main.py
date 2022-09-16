import ReadCSV as csv
from Board import Board
from queue import PriorityQueue
from copy import deepcopy

initialBoard = csv.readCSV('board.csv')

q = PriorityQueue()

board = Board(initialBoard)
print("initial Board")
board.printBoard()

if not board.isSafe():

    for moves in board.findPossibleMovesFromBoard():
        newBoard = deepcopy(board.board)
        newBoard[moves[0]][moves[1]] = 0
        newBoard[moves[2]][moves[3]] = moves[4]
        q.put((moves[4] ** 2, newBoard))

    nextNode = q.get()
    cost = nextNode[0]
    nextBoard = Board(nextNode[1])

    while not nextBoard.isSafe() and not q.empty():
        for moves in nextBoard.findPossibleMovesFromBoard():
            newBoard = deepcopy(nextBoard.board)
            newBoard[moves[0]][moves[1]] = 0
            newBoard[moves[2]][moves[3]] = moves[4]
            q.put((cost + moves[4] ** 2, newBoard))

        nextNode = q.get()
        cost = nextNode[0]
        nextBoard = Board(nextNode[1])
        cost += nextBoard.findNumQueensAttacking()

    print("Final Board, Cost: ", cost)
    print(nextBoard.findNumQueensAttacking())
    nextBoard.printBoard()
