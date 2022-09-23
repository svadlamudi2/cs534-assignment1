from pdb import Restart
import random
import ReadCSV as csv
from Board import Board
from queue import PriorityQueue
from copy import deepcopy
import time

st = time.time()
# "UD" for moving queen up and down. "4D" for 4 directions up, down, left, right
mode = "UD"
#mode = "4D"
#mode = "HC"
#mode = "HC4D"

initialBoard = csv.readCSV('board.csv')

q = PriorityQueue()
nodeCount = 0

board = Board(initialBoard, 0)
print("initial Board")
board.printBoard()

# A* can only move up and down
if mode == "UD":
    if not board.isSafe(board):
        for moves in board.findPossibleMovesFromBoard():
            newBoard = deepcopy(board.board)
            newBoard[moves[0]][moves[1]] = 0
            newBoard[moves[2]][moves[3]] = moves[4]
            tempBoard = Board(newBoard, 1)
            # multiple heuristic by * 100000000 to get greedy
            heuristic = tempBoard.findNumQueensAttacking(tempBoard) #* 100000000
            #heuristic = tempBoard.findNumQueensAttacking(tempBoard) + (moves[4] ** 2)
            #heuristic = moves[4] ** 2
            q.put((heuristic + (moves[4] ** 2), newBoard, 1, moves[4] ** 2))
            nodeCount += 1

        nextNode = q.get()
        cost = nextNode[3]
        print('printing first cost: ', cost)
        nextBoard = Board(nextNode[1], 1)

        while not nextBoard.isSafe(nextBoard) and not q.empty():
            level = nextBoard.level
            for moves in nextBoard.findPossibleMovesFromBoard():
                newBoard = deepcopy(nextBoard.board)
                newBoard[moves[0]][moves[1]] = 0
                newBoard[moves[2]][moves[3]] = moves[4]
                tempBoard = Board(newBoard, 1)
                # multiple heuristic by * 100000000 to get greedy
                heuristic = tempBoard.findNumQueensAttacking(tempBoard) #* 100000000
                #heuristic = tempBoard.findNumQueensAttacking(tempBoard) + (moves[4] ** 2)
                #heuristic = moves[4] ** 2

                q.put((cost + heuristic + (moves[4] ** 2), newBoard, level + 1, cost + moves[4] ** 2))
                nodeCount += 1

            nextNode = q.get()
            cost = nextNode[3]
            nextBoard = Board(nextNode[1], nextNode[2])
            #print("printing next board with cost: ", cost)
            #nextBoard.printBoard()

        # execution time
        et = time.time() - st
        print('Execution time:', time.strftime("%H:%M:%S", time.gmtime(et)))

        print("Final Board, Cost: ", cost)
        print("Final Node Count: ", nodeCount)
        print("Final Level: ", nextBoard.level)
        nextBoard.printBoard()

# A* with 4 directions
elif mode == "4D":
    if not board.isSafe(board):
        for moves in board.findPossibleMovesFromBoard4D():
            newBoard = deepcopy(board.board)
            newBoard[moves[0]][moves[1]] = 0
            newBoard[moves[2]][moves[3]] = moves[4]
            tempBoard = Board(newBoard, 1)
            # multiple heuristic by * 100000000 to get greedy
            heuristic = tempBoard.findNumQueensAttacking(tempBoard) #* 100000000
            #heuristic = moves[4]
            q.put((heuristic + (moves[4] ** 2), newBoard, 1, moves[4] ** 2))
            nodeCount += 1

        nextNode = q.get()
        cost = nextNode[3]
        #print('printing first cost: ', cost)
        nextBoard = Board(nextNode[1], 1)

        while not nextBoard.isSafe(nextBoard) and not q.empty():
            level = nextBoard.level
            for moves in nextBoard.findPossibleMovesFromBoard4D():
                newBoard = deepcopy(nextBoard.board)
                newBoard[moves[0]][moves[1]] = 0
                newBoard[moves[2]][moves[3]] = moves[4]
                tempBoard = Board(newBoard, 1)
                # multiple heuristic by * 100000000 to get greedy
                heuristic = tempBoard.findNumQueensAttacking(tempBoard) # * 100000000
                #heuristic = moves[4]
                q.put((cost + heuristic + (moves[4] ** 2), newBoard, level + 1, cost + moves[4] ** 2))
                nodeCount += 1

            nextNode = q.get()
            cost = nextNode[3]
            nextBoard = Board(nextNode[1], nextNode[2])
            #print("printing next board with cost: ", cost)
            #nextBoard.printBoard()

        # execution time
        et = time.time() - st
        print('Execution time:', time.strftime("%H:%M:%S", time.gmtime(et)))

        print("Final Board, Cost: ", cost)
        print("Final Node Count: ", nodeCount)
        print("Final Level: ", nextBoard.level)
        nextBoard.printBoard()

