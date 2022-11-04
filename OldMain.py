import heapq
import math
import sys
from pdb import Restart
import random
import ReadCSV as csv
from Board import Board
from queue import PriorityQueue
from copy import deepcopy
import time
 
print("HELLO")
st = time.time()
# "UD" for moving queen up and down. "4D" for 4 directions up, down, left, right
# "UDG" for "greedy best first with queen moving up and down"
# "HC" is Hill Climbing and "HC4D" is Hill Climbing in 4 directions up, down, left, right
#mode = "UD"
#mode = "UDG"
#mode = "4D"
mode = "HC"
#mode = "HC4D"

f = open('HillT.txt','w')

initialBoard = csv.readCSV('4x4.csv')

q = PriorityQueue()
nodeCount = 0

board = Board(initialBoard, 0)
print("initial Board")
board.printBoard()

# A* can only move up and down
if mode == "UD":
    maxLevel = 0
    if not board.isSafe(board):
        for moves in board.findPossibleMovesFromBoard():
            newBoard = deepcopy(board.board)
            newBoard[moves[0]][moves[1]] = 0
            newBoard[moves[2]][moves[3]] = moves[4]
            tempBoard = Board(newBoard, 1)

            # Heuristic 1: tempBoard.findNumQueensAttacking(tempBoard)
            # Heuristic 2: tempBoard.costFromAttackingPairsRecursive()
            # Replace heuristic calculation function below depending on which heuristic you want
            heuristic = tempBoard.costFromAttackingPairsRecursive()

            q.put((heuristic + (moves[4] ** 2), newBoard, 1, moves[4] ** 2))
            nodeCount += 1

        nextNode = q.get()
        cost = nextNode[3]
        #print('printing first cost: ', cost)
        nextBoard = Board(nextNode[1], 1)

        while not nextBoard.isSafe(nextBoard) and not q.empty():
            level = nextBoard.level
            if level > maxLevel:
                maxLevel = level
            for moves in nextBoard.findPossibleMovesFromBoard():
                newBoard = deepcopy(nextBoard.board)
                newBoard[moves[0]][moves[1]] = 0
                newBoard[moves[2]][moves[3]] = moves[4]
                tempBoard = Board(newBoard, 1)
                # Heuristic 1: tempBoard.findNumQueensAttacking(tempBoard)
                # Heuristic 2: tempBoard.costFromAttackingPairsRecursive()
                # Replace heuristic calculation function below depending on which heuristic you want
                heuristic = tempBoard.costFromAttackingPairsRecursive()
                #print(heuristic)
                # tempBoard.printBoard();
                q.put((cost + heuristic + (moves[4] ** 2), newBoard, level + 1, cost + moves[4] ** 2))
                nodeCount += 1

            nextNode = q.get()
            cost = nextNode[3]
            nextBoard = Board(nextNode[1], nextNode[2])
            print("printing next board with cost: ", cost)
            nextBoard.printBoard()

        # execution time
        et = time.time() - st 
        print('Execution time:', time.strftime("%H:%M:%S", time.gmtime(et)))
        print("Final Board, Cost: ", cost)
        print("Number Nodes Explored: ", nodeCount)
        print("Solution at Level: ", nextBoard.level)
        if nextBoard.level > maxLevel:
            maxLevel = nextBoard.level
        print("Max Level Reached: ", maxLevel)
        print("Effective Branching Factor: ", nodeCount ** (1/maxLevel))
        nextBoard.printBoard()


