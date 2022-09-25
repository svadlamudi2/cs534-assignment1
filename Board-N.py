#import csv
#import numpy as np


from copy import deepcopy


class Board:
    def __init__(self, array, level):
        self.dimensions = len(array)
        self.board = array
        self.level = level

    def printBoard(self):
        for row in self.board:
            print(row)

    def findAllQueens(self):
        queenLocations = [[0] * 3 for i in range(self.dimensions)]
        counter = 0
        for i in range(0, self.dimensions):
            for j in range(0, self.dimensions):
                if self.board[i][j] > 0:
                    queenLocations[counter][0] = i
                    queenLocations[counter][1] = j
                    queenLocations[counter][2] = self.board[i][j]
                    counter += 1
        return queenLocations

    def outOfGrid(self, row, col):
        if (row < 0 or col < 0) or (row >= self.dimensions or col >= self.dimensions):
            return True
        else:
            return False


    def findVerticalAttack(self, col):
        counter = 0
        for i in range(self.dimensions):
            if counter > 1:
                return True
            if self.board[i][col] > 0:
                counter += 1
        if counter > 1:
            return True
        return False

    def findHorizontalAttack(self, row):
        counter = 0
        for i in range(self.dimensions):
            if counter > 1:
                return True
            if self.board[row][i] > 0:
                counter += 1
        if counter > 1:
            return True
        return False

    def findDiagonalAttack(self, row, col):
        mover = 1
        tempRow = row
        tempCol = col
        counter = 0

        # Check Backwards
        while not self.outOfGrid(tempRow, tempCol):
            if self.board[tempRow][tempCol] > 0:
                counter += 1

            tempRow = row - mover
            tempCol = col - mover

            mover += 1

        if counter > 1:
            return True

        mover = 1
        tempRow = row
        tempCol = col
        counter = 0

        while not self.outOfGrid(tempRow, tempCol):
            if self.board[tempRow][tempCol] > 0:
                counter += 1

            tempRow = row + mover
            tempCol = col + mover

            mover += 1

        if counter > 1:
            return True

        mover = 1
        tempRow = row
        tempCol = col
        counter = 0

        while not self.outOfGrid(tempRow, tempCol):
            if self.board[tempRow][tempCol] > 0:
                counter += 1

            tempRow = row + mover
            tempCol = col - mover

            mover += 1

        if counter > 1:
            return True

        mover = 1
        tempRow = row
        tempCol = col
        counter = 0

        while not self.outOfGrid(tempRow, tempCol):
            if self.board[tempRow][tempCol] > 0:
                counter += 1

            tempRow = row - mover
            tempCol = col + mover

            mover += 1

        if counter > 1:
            return True

        return False

    def findNumQueensAttacking(self, board):
        queensArray = board.findAllQueens()
        counter = 0
        for location in queensArray:
            if board.findHorizontalAttack(location[0]) or board.findVerticalAttack(location[1]) or \
                    board.findDiagonalAttack(location[0], location[1]):
                counter += 1
        return counter

    def findPossibleMovesFromBoard(self):
        possibleMoves = []
        spacesMoved = 1
        for location in self.findAllQueens():
            # Check if it is possible to move queen up without going out of board
            if not self.outOfGrid(location[0] - spacesMoved, location[1]):
                possibleMove = [location[0], location[1], location[0] - spacesMoved, location[1], location[2]]
                possibleMoves.append(possibleMove)
            # Check if it is possible to move queen down without going out of board
            if not self.outOfGrid(location[0] + spacesMoved, location[1]):
                possibleMove = [location[0], location[1], location[0] + spacesMoved, location[1], location[2]]
                possibleMoves.append(possibleMove)
        return possibleMoves

    #######QUINLIN CODE BELOW

    def findPossibleMovesFromBoard4D(self):
        possibleMoves = []
        spacesMoved = 1
        for location in self.findAllQueens():
            # Check if it is possible to move queen up without going out of board
            if ((not self.outOfGrid(location[0] - spacesMoved, location[1])) and (self.board[location[0] - spacesMoved][location[1]] == 0)):
                possibleMove = [location[0], location[1], location[0] - spacesMoved, location[1], location[2]]
                possibleMoves.append(possibleMove)
            # Check if it is possible to move queen down without going out of board
            if ((not self.outOfGrid(location[0] + spacesMoved, location[1])) and (self.board[location[0] + spacesMoved][location[1]] == 0)):
                possibleMove = [location[0], location[1], location[0] + spacesMoved, location[1], location[2]]
                possibleMoves.append(possibleMove)
            # Check if it is possible to move queen Left without going out of board
            if ((not self.outOfGrid(location[0], location[1] + spacesMoved)) and (self.board[location[0]][location[1] + spacesMoved] == 0)):
                possibleMove = [location[0], location[1], location[0], location[1] + spacesMoved, location[2]]
                possibleMoves.append(possibleMove)
            # Check if it is possible to move queen Right without going out of board
            if ((not self.outOfGrid(location[0], location[1] - spacesMoved)) and (self.board[location[0]][location[1] - spacesMoved] == 0)):
                possibleMove = [location[0], location[1], location[0], location[1] - spacesMoved, location[2]]
                possibleMoves.append(possibleMove)
        return possibleMoves

    def AddQueen(self, queen):
        self.queens.append(queen)
        self.UpdateBoard()

    def UpdateBoard(self):
        # self.board[x][y] = weight
        # load the queens to the board
        self.board = [[0 for i in range(self.rows)] for j in range(self.cols)]
        for i in range(len(self.queens)):
            self.board[self.queens[i].x][self.queens[i].y] = self.queens[i].weight

    def PrintBoard(self):
        for x in self.board:  # outer loop
            for i in x:  # inner loop
                print(i, end=" ")  # print the elements
            print()
        global Counter
        print("Node Number: ", Counter)
        Counter = Counter + 1

    # def CheckBoard(self):
    #     self.UnsafeQueens.clear()
    #     for i in range(len(self.queens)):
    #         for j in range(len(self.queens)):
    #             if ((self.queens[i].x == self.queens[j].x and i != j)
    #                     or (self.queens[i].y == self.queens[j].y and i != j)
    #                     or ((self.queens[i].x - self.queens[j].x) == (self.queens[i].y - self.queens[j].y) and (
    #                             i != j))
    #                     or ((self.queens[i].x - self.queens[j].x) == -(self.queens[i].y - self.queens[j].y) and (
    #                             i != j))):
    #                 self.UnsafeQueens.append(self.queens[i])
    #     if len(self.UnsafeQueens) == 0:
    #         self.safe = True
    #     else:
    #         self.safe = False

    def PrintQueens(self):
        for i in range(len(self.queens)):  # outer loop
            print(self.queens[i].x)  # print the elements
            print(self.queens[i].y)

            # returns a list of the attacking pairs weights

    # update for new layout @ANE
    def returnAttackingPairs(self):
        pairs = [];
        cost = 0;

        # traverse the full board
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):

                if self.board[i][j] > 0:
                    # look to the right for attacking pairs
                    for k in range(j + 1, len(self.board[i])):
                        if self.board[i][k] > 0:
                            pairs.append([self.board[i][j], self.board[i][k]]);
                            # look down for attacking pairs
                    for k in range(i + 1, len(self.board)):
                        if self.board[k][j] > 0:
                            pairs.append([self.board[i][j], self.board[k][j]]);

                            # insert check for diagonal
                    rcDiff = i - j;

                    # if board[i][j] > 0:
                    #     print(rcDiff);

                    # checks the right side of the board for diagonal attacking queens
                    for h in range(0, len(self.board)):  # i+1, len(board)):
                        for k in range(j + 1, len(self.board[i])):  # j+1, len(board[i])):
                            newRCDiff = h - k;
                            # checks if on the down-right diagonal
                            if newRCDiff == rcDiff and h != i and k != j and self.board[h][k] > 0:
                                pairs.append([self.board[i][j], self.board[h][k]]);
                            # checks if on the up-right diagonal
                            elif (rcDiff - newRCDiff) % 2 == 0 and h != i and k != j and self.board[h][k] > 0:
                                pairs.append([self.board[i][j], self.board[h][k]]);

        return pairs


    #takes in matrix
    def returnAttackingPairs(self, matrix):
        mat = matrix;
        listWithIndex = [];
        pairs = [];
        cost = 0;

        # traverse the full board
        for i in range(len(mat)):
            for j in range(len(mat[i])):

                if mat[i][j] > 0:
                    # look to the right for attacking pairs
                    for k in range(j + 1, len(mat[i])):
                        if mat[i][k] > 0:
                            listWithIndex.append(mat[i][j]);
                            listWithIndex.append(mat[i][k]);
                            listWithIndex.append(i);
                            listWithIndex.append(j);
                            listWithIndex.append(i);
                            listWithIndex.append(k);
                            pairs.append(listWithIndex);
                            listWithIndex = [];
                            #pairs.append([mat[i][j], mat[i][k]]);
                            # look down for attacking pairs
                    for k in range(i + 1, len(mat)):
                        if mat[k][j] > 0:
                            listWithIndex.append(mat[i][j]);
                            listWithIndex.append(mat[k][j]);
                            listWithIndex.append(i);
                            listWithIndex.append(j);
                            listWithIndex.append(k);
                            listWithIndex.append(j);
                            pairs.append(listWithIndex);
                            listWithIndex = [];
                            #pairs.append([mat[i][j], mat[k][j]]);

                            # insert check for diagonal
                    rcDiff = i - j;

                    # if board[i][j] > 0:
                    #     print(rcDiff);

                    # checks the right side of the board for diagonal attacking queens
                    for h in range(0, len(mat)):  # i+1, len(board)):
                        for k in range(j + 1, len(mat[i])):  # j+1, len(board[i])):
                            newRCDiff = h - k;
                            # checks if on the down-right diagonal
                            if newRCDiff == rcDiff and h != i and k != j and mat[h][k] > 0:
                                listWithIndex.append(mat[i][j]);
                                listWithIndex.append(mat[h][k]);
                                listWithIndex.append(i);
                                listWithIndex.append(j);
                                listWithIndex.append(h);
                                listWithIndex.append(k);
                                #print(listWithIndex);
                                pairs.append(listWithIndex);
                                listWithIndex = [];
                                #pairs.append([mat[i][j], mat[h][k]]);
                            # checks if on the up-right diagonal
                            elif (rcDiff - newRCDiff) % 2 == 0 and h != i and k != j and mat[h][k] > 0:
                                listWithIndex.append(mat[i][j]);
                                listWithIndex.append(mat[h][k]);
                                listWithIndex.append(i);
                                listWithIndex.append(j);
                                listWithIndex.append(h);
                                listWithIndex.append(k);
                                #print(listWithIndex);
                                pairs.append(listWithIndex);
                                listWithIndex = [];
                                #pairs.append([mat[i][j], mat[h][k]]);

        return pairs

    # takes in a list of attacking pairs weights and calculates the estimated cost to solve the position
    # by assuming for each pair of attacking queens will need to have the lower queen move 1 space
    # this heuristic is inadmissible since it is posssible to have one queen that is attacking two other
    # queens move one spot and resolve both pairs of attacking queens
    def costFromAttackingPairs(self):
        attackingPairs = self.returnAttackingPairs()
        cost = 0;
        for pair in attackingPairs:
            cost += pow(min(pair[0], pair[1]), 2);
        print(cost);
        return cost;

    def costFromAttackingPairs(self,  matrix):
        attackingPairs = self.returnAttackingPairs(self, matrix)
        cost = 0;
        for pair in attackingPairs:
            cost += pow(min(pair[0], pair[1]), 2);
        print(cost);
        return cost;

    
    def costFromAttackingPairsRecursive(self):
        # print("HERE");
        matrix = deepcopy(self.board);


        #matrix[0][0] = 9;
        
        # print("HERE")
        attackingPairs = self.returnAttackingPairs(matrix); 
        
        cost = 0;

        while len(attackingPairs) >= 1:
            minVal = 100;
            minX = 0;
            minY = 0;
            for pair in attackingPairs:
                if min(pair[0], pair[1]) < minVal:
                    
                    minVal = min(pair[0], pair[1])
                    if minVal == pair[0]:
                        minX = pair[2];
                        minY = pair[3];
                    else:
                        minX = pair[4];
                        minY = pair[5];
            # print("Coordinates of min");
            # print(minX, minY);
            cost += pow(minVal, 2);
            matrix[minX][minY] = 0;
            # print("Matrix Values");
            # print(matrix);
            # print("Cost");
            # print(cost);
            # print("\n");
            attackingPairs = self.returnAttackingPairs(matrix);
        #end of while 
        
        return cost;


    def isSafe(self, board):
        if self.findNumQueensAttacking(board) > 0:
            return False
        else:
            return True
