import ReadCSV as csv
from Board import Board
from queue import PriorityQueue
from copy import deepcopy
import time
 
print("HELLO");
st = time.time()
# "UD" for moving queen up and down. "4D" for 4 directions up, down, left, right
# mode = "UD"
mode = "4D"

initialBoard = csv.readCSV('board5.csv')

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
            #print("PRE HEURISTIC")
            #tempBoard.printBoard();
            # multiple heuristic by * 100000000 to get greedy
            heuristic = tempBoard.costFromAttackingPairsRecursive()#tempBoard.findNumQueensAttacking(tempBoard) * 0 #* 100000000   #HEURIstic
            #print("POST HEURISTIC")
            #tempBoard.printBoard();
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
                # print("PRE HEURISTIC")
                # tempBoard.printBoard();
                # multiple heuristic by * 100000000 to get greedy
                heuristic = tempBoard.costFromAttackingPairsRecursive();#tempBoard.findNumQueensAttacking(tempBoard) * 0 #* 100000000  # heuristic
                # print("POST HEURISTIC")
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
            heuristic = tempBoard.costFromAttackingPairsRecursive();#tempBoard.findNumQueensAttacking(tempBoard)  #* 100000000  #heuristic
            q.put((heuristic + (moves[4] ** 2), newBoard, 1, moves[4] ** 2))
            nodeCount += 1

        nextNode = q.get()
        cost = nextNode[3]
        print('printing first cost: ', cost)
        nextBoard = Board(nextNode[1], 1)

        while not nextBoard.isSafe(nextBoard) and not q.empty():
            level = nextBoard.level
            for moves in nextBoard.findPossibleMovesFromBoard4D():
                newBoard = deepcopy(nextBoard.board)
                newBoard[moves[0]][moves[1]] = 0
                newBoard[moves[2]][moves[3]] = moves[4]
                tempBoard = Board(newBoard, 1)
                # multiple heuristic by * 100000000 to get greedy
                heuristic = tempBoard.costFromAttackingPairsRecursive();#tempBoard.findNumQueensAttacking(tempBoard) # * 100000000  # heuristic
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
        print("Final Node Count: ", nodeCount)
        print("Final Level: ", nextBoard.level)
        nextBoard.printBoard()

        #execution time
        et = time.time() - st
        print('Execution time:', time.strftime("%H:%M:%S", time.gmtime(et)))

        print("Final Board, Cost: ", cost)
        print("Final Node Count: ", nodeCount)
        print("Final Level: ", nextBoard.level)
        nextBoard.printBoard()

#Nikki Test

#returnAttackingPairs(mat);
#print(returnAttackingPairs(mat));
#(returnAttackingPairs(mat));
#print(board.costFromAttackingPairsRecursive());