elif mode == "HC":
    # num of attacking queens as h
    maxH = board.dimensions
    startList = []
    list = []
    solutions = PriorityQueue()
    reStartTimes = 0
    trappedTimes = 0
    temperature = (board.dimensions ** 2) * 2

    if not board.isSafe(board):
        for moves in board.findPossibleMovesForQueen():
            newBoard = deepcopy(board.board)
            newBoard[moves[0]][moves[1]] = 0
            newBoard[moves[2]][moves[3]] = moves[4]
            tempBoard = Board(newBoard, 1)
            #print('location:', moves[0], moves[1])
            # multiple heuristic by * 100000000 to get greedy
            heuristic = tempBoard.findNumQueensAttacking(tempBoard) #* 100000000
            #heuristic = moves[4]
            spaceMove = moves[5]
            if heuristic <= maxH:
                startList.append((heuristic, newBoard, 1, (moves[4] ** 2)*spaceMove, spaceMove))
                #print('spaceMove', spaceMove)
                nodeCount += 1

    while not temperature == 0:
        reStartTimes += 1
        # random start
        nextNode = random.choice(startList)
        nextBoard = Board(nextNode[1], nextNode[2])
        cost = nextNode[3]

        #nextBoard.printBoard()
        
        while not nextBoard.isSafe(nextBoard):
            currentH = nextBoard.board[0][0]
            #print('currentH: ', currentH)
            level = nextBoard.level
            for moves in nextBoard.findPossibleMovesForQueen():
                newBoard = deepcopy(nextBoard.board)
                newBoard[moves[0]][moves[1]] = 0
                newBoard[moves[2]][moves[3]] = moves[4]
                tempBoard = Board(newBoard, 1)
                # multiple heuristic by * 100000000 to get greedy
                heuristic = tempBoard.findNumQueensAttacking(tempBoard) # * 100000000
                #heuristic = moves[4]
                spaceMove = moves[5]
                list.clear
                if heuristic <= currentH:
                    list.append((heuristic, newBoard, level + 1, cost + (moves[4] ** 2)*spaceMove, spaceMove))
                    #print('spaceMove', spaceMove)
                    nodeCount += 1
                    
                #q.put((cost + heuristic + (moves[4] ** 2), newBoard, level + 1, cost + moves[4] ** 2))
                #nodeCount += 1

            if len(list) != 0:
                nextNode = random.choice(list)
            else:
                nextBoard = Board(nextNode[1], nextNode[2])
                break

            cost = nextNode[3]
            nextBoard = Board(nextNode[1], nextNode[2])
            #print("printing next board with cost: ", cost)
            #nextBoard.printBoard()

        if nextBoard.isSafe(nextBoard):
            newBoard = deepcopy(nextBoard.board)
            solutions.put((cost, newBoard, level + 1))   
            temperature -= 1
        else:
            #print('trapped')
            trappedTimes += 1

    bestSolution = solutions.get()
    cost = bestSolution[0]
    bestBoard = Board(bestSolution[1], bestSolution[2])
    print("Final Board, Cost: ", cost)
    print("Final Node Count: ", nodeCount)
    print("Final Level: ", bestBoard.level)
    bestBoard.printBoard()

    # execution time
    et = time.time() - st
    print('Execution time:', time.strftime("%H:%M:%S", time.gmtime(et)))
    print('Restart ', reStartTimes, ' times')
    print('Trapped ', trappedTimes, ' times')