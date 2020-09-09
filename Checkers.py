import numpy as np
class Checkers():
    def __init__(self,board_width):
        self.board_width = board_width
        self.board = []
        self.turn = 1
        self.reward = 0
        self.P1list = {}
        self.P2list = {}
    def GameInitiate(self):
        for h in range(self.board_width):
            for w in range(self.board_width):
                self.board.append(0)
        for a in range(3):
            row = a * self.board_width
            b = 0
            if a % 2 == 0:
                b = 1
            for i in range(self.board_width):
                i += row
                if i % 2 == 0:
                    pos = i+b
                    self.board[pos] = 1
                    self.P1list[pos] = self.PosToLoc(pos)
        for a in range(3):
            startingpoint = (self.board_width*self.board_width)-(3*self.board_width)
            row = a * self.board_width
            b = 1
            if a % 2 == 0:
                b = 0
            for i in range(self.board_width):
                i += row
                if i % 2 == 0:
                    pos = startingpoint+i+b
                    self.board[pos] = 2
                    self.P2list[pos] = self.PosToLoc(pos)
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
    def PosToLoc(self,pos):
        return [pos - (self.board_width*int(pos/self.board_width)),int(pos/self.board_width)]
    def UpdateLocs(self,prevloc,futureloc,P):
        if P == 1:
            self.P1list.pop(prevloc)
            self.P1list[futureloc] = self.PosToLoc(futureloc)
        if P == 2:
            self.P2list.pop(prevloc)
            self.P2list[futureloc] = self.PosToLoc(futureloc)
    def GetColoum(self,pos):
        return pos - (self.board_width*int(pos/self.board_width))
    def Move(self,loc,action):
        cords = loc[0] + (loc[1] * self.board_width)
        startcoloum = self.GetColoum(cords)
        if(self.board[cords] == 0):
            return
        P1 = True
        if(self.board[cords] == 2):
            P1 = False
        if action == 2:
            if P1 == True:
                if self.turn == 1:

                    if(int(self.board[(cords + self.board_width) + 1]) == 2) and (self.GetColoum((cords + (self.board_width*2)) + 2) == startcoloum -1 or self.GetColoum((cords + (self.board_width*2)) + 2) == startcoloum +1):
                        self.board[cords] = 0
                        self.board[(cords + self.board_width) + 1] = 0
                        self.board[(cords + (self.board_width*2)) + 2] = 1
                        self.turn = 2
                        self.UpdateLocs(cords,(cords + (self.board_width*2)) + 2,1)
                    elif(int(self.board[(cords + self.board_width) + 1]) == 0) and (self.GetColoum((cords + self.board_width) + 1) == startcoloum -1 or self.GetColoum((cords + self.board_width) + 1) == startcoloum +1):
                        self.board[cords] = 0
                        self.board[(cords + self.board_width) + 1] = 1
                        self.turn = 2
                        self.UpdateLocs(cords,(cords + self.board_width) + 1,1)
                    else:
                        print("Cant move Their")
                        print("Tried to move to ",self.board[(cords - self.board_width) + 1])
                else:
                    print("Not you're turn")
            elif P1 == False:
                if self.turn == 2:
                    if(int(self.board[(cords - self.board_width) + 1]) == 1) and (self.GetColoum((cords + (self.board_width*2)) + 2) == startcoloum -2 or self.GetColoum((cords + (self.board_width*2)) + 2) == startcoloum +2):
                        self.board[cords] = 0
                        self.board[(cords - self.board_width) + 1] = 0
                        self.board[(cords - (self.board_width*2)) + 2] = 2
                        self.turn = 1
                        self.UpdateLocs(cords,cords - (self.board_width*2) + 2,2)
                        
                    elif(int(self.board[(cords - self.board_width) + 1]) == 0) and (self.GetColoum((cords + self.board_width) + 1) == startcoloum -1 or self.GetColoum((cords + self.board_width) + 1) == startcoloum +1):
                        self.board[cords] = 0
                        self.board[(cords - self.board_width) + 1] = 2
                        self.turn = 1
                        self.UpdateLocs(cords,(cords - self.board_width) + 1,2)
                    else:
                        print("Cant move Their")
                        print("Tried to move to ",self.board[(cords - self.board_width) + 1])
                else:
                    print("Not you're turn")
        elif action == 1:
            if P1 == True:
                if self.turn == 1:
                    if(int(self.board[(cords + self.board_width) - 1]) == 2) and (self.GetColoum((cords + (self.board_width*2)) - 2) == startcoloum -1 or self.GetColoum((cords + (self.board_width*2)) - 2) == startcoloum +1):
                        self.board[cords] = 0
                        self.board[(cords + self.board_width) - 1] = 0
                        self.board[(cords + self.board_width + self.board_width) - 2] = 1
                        self.turn = 2
                        self.UpdateLocs(cords,(cords + self.board_width) - 1,1)
                    elif(int(self.board[(cords + self.board_width) - 1]) == 0) and (self.GetColoum((cords + self.board_width) - 1) == startcoloum -1 or self.GetColoum((cords + self.board_width) - 1) == startcoloum +1):
                        self.board[cords] = 0
                        self.board[(cords + self.board_width) - 1] = 1
                        self.turn = 2
                        self.UpdateLocs(cords,(cords + self.board_width) - 1,1)
                    else:
                        print("Cant move Their")
                        print("Tried to move to ",self.board[(cords - self.board_width) + 1])
                else:
                    print("Not you're turn")
            elif P1 == False:
                if self.turn == 2:
                    if(int(self.board[(cords - self.board_width) - 1]) == 1) and (self.GetColoum((cords + (self.board_width*2)) - 2) == startcoloum -1 or self.GetColoum((cords + (self.board_width*2)) - 2) == startcoloum +1):
                        self.board[cords] = 0
                        self.board[(cords - self.board_width) - 1] = 0
                        self.board[(cords - (self.board_width*2)) - 2] = 2
                        self.turn = 1
                        self.UpdateLocs(cords,cords - (self.board_width*2) - 2,2)
                    elif(int(self.board[(cords - self.board_width) - 1]) == 0):
                        self.board[cords] = 0
                        self.board[(cords - self.board_width) - 1] = 2
                        self.turn = 1
                        self.UpdateLocs(cords,(cords - self.board_width) - 1,2)
                        
                    else:
                        print("Cant move Their")
                        print("Tried to move to ",self.board[(cords - self.board_width) + 1])
                else:
                    print("Not you're turn")
    def CheckWin(self):
        P1 = 0
        P2 = 0
        for i in self.board:
            if int(i) == 1:
                P1 += 1
            elif int(i) == 2:
                P2 +=1
        if P2 == 0:
            return "P1 Won"
        elif P1 == 0:
            return "P1 lost"
        else:
            return ""
    def DiscoverMoves(self,P):
        if P == 1:
            
        

game = Checkers(8)
game.GameInitiate()
game.PrintBoard()
print(game.GetColoum(10))
while True:
    print("")
    X = input("X: ")
    Y = input("Y: ")
    Action = input("Action: ")
    if(Action != 3):
        game.Move([int(X),int(Y)],int(Action))
        game.PrintBoard()
        print(game.CheckWin())