elif mode == "UDG":
    maxLevel = 0
    minH = 100000000000
    if not board.isSafe(board):
        for move in board.findPossibleMovesFromBoard():
            newBoard = deepcopy(board.board)
            newBoard[move[0]][move[1]] = 0
            newBoard[move[2]][move[3]] = move[4]
            tempBoard = Board(newBoard, 1)
            # Heuristic 1: tempBoard.findNumQueensAttacking(tempBoard)
            # Heuristic 2: tempBoard.costFromAttackingPairsRecursive()
            # Replace heuristic calculation function below depending on which heuristic you want
            heuristic = tempBoard.costFromAttackingPairsRecursive()
            q.put((heuristic, newBoard, 1, move[4] ** 2))
            nodeCount += 1

        nextNode = q.get()
        minH = nextNode[0]
        cost = nextNode[3]

        nextBoard = Board(nextNode[1], 1)

        while not nextBoard.isSafe(nextBoard) and not q.empty():
            level = nextBoard.level
            if level > maxLevel:
                maxLevel = level
            for moves in nextBoard.findPossibleMovesFromBoard():
                newBoard = deepcopy(nextBoard.board)
                newBoard[moves[0]][moves[1]] = 0
                newBoard[moves[2]][moves[3]] = moves[4]
                tempBoard = Board(newBoard, 1)
                # Heuristic 1: tempBoard.findNumQueensAttacking(tempBoard)
                # Heuristic 2: tempBoard.costFromAttackingPairsRecursive()
                # Replace heuristic calculation function below depending on which heuristic you want
                heuristic = tempBoard.costFromAttackingPairsRecursive()
                q.put((heuristic, newBoard, level + 1, cost + moves[4] ** 2))
                nodeCount += 1

            nextNode = q.get()
            minH = nextNode[0]
            cost = nextNode[3]
            nextBoard = Board(nextNode[1], nextNode[2])
            print("printing next board with cost: ", cost)
            nextBoard.printBoard()

        # execution time
        et = time.time() - st
        print('Execution time:', time.strftime("%H:%M:%S", time.gmtime(et)))
        print("Final Board, Cost: ", cost)
        print("Number Nodes Explored: ", nodeCount)
        print("Solution at Level: ", nextBoard.level)
        if nextBoard.level > maxLevel:
            maxLevel = nextBoard.level
        print("Max Level Reached: ", maxLevel)
        print("Effective Branching Factor: ", nodeCount ** (1/maxLevel))
        nextBoard.printBoard()


# A* with 4 directions
elif mode == "4D":
    maxLevel = 0
    if not board.isSafe(board):
        for moves in board.findPossibleMovesFromBoard4D():
            newBoard = deepcopy(board.board)
            newBoard[moves[0]][moves[1]] = 0
            newBoard[moves[2]][moves[3]] = moves[4]
            tempBoard = Board(newBoard, 1)
            # Heuristic 1: tempBoard.findNumQueensAttacking(tempBoard)
            # Heuristic 2: tempBoard.costFromAttackingPairsRecursive()
            # Replace heuristic calculation function below depending on which heuristic you want
            heuristic = tempBoard.findNumQueensAttacking(tempBoard)
            q.put((heuristic + (moves[4] ** 2), newBoard, 1, moves[4] ** 2))
            nodeCount += 1

        nextNode = q.get()
        cost = nextNode[3]
        #print('printing first cost: ', cost)
        nextBoard = Board(nextNode[1], 1)

        while not nextBoard.isSafe(nextBoard) and not q.empty():
            level = nextBoard.level
            if level > maxLevel:
                maxLevel = level
            for moves in nextBoard.findPossibleMovesFromBoard4D():
                newBoard = deepcopy(nextBoard.board)
                newBoard[moves[0]][moves[1]] = 0
                newBoard[moves[2]][moves[3]] = moves[4]
                tempBoard = Board(newBoard, 1)
                # Heuristic 1: tempBoard.findNumQueensAttacking(tempBoard)
                # Heuristic 2: tempBoard.costFromAttackingPairsRecursive()
                # Replace heuristic calculation function below depending on which heuristic you want
                heuristic = tempBoard.findNumQueensAttacking(tempBoard)
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
        print("Number Nodes Explored: ", nodeCount)
        print("Solution at Level: ", nextBoard.level)
        if nextBoard.level > maxLevel:
            maxLevel = nextBoard.level
        print("Max Level Reached: ", maxLevel)
        print("Effective Branching Factor: ", nodeCount ** (1 / maxLevel))
        nextBoard.printBoard()

