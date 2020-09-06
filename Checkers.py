import numpy as np
class Checkers():
    def __init__(self,board_width):
        self.board_width = board_width
        self.board = []

    def GameInitiate(self):
        for h in range(self.board_width):
            for w in range(self.board_width):
                self.board.append("0")
        counter1 = 0
        counter2 = 0
        counter3 = 0
        for a in range(3):
            row = a * self.board_width
            b = 0
            if a % 2 == 0:
                b = 1
            for i in range(self.board_width):
                i += row
                if i % 2 == 0:
                    self.board[i+b] = 1
        for a in range(3):
            startingpoint = (self.board_width*self.board_width)-(3*self.board_width)
            row = a * self.board_width
            b = 1
            if a % 2 == 0:
                b = 0
            for i in range(self.board_width):
                i += row
                if i % 2 == 0:
                    self.board[startingpoint+i+b] = 2
    def PrintBoard(self):
        print("")
        print("   ",end="")
        for i in range(self.board_width):
            print(i,end=".")
        for i in range(self.board_width*self.board_width):
            if i % self.board_width == 0:
                print(end="\n")
                print(str(int(i/self.board_width)),end=". ")
            print(self.board[i],end=" ")
    def Move(self,loc,action):
        cords = loc[0] + (loc[1] * self.board_width)
        print(self.board[cords])
        P1 = True
        if(self.board[cords] == 2):
            P1 = False
        if action == 1:
            self.board[cords] = 0
            if P1 == True:
                self.board[(cords + self.board_width) + 1] = 1
            elif P1 == False:
                self.board[(cords - self.board_width) + 1] = 2
        elif action == 2:
            self.board[cords] = 0
            if P1 == True:
                self.board[(cords + self.board_width) - 1] = 1
            elif P1 == False:
                self.board[(cords - self.board_width) - 1] = 2

game = Checkers(10)
game.GameInitiate()
game.PrintBoard()
game.Move([3,2],1)
game.PrintBoard()




