

N = 4


class Queen:
    def __init__(self, x, y, weight):
        self.x = x
        self.y = y
        self.weight = weight
    
    def Print(self):
        print(self.x)
        print(self.y)

    def MoveUp(self):
        self.y = self.y + 1

    def MoveDown(self):
        self.y = self.y - 1

    def MoveLeft(self):
        self.x = self.x - 1

    def MoveRight(self):
        self.x = self.x + 1


class Board:
    def __init__(self, N):
        self.cols = N
        self.rows = N
        self.board = [[0 for i in range(self.cols)] for j in range(self.rows)]

    def UpdateQueens(self, x, y, weight):
        self.board[x][y] = weight

    def PrintBoard(self):
        for x in self.board:  # outer loop  
            for i in x:  # inner loop  
                print(i, end = " ") # print the elements  
            print()  




#create the queens list
queens = []

#need a function to read from file, now I just manuelly input the queen
queens.append(Queen(0,0,1))
queens.append(Queen(1,1,2))
queens.append(Queen(2,2,4))
queens.append(Queen(3,3,8))
#

#create board
board = Board(N)

#load the queens to the board
for i in range(len(queens)):
    board.UpdateQueens(queens[i].x, queens[i].y, queens[i].weight)

#print the board
board.PrintBoard()
