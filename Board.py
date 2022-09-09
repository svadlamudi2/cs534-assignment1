import csv
import numpy as np


class Board:
    def __init__(self):
        rows = 0
        with open('board.txt.csv', mode='r', encoding='utf-8-sig') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            for row in csv_reader:
                rows += 1

        self.board = [[0] * rows for i in range(rows)]
        self.dimensions = rows


        with open('board.txt.csv', mode='r', encoding='utf-8-sig') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            rowNum = 0
            for row in csv_reader:
                colNum = 0
                for value in row:
                    if value == '':
                        self.board[rowNum][colNum] = 0
                    else:
                        self.board[rowNum][colNum] = int(value)
                    colNum += 1
                rowNum += 1

    def findAllQueens(self):
        queenLocations = [[0] * 2 for i in range(self.dimensions)]
        counter = 0
        for i in range(0, self.dimensions):
            for j in range(0, self.dimensions):
                if self.board[i][j] > 0:
                    queenLocations[counter][0] = i
                    queenLocations[counter][1] = j
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

        return False

    def findHorizontalAttack(self, row):
        counter = 0
        for i in range(self.dimensions):
            if counter > 1:
                return True
            if self.board[row][i] > 0:
                counter += 1

        return False

    def findDiagonalAttack(self, row, col):
        mover = 1
        backRow = row
        forwardRow = row
        backCol = col
        forwardCol = col
        counter = 0

        #Check Backwards
        while not self.outOfGrid(backRow, backCol):
            backRow = row - mover
            backCol = col - mover

            if self.board[backRow][backCol] > 0:
                if counter > 1:
                    return True
                counter += 1

            mover += 1

        mover = 1

        while not self.outOfGrid(forwardRow, forwardCol):
            forwardRow = row + mover
            forwardCol = col + mover

            if self.board[forwardRow][forwardCol] > 0:
                if counter > 1:
                    return True
                counter += 1

            mover += 1

        return False

    def findNumQueensAttacking(self):
        queensArray = self.findAllQueens()
        counter = 0
        for location in queensArray:
            if self.findHorizontalAttack(location[0]) or self.findVerticalAttack(location[1]) or \
                    self.findDiagonalAttack(location[0], location[1]):
                counter += 1

board = Board()
print(board.findDiagonalAttack(1, 3))


