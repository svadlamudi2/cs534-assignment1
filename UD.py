import heapq
import sys
from pdb import Restart
import random
import ReadCSV as csv
from Board import Board
from queue import PriorityQueue
from copy import deepcopy
import time
import random
import csv

def generateBoard(N,seed):
    board = [[0] * N for j in range(N)]
    random.seed(seed)
    for i in range(N):
        board[random.randint(0, N-1)][i] = random.randint(1,9)
    return board

def greedy(initialBoard):
    q = PriorityQueue()
    nodeCount = 0
    board = Board(initialBoard, 0)
    st = time.time()
    visitedBoards=[]

    print("initial Board")
    board.printBoard()


    if not board.isSafe(board):
        for move in board.findPossibleMovesFromBoard():
            newBoard = deepcopy(board.board)
            newBoard[move[0]][move[1]] = 0
            newBoard[move[2]][move[3]] = move[4]
            tempBoard = Board(newBoard, 1)
            heuristic = tempBoard.goodHeuristic() #costFromAttackingPairsRecursive() #tempBoard.findNumQueensAttacking(tempBoard)
            q.put((heuristic, newBoard, 1, move[4] ** 2))
            nodeCount += 1

        nextNode = q.get()
        q = PriorityQueue()
        cost = nextNode[3]

        nextBoard = Board(nextNode[1], 1)
        visitedBoards.append(nextBoard.board)

        ct = time.time() - st
        while not nextBoard.isSafe(nextBoard) and ct < 30:
            nextBoard.level+=1
            for moves in nextBoard.findPossibleMovesFromBoard():
                newBoard = deepcopy(nextBoard.board)
                newBoard[moves[0]][moves[1]] = 0
                newBoard[moves[2]][moves[3]] = moves[4]
                tempBoard = Board(newBoard, 1)
                heuristic = tempBoard.goodHeuristic() # costFromAttackingPairsRecursive() #tempBoard.findNumQueensAttacking(tempBoard)
                if (newBoard not in visitedBoards):
                    q.put((heuristic, newBoard, nextBoard.level, cost + moves[4] ** 2))
                    nodeCount += 1

            nextNode = q.get()
            q = PriorityQueue()
            cost = nextNode[3]
            nextBoard = Board(nextNode[1], nextNode[2])
            visitedBoards.append(nextBoard.board)
            #print("printing next board with cost: ", cost)
            #nextBoard.printBoard()
            ct = time.time() - st

    else:
        nextBoard = board
        cost = 0

    return st, nextBoard, nodeCount, nextBoard.level, nextBoard.calculateFinalCost(board)

def aStar(initialBoard):
    q = PriorityQueue()
    nodeCount = 0
    st = time.time()
    board = Board(initialBoard, 0)
    print("initial Board")
    board.printBoard()

    maxLevel = 0
    if not board.isSafe(board):
        for moves in board.findPossibleMovesFromBoard():
            newBoard = deepcopy(board.board)
            newBoard[moves[0]][moves[1]] = 0
            newBoard[moves[2]][moves[3]] = moves[4]
            tempBoard = Board(newBoard, 1)
            # print("PRE HEURISTIC")
            # tempBoard.printBoard();
            # multiple heuristic by * 100000000 to get greedy
            heuristic = tempBoard.goodHeuristic() # tempBoard.costFromAttackingPairsRecursive() tempBoard.findNumQueensAttacking(tempBoard)
            # print("POST HEURISTIC")
            # tempBoard.printBoard();
            q.put((heuristic + (moves[4] ** 2), newBoard, 1, moves[4] ** 2))
            nodeCount += 1

        nextNode = q.get()
        cost = nextNode[3]
        # print('printing first cost: ', cost)
        nextBoard = Board(nextNode[1], 1)
        ct = time.time() - st
        while not nextBoard.isSafe(nextBoard) and not q.empty() and ct < 30:
            level = nextBoard.level
            if level > maxLevel:
                maxLevel = level
            for moves in nextBoard.findPossibleMovesFromBoard():
                newBoard = deepcopy(nextBoard.board)
                newBoard[moves[0]][moves[1]] = 0
                newBoard[moves[2]][moves[3]] = moves[4]
                tempBoard = Board(newBoard, 1)
                # print("PRE HEURISTIC")
                # tempBoard.printBoard();
                # multiple heuristic by * 100000000 to get greedy
                heuristic = tempBoard.goodHeuristic()  # tempBoard.costFromAttackingPairsRecursive() tempBoard.findNumQueensAttacking(tempBoard)
                # print("POST HEURISTIC")
                # tempBoard.printBoard();
                q.put((cost + heuristic + (moves[4] ** 2), newBoard, level + 1, cost + moves[4] ** 2))
                nodeCount += 1

            nextNode = q.get()
            cost = nextNode[3]
            nextBoard = Board(nextNode[1], nextNode[2])
            # print("printing next board with cost: ", cost)
            # nextBoard.printBoard()
            ct = time.time() - st
    else:
        nextBoard = board
        cost = 0
    return st, nextBoard, nodeCount, nextBoard.level, cost

