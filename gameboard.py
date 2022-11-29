from car import Car
from copy import deepcopy


class Gameboard(object):
    def __init__(self, carFuel, carOrientation, state):
        self.carFuel = carFuel
        self.carOrientation = carOrientation
        self.children = []
        self.state = state

    def createGraph(self):
        if self.checkFuel():
            for c in self.carFuel:
                print(c)
                if self.carOrientation.get(c) == "h":
                    hcoords = self.getHorizontalCoordinates(c)
                    startCoord = hcoords[0]
                    endCoord = hcoords[1]
                    row = startCoord[0]
                    column = startCoord[1]
                    #check left
                    if self.carFuel.get(c) >0 and column -1 in range(6):
                        if self.state[row][column-1] == ".":
                            self.moveCarLeft(c,row,column,startCoord,endCoord)
                    #check right
                    row = endCoord[0]
                    column = endCoord[1]
                    if self.carFuel.get(c) >0 and column +1 in range(6):
                        if self.state[row][column+1] == ".":
                            self.moveCarRight(c,row,column,startCoord,endCoord)
                elif self.carOrientation.get(c) == "v":
                    vcoords = self.getVerticalCoordinates(c)
                    startCoord = vcoords[0]
                    endCoord = vcoords[1]
                    row = startCoord[0]
                    column = startCoord[1]
                    #check up
                    if self.carFuel.get(c) >0 and row-1 in range(6):
                        if self.state[row-1][column] == ".":
                            self.moveCarUp(c,row,column,endCoord)
                    #check down
                    row = endCoord[0]
                    column = endCoord[1]
                    if self.carFuel.get(c) >0 and row+1 in range(6):
                        if self.state[row+1][column] == ".":
                            self.moveCarDown(c,row,column,endCoord)
        else:
            return "no solution"

    def carAtExit(self,start,end):
        if start[0]==2 and start[1]==5:
            return True
        elif end[0]==2 and end[1]==5 :
            return True
        else:
            return False

    def removeCar(self,car):
        self.carFuel.pop(car)

    def checkFuel(self):
        fuelLeft = False
        for c in self.carFuel:
            if self.carFuel.get(c)>0:
                fuelLeft = True
        return fuelLeft

    def moveCarUp(self, c, row, column, endCoord):
            newState = deepcopy(self.state)
            newState[row-1][column] = c
            newState[endCoord[0]][endCoord[1]] = "."
            self.carFuel[c] = self.carFuel.get(c) -1
            newBoard = Gameboard(self.carFuel,self.carOrientation, newState)
            self.children.append(newBoard)

    def moveCarDown(self,c,row,column,endCoord):
        newState = deepcopy(self.state)
        newState[row+1][column] = c
        newState[endCoord[0]][endCoord[1]] = "."
        self.carFuel[c] = self.carFuel.get(c) -1
        newBoard = Gameboard(self.carFuel,self.carOrientation, newState)
        self.children = newBoard

    def moveCarLeft(self, c, row,column,startCoord, endCoord):
        newState = deepcopy(self.state)
        newState[row][column-1] = c
        newState[endCoord[0]][endCoord[1]] = "."
        self.carFuel[c] = self.carFuel.get(c) -1
        #check if at exit
        carPosition = self.carAtExit(startCoord,endCoord)
        if carPosition:
            if newState[2][5]=="A":
                return "win"
            else:
                x = 2
                y=5
                towCar = newState[x][y]
                while newState[x][y] ==towCar:
                    newState[x][y] = "."
                    if y-1 in range(6):
                        y-= 1
                    else:
                        break
                self.removeCar(towCar)
        newBoard = Gameboard(self.carFuel,self.carOrientation, newState)
        self.children.append(newBoard)

    def moveCarRight(self,c,row,column, startCoord,endCoord):
        newState = deepcopy(self.state)
        newState[row][column+1] = c
        newState[startCoord[0]][startCoord[1]] = "."
        self.carFuel[c] = self.carFuel.get(c) -1
        carPosition = self.carAtExit(startCoord,endCoord)
        if carPosition:
            if newState[2][5]=="A":
                return "win"
            else:
                x = 2
                y=5
                towCar = newState[x][y]
                while newState[x][y] ==towCar:
                    newState[x][y] = "."
                    if y-1 in range(6):
                        y-= 1
                    else:
                        break
                self.removeCar(towCar)
            newBoard = Gameboard(self.carFuel,self.carOrientation, newState)
            self.children = newBoard

    def getHorizontalCoordinates(self,c):
        for i in range(6):
            for j in range(6):
                if self.state[i][j] == c:
                    startCoord = [i,j]
                    if j+1 in range(6):
                        tempj = j+1
                    while self.state[i][tempj] == c:
                        if tempj+1 in range(6):
                            tempj+=1
                        else:
                            break
                    endCoord = [i,tempj-1]
        return [startCoord,endCoord]

    def getVerticalCoordinates(self,c):
        for i in range(6):
            for j in range(6):
                if self.state[i][j] == c:
                    startCoord = [i,j]
                    if i+1 in range(6):
                        tempi = i+1
                        while self.state[tempi][j] == c:
                            if tempi+1 in range(6):
                                tempi+=1
                            else:
                                break
                        endCoord = [tempi,j]
        return [startCoord,endCoord]