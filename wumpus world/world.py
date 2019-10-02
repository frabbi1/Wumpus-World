import random

class Percept:
    def __init__(self):
        self.wumpus = False
        self.pit = False
        self.glitter = False
        self.stench = False
        self.breeze = False
        self.visited = False

        self.pitValue = 0
        self.wumpusValue = 0
        self.visitedValue = 0


class World:
    def __init__(self,opt):
        self.row = 10
        self.col = 10
        self.board = [[Percept() for j in range (self.col)] for i in range(self.row)]
        if(opt==1):
            self.addPits()
            self.addWumpus()
            self.addGold()
        else:
            self.addManualPits()
            self.addManualWumpus()
            self.addManualGold()



    def addPits(self):
        totalPits = int((self.row * self.col) * .2)

        for i in range(totalPits):
            rr = random.randint(0, self.row - 1)
            rc = random.randint(0, self.col - 1)
            if (rr != 0 and rc != 0):
                self.board[rr][rc].pit = True
                self.addBreeze(rr, rc)

    def addWumpus(self):
        while (True):
            rr = random.randint(0, self.row - 1)
            rc = random.randint(0, self.col - 1)
            if self.board[rr][rc].pit or (rr == 0 and rc == 0):
                continue
            else:
                self.board[rr][rc].wumpus = True
                self.addStench(rr, rc)
                break

    def addGold(self):
        while (True):
            rr = random.randint(0, self.row - 1)
            rc = random.randint(0, self.col - 1)

            if (self.board[rr][rc].pit or self.board[rr][rc].wumpus):
                continue
            else:
                self.board[rr][rc].glitter = True
                break

    def addBreeze(self, rr, rc):
        if (rr - 1 >= 0):
            self.board[rr - 1][rc].breeze = True
        if (rr + 1 < self.row):
            self.board[rr + 1][rc].breeze = True
        if (rc - 1 >= 0):
            self.board[rr][rc - 1].breeze = True
        if (rc + 1 < self.col):
            self.board[rr][rc + 1].breeze = True

    def addStench(self, rr, rc):
        if (rr - 1 >= 0):
            self.board[rr - 1][rc].stench = True
        if (rr + 1 < self.row):
            self.board[rr + 1][rc].stench = True
        if (rc - 1 >= 0):
            self.board[rr][rc - 1].stench = True
        if (rc + 1 < self.col):
            self.board[rr][rc + 1].stench = True

    def show(self):
        for r in range(self.row):
            for c in range(self.col):
                print(r, c, self.board[r][c].glitter)

    def addManualPits(self):
        for i in range (self.row):
            self.board[i][self.col-2].pit =  True
            self.addBreeze(i, self.col-2)

    def addManualWumpus(self):
        self.board[0][2].wumpus = True
        self.addStench(0,2)

    def addManualGold(self):
        self.board[7][2].glitter = True


