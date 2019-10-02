from world import *
import keyboard


class Move:
    pass


class Game:
    def __init__(self, world):
        self.world = world
        self.p_loc = []
        self.c_loc = [0, 0]
        self.pMove = None
        self.world.board[0][0].visited = True
        self.world.board[0][0].visitedValue += 1
        self.updateBoardForBreeze(0, 0, -1)
        self.updateBoardForStench(0, 0, -1)
        self.dir = "right"
        self.score = 0

    def nextPosition(self, r, c):
        if self.world.board[r][c].glitter:
            print("found Gold")
            self.score += 1000
            print("Score: ", self.score)
            exit()
            self.printPrevPath()
            return
        if (self.world.board[r][c].breeze):
            self.updateBoardForBreeze(r, c, 1)
        else:
            self.updateBoardForBreeze(r, c, -1)

        if (self.world.board[r][c].stench):
            self.updateBoardForStench(r, c, 1)
        else:
            self.updateBoardForStench(r, c, -1)


    def printPrevPath(self):
        pass
    def updateBoardForBreeze(self,r,c,val):

        if (r + 1 < self.world.row):
            self.world.board[r + 1][c].pitValue += val

        if (r - 1 >= 0):
            self.world.board[r - 1][c].pitValue += val
        if (c + 1 < self.world.col):
            self.world.board[r][c + 1].pitValue += val
        if (c - 1 >= 0):
            self.world.board[r][c - 1].pitValue += val

    def updateBoardForStench(self, r, c, val):
        if (r + 1 < self.world.row):
            self.world.board[r + 1][c].wumpusValue += val
            if self.world.board[r + 1][c].wumpusValue >= 2:
                print(r+1,c,"shoo-------------------------------------------------------------------------------------------------------t")
        if (r - 1 >= 0):
            self.world.board[r - 1][c].wumpusValue += val
            if self.world.board[r + 1][c].wumpusValue >= 2:
                print(r+1,c,"shoo-------------------------------------------------------------------------------------------------------t")
        if (c + 1 < self.world.col):
            self.world.board[r][c + 1].wumpusValue += val
            if self.world.board[r + 1][c].wumpusValue >= 2:
                print(r+1,c,"shoot-------------------------------------------------------------------------------------------------------")
        if (c - 1 >= 0):
            self.world.board[r][c - 1].wumpusValue += val
            if self.world.board[r + 1][c].wumpusValue >= 2:
                print(r+1,c,"shoot-------------------------------------------------------------------------------------------------------")

    def checkAdjacentCell(self,r,c):
        stack = []
        if(c+1<self.world.col and self.world.board[r][c+1].pitValue <= 0 and self.world.board[r][c+1].wumpusValue <= 0):
            stack.append([r, c+1]) #right

        if (r - 1 >= 0 and self.world.board[r-1][c].pitValue <= 0 and self.world.board[r-1][c].wumpusValue <= 0):
            stack.append([r-1, c])
        if (c - 1 >= 0 and self.world.board[r][c-1].pitValue <= 0 and self.world.board[r][c-1].wumpusValue <= 0):
            stack.append([r, c-1])
        if (r+1 < self.world.row and self.world.board[r + 1][c].pitValue <= 0 and self.world.board[r + 1][c].wumpusValue <= 0):
            stack.append([r + 1, c])

        return stack

    def move_forward(self):
        pass

    def run(self):
        while(True):
            self.nextPosition(self.c_loc[0], self.c_loc[1])
            stack = self.checkAdjacentCell(self.c_loc[0], self.c_loc[1])
            elem = self.choosePath(stack)
            expDir = self.direction(self.c_loc, elem)

            self.turn(expDir)


            self.world.board[elem[0]][elem[1]].visited = True
            self.world.board[elem[0]][elem[1]].visitedValue += 1
            print("moving Forward to", elem, "from", self.c_loc)
            self.c_loc = elem
            self.score -= 1
            self.showBoard()


        #print(stack)

    def choosePath(self, stack):
        for elem in stack:
            if not self.world.board[elem[0]][elem[1]].visited:
                self.p_loc.append(self.c_loc)
                # print(self.p_loc)
                # print(elem)
                return elem
        if len(stack) == 0:
            print("Not Possible")
            exit()
        min = self.world.board[stack[0][0]][stack[0][1]].visitedValue
        rv = stack[0]
        for elem in stack:
            if self.world.board[elem[0]][elem[1]].visitedValue <= min:
                rv = elem
                min = self.world.board[elem[0]][elem[1]].visitedValue

        return rv

    def direction(self, c_loc, elem):
        r1 = self.c_loc[0]
        c1 = self.c_loc[1]
        r2 = elem[0]
        c2 = elem[1]

        if(r2>r1 and c1==c2):
            return "up"
        elif r1>r2 and c1==c2:
            return "down"
        elif r1==r2 and c2<c1:
            return "left"
        elif r1==r2 and c2>c1:
            return "right"
        else:
            return self.dir

    def turn(self,ed):
        if(self.dir == "left"):
            if(ed == "left"):
                print("Turn:")
            elif (ed == "right"):
                print("Turn: right, right")
                self.score -= 2

            elif (ed == "up"):
                print("Turn: right")
                self.score -= 1
            elif (ed == "down"):
                print("Turn: left")
                self.score -= 1

        if (self.dir == "right"):
            if (ed == "left"):
                print("Turn: right, right")
                self.score -= 2
            elif (ed == "right"):
                print("Turn:")
            elif (ed == "up"):
                print("Turn: left")
                self.score -= 1
            elif (ed == "down"):
                print("Turn: right")
                self.score -= 1

        if (self.dir == "up"):
            if (ed == "left"):
                print("Turn: left")
                self.score -= 1
            elif (ed == "right"):
                print("Turn: right")
                self.score -= 1
            elif (ed == "up"):
                print("Turn: ")
            elif (ed == "down"):
                print("Turn: right,right")
                self.score -= 2

        if (self.dir == "down"):
            if (ed == "left"):
                print("Turn: right")
                self.score -= 1
            elif (ed == "right"):
                print("Turn: left")
                self.score -= 1
            elif (ed == "up"):
                print("Turn: right,right")
                self.score -= 2
            elif (ed == "down"):
                print("Turn:")


        self.dir = ed


    def showBoard(self):
        board = self.world.board
        for i in range (self.world.row):
            for j in range(self.world.col):
                if(board[i][j].visited):
                    if board[i][j].breeze or board[i][j].stench:

                        if(board[i][j].breeze):
                            print("b ", end="")
                        if board[i][j].stench:
                            print("s ", end="")
                    else:
                        print("V ", end = "")
                    print("  ",end ="")
                else:
                    print("xx", end= "  ")

            print("")




w = World(1)
g = Game(w)
g.run()