elif mode == "HC":
    # num of attacking queens as h
    maxH = board.dimensions
    startList = []
    list = []
    solutions = PriorityQueue()
    reStartTimes = 0
    trappedTimes = 0
    temperature = (board.dimensions ** 2)
    explorationTime = 0

    if not board.isSafe(board):
        # find all possible start position
        for moves in board.findPossibleMovesForQueen():
            newBoard = deepcopy(board.board)
            newBoard[moves[0]][moves[1]] = 0
            newBoard[moves[2]][moves[3]] = moves[4]
            tempBoard = Board(newBoard, 1)
            # Heuristic 1: tempBoard.findNumQueensAttacking(tempBoard)
            # Heuristic 2: tempBoard.costFromAttackingPairsRecursive()
            # Replace heuristic calculation function below depending on which heuristic you want
            heuristic = tempBoard.findNumQueensAttacking(tempBoard) #* 100000000
            #heuristic = moves[4]
            spaceMove = moves[5]
            #pick better or equal position than now
            if heuristic <= maxH:
                startList.append((heuristic, newBoard, 1, (moves[4] ** 2)*spaceMove, spaceMove))
                #print('spaceMove', spaceMove)
                nodeCount += 1

    while temperature >= 1:
        #print(temperature)
        f.write(str(temperature))
        f.write('\n')

        reStartTimes += 1
        restart = False
        #print('restart!')
        # random start
        startT = time.time()
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
                # Heuristic 1: tempBoard.findNumQueensAttacking(tempBoard)
                # Heuristic 2: tempBoard.costFromAttackingPairsRecursive()
                # Replace heuristic calculation function below depending on which heuristic you want
                heuristic = tempBoard.findNumQueensAttacking(tempBoard) # * 100000000
                #heuristic = moves[4]
                spaceMove = moves[5]
                
                # if heuristic < currentH:
                list.append((heuristic, newBoard, level + 1, cost + (moves[4] ** 2)*spaceMove, spaceMove))
                #print('spaceMove', spaceMove)
                nodeCount += 1


                #restart when current cost is already larger than the current best solution
                currentCost = cost + (moves[4] ** 2)*spaceMove
                if (not solutions.empty()) and solutions.queue[0][0] < currentCost:
                    #print("end early!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                    restart = True
                    explorationTime += (time.time() - startT)
                    #print(explorationTime)
                    break
                
            if restart:
                break
                
                #q.put((cost + heuristic + (moves[4] ** 2), newBoard, level + 1, cost + moves[4] ** 2))
                #nodeCount += 1


            if len(list) != 0:
                nextNode = random.choice(list)
                if nextNode[0] < currentH:
                    nextBoard = Board(nextNode[1], nextNode[2])
                else:
                    if  math.exp(-(currentH - nextNode[0]) / temperature):
                        nextBoard = Board(nextNode[1], nextNode[2])

            else:
                nextBoard = Board(nextNode[1], nextNode[2])
                break
        
            list.clear


            cost = nextNode[3]
            nextBoard = Board(nextNode[1], nextNode[2])
            #print("printing next board with cost: ", cost)
            #nextBoard.printBoard()

        if nextBoard.isSafe(nextBoard):
            newBoard = deepcopy(nextBoard.board)
            solutions.put((cost, newBoard, level + 1))

            #print('get one solution!')   
            temperature -= temperature * 0.1
            #temperature = temperature / (1 + reStartTimes)
        else:
            #print('trapped!!!!!!!!!!!!!!!!!!!!!!!')
            trappedTimes += 1
            temperature = temperature / ((1 + (time.time() - startT)))
            #temperature = temperature / (1 + reStartTimes)
            
            

    bestSolution = solutions.get()
    cost = bestSolution[0]
    bestBoard = Board(bestSolution[1], bestSolution[2])
    print("Final Board, Cost: ", cost)
    #print("Final Node Count: ", nodeCount)
    #print("Final Level: ", bestBoard.level)
    bestBoard.printBoard()

    # execution time
    et = time.time() - st
    print('Execution time:', et)
    print('Restart ', reStartTimes, ' times')
    print('Ends early ', trappedTimes, ' times')
    print('Finished climb that got solution:',reStartTimes - trappedTimes, "times" )
    print('Exploration Time', explorationTime)
    print('Exploitation Time:', et - explorationTime)