def printResults(startTime,board, nodeCount, level, cost):
    et = time.time() - startTime
    print('Solution Found:', board.isSafe(board))
    print('Execution time:', time.strftime("%H:%M:%S", time.gmtime(et)))
    print("Final Board Cost: ", cost)
    print("Number Nodes Explored: ", nodeCount)
    print("Solution at Level: ", level)
    if level != 0:
        print("Effective Branching Factor: ", nodeCount ** (1 / level))
    board.printBoard()
    return

def tallyResults(N):
    file = open("data.csv","w")
    csvFile = csv.writer(file)
    resultsGreedy = []
    resultsAStar = []
    for j in range(4,10):
        solvedG = 0
        totalTimeG = 0
        totalNodeCountSolvedG = 0
        totalCostG = 0
        totalLevelG = 0

        totalNodeCountNotSolvedG = 0

        solvedA = 0
        totalTimeA = 0
        totalNodeCountSolvedA = 0
        totalCostA = 0
        totalLevelA = 0

        totalNodeCountNotSolvedA = 0
        for i in range(0, N):
            print("Greedy:")
            st, board, nodeCount, level, cost = greedy(generateBoard(j, i))
            if board.isSafe(board):
                solvedG+=1
                totalTimeG += (time.time()-st)
                totalNodeCountSolvedG+=nodeCount
                totalCostG += cost
                totalLevelG += level
            else:
                totalNodeCountNotSolvedG += nodeCount

            printResults(st, board, nodeCount, level, cost)

            print("A*")
            st, board, nodeCount, level, cost = aStar(generateBoard(j, i))
            if board.isSafe(board):
                solvedA+=1
                totalTimeA += (time.time()-st)
                totalNodeCountSolvedA+=nodeCount
                totalCostA += cost
                totalLevelA += level
            else:
                totalNodeCountNotSolvedA += nodeCount
            printResults(st, board, nodeCount, level, cost)

        avgTimeG = 0
        avgNodeCountSolvedG = 0
        avgCostG = 0
        avgLevelG = 0
        avgNodeCountNotSolvedG = 0
        avgBranchingFactorG = 0
        if solvedG != 0:
            avgTimeG = totalTimeG/solvedG
            avgNodeCountSolvedG = totalNodeCountSolvedG/solvedG
            avgCostG = totalCostG/solvedG
            avgLevelG = totalLevelG/solvedG
            avgBranchingFactorG = avgNodeCountSolvedG ** (1 / avgLevelG)
        if (N - solvedG) != 0:
            avgNodeCountNotSolvedG = totalNodeCountNotSolvedG/(N-solvedG)

        resultsGreedy.append([j, solvedG, avgTimeG,avgLevelG, avgCostG,avgBranchingFactorG, avgNodeCountSolvedG,N-solvedG,avgNodeCountNotSolvedG])
        csvFile.writerow(["Greedy",j, solvedG, avgTimeG,avgLevelG, avgCostG,avgBranchingFactorG, avgNodeCountSolvedG,N-solvedG,avgNodeCountNotSolvedG])

        avgTimeA = 0
        avgNodeCountSolvedA = 0
        avgCostA = 0
        avgLevelA = 0
        avgNodeCountNotSolvedA = 0
        avgBranchingFactorA = 0
        if solvedA != 0:
            avgTimeA = totalTimeA / solvedA
            avgNodeCountSolvedA = totalNodeCountSolvedA / solvedA
            avgCostA = totalCostA / solvedA
            avgLevelA = totalLevelA / solvedA
            avgBranchingFactorA = avgNodeCountSolvedA ** (1 / avgLevelA)
        if (N - solvedA) != 0:
            avgNodeCountNotSolvedA = totalNodeCountNotSolvedA / (N - solvedA)

        resultsAStar.append([j, solvedA, avgTimeA,avgLevelA, avgCostA,avgBranchingFactorA, avgNodeCountSolvedA,N-solvedA,avgNodeCountNotSolvedA])
        csvFile.writerow(["A*", j, solvedA, avgTimeA,avgLevelA, avgCostA,avgBranchingFactorA, avgNodeCountSolvedA,N-solvedA,avgNodeCountNotSolvedA])

    print(resultsGreedy)
    print(resultsAStar)


