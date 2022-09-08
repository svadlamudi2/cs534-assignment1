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
                    self.board[rowNum][colNum] = value
                    colNum += 1
                rowNum += 1