elif mode == "HC4D":
    # num of attacking queens as h
    maxH = board.dimensions
    startList = []
    list = []
    solutions = PriorityQueue()
    reStartTimes = 0
    trappedTimes = 0
    temperature = (board.dimensions ** 2)
    explorationTime = 0

    if not board.isSafe(board):
        # find all possible start position
        for moves in board.findPossibleMovesForQueen4D():
            newBoard = deepcopy(board.board)
            newBoard[moves[0]][moves[1]] = 0
            newBoard[moves[2]][moves[3]] = moves[4]
            tempBoard = Board(newBoard, 1)
            # Heuristic 1: tempBoard.findNumQueensAttacking(tempBoard)
            # Heuristic 2: tempBoard.costFromAttackingPairsRecursive()
            # Replace heuristic calculation function below depending on which heuristic you want
            heuristic = tempBoard.findNumQueensAttacking(tempBoard) #* 100000000
            #heuristic = moves[4]
            spaceMove = moves[5]
            #pick better or equal position than now
            if heuristic <= maxH:
                startList.append((heuristic, newBoard, 1, (moves[4] ** 2)*spaceMove, spaceMove))
                #print('spaceMove', spaceMove)
                nodeCount += 1

    while temperature >= 1:
        f.write(str(time.time()-st))
        f.write('\t')
        f.write(str(temperature))
        f.write('\n')

        reStartTimes += 1
        restart = False
        #print('restart!')
        # random start
        startT = time.time()
        nextNode = random.choice(startList)
        nextBoard = Board(nextNode[1], nextNode[2])
        cost = nextNode[3]

        #nextBoard.printBoard()
        
        while not nextBoard.isSafe(nextBoard):
            currentH = nextBoard.board[0][0]
            #print('currentH: ', currentH)
            level = nextBoard.level
            for moves in nextBoard.findPossibleMovesForQueen4D():
                newBoard = deepcopy(nextBoard.board)
                newBoard[moves[0]][moves[1]] = 0
                newBoard[moves[2]][moves[3]] = moves[4]
                tempBoard = Board(newBoard, 1)
                # Heuristic 1: tempBoard.findNumQueensAttacking(tempBoard)
                # Heuristic 2: tempBoard.costFromAttackingPairsRecursive()
                # Replace heuristic calculation function below depending on which heuristic you want
                heuristic = tempBoard.findNumQueensAttacking(tempBoard) # * 100000000
                #heuristic = moves[4]
                spaceMove = moves[5]
                
                # if heuristic < currentH:
                list.append((heuristic, newBoard, level + 1, cost + (moves[4] ** 2)*spaceMove, spaceMove))
                #print('spaceMove', spaceMove)
                nodeCount += 1


                #restart when current cost is already larger than the current best solution
                currentCost = cost + (moves[4] ** 2)*spaceMove
                if (not solutions.empty()) and solutions.queue[0][0] < currentCost:
                    #print("end early!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                    restart = True
                    explorationTime += (time.time() - startT )
                    #print(explorationTime)
                    break
                
            if restart:
                break
                
                #q.put((cost + heuristic + (moves[4] ** 2), newBoard, level + 1, cost + moves[4] ** 2))
                #nodeCount += 1


            if len(list) != 0:
                nextNode = random.choice(list)
                if nextNode[0] < currentH:
                    nextBoard = Board(nextNode[1], nextNode[2])
                else:
                    if  math.exp(-(currentH - nextNode[0]) / temperature):
                        nextBoard = Board(nextNode[1], nextNode[2])

            else:
                nextBoard = Board(nextNode[1], nextNode[2])
                break
        
            list.clear


            cost = nextNode[3]
            nextBoard = Board(nextNode[1], nextNode[2])
            #print("printing next board with cost: ", cost)
            #nextBoard.printBoard()

        if nextBoard.isSafe(nextBoard):
            newBoard = deepcopy(nextBoard.board)
            solutions.put((cost, newBoard, level + 1))

            #print('get one solution!')   
            temperature -= temperature * 0.1
            #temperature = temperature / (1 + reStartTimes)
        else:
            #print('trapped!!!!!!!!!!!!!!!!!!!!!!!')
            trappedTimes += 1
            temperature = temperature / ((1 + (time.time() - startT)))
            #temperature = temperature / (1 + reStartTimes)
            
            

    bestSolution = solutions.get()
    cost = bestSolution[0]
    bestBoard = Board(bestSolution[1], bestSolution[2])
    print("Final Board, Cost: ", cost)
    #print("Final Node Count: ", nodeCount)
    #print("Final Level: ", bestBoard.level)
    bestBoard.printBoard()

    # execution time
    et = time.time() - st
    print('Execution time:', et)
    print('Restart ', reStartTimes, ' times')
    print('Ends early ', trappedTimes, ' times')
    print('Finished climb that got solution:',reStartTimes - trappedTimes, "times" )
    print('Exploration Time', explorationTime)
    print('Exploitation Time:', et - explorationTime)