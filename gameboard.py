from car import Car
from copy import deepcopy


class Gameboard(object):
    def __init__(self, carFuel, carOrientation, state):
        self.carFuel = carFuel
        self.carOrientation = carOrientation
        self.children = None
        self.state = state

    #move should only move 1
    #we should have other methods that call move, that create graph
    #TODO: add board each for empty space next to car
    #TODO: add base cases (win condition, out of fuel, no solution )
    def move(self):
        for c in self.carFuel:
            if self.carOrientation.get(c.keys()) == "h":
                for i in range(6):
                    for j in range(6):
                        if self.state[i][j] == c.keys():
                            startCoord = [i,j]
                            tempj = j+1
                            while(self.state[i][tempj] == c.keys()):
                                tempj+=1
                            endCoord = [i,tempj-1]
                row = startCoord[0]
                column = startCoord[1]
                #check left
                if c.values() >0:
                    if column -1 in range(6):
                        if self.state[row][column-1] == ".":
                            newState = deepcopy(self.state)
                            newState[row][column-1] = c.keys()
                            newState[endCoord[0]][endCoord[1]] = "."
                            self.carFuel[c.keys()] = c.values() -1
                            newBoard = Gameboard(self.carFuel,self.carOrientation, newState)
                            self.children = newBoard
                        else:
                            continue
                #check right
                row = endCoord[0]
                column = endCoord[1]
                if c.values() >0:
                    if column +1 in range(6):
                        if self.state[row][column+1] == ".":
                            newState = deepcopy(self.state)
                            newState[row][column+1] = c.keys()
                            newState[startCoord[0]][startCoord[1]] = "."
                            self.carFuel[c.keys()] = c.values() -1
                            newBoard = Gameboard(self.carFuel,self.carOrientation, newState)
                            self.children = newBoard
                        else:
                            continue
            elif self.carOrientation.get(c.keys()) == "v":
                for i in range(6):
                    for j in range(6):
                        if self.state[i][j] == c.keys():
                            startCoord = [i,j]
                            tempi = i+1
                            while(self.state[tempi][j] == c.keys()):
                                tempi+=1
                            endCoord = [tempi,j]
                row = startCoord[0]
                column = startCoord[1]
                #check up
                if c.values() >0:
                    if row-1 in range(6):
                        if self.state[row-1][column] == ".":
                            newState = deepcopy(self.state)
                            newState[row-1][column] = c.keys()
                            newState[endCoord[0]][endCoord[1]] = "."
                            self.carFuel[c.keys()] = c.values() -1
                            newBoard = Gameboard(self.carFuel,self.carOrientation, newState)
                            self.children = newBoard
                        else:
                            continue
                #check down
                row = endCoord[0]
                column = endCoord[1]
                if c.values() >0:
                    if row+1 in range(6):
                        if self.state[row+1][column] == ".":
                            newState = deepcopy(self.state)
                            newState[row+1][column] = c.keys()
                            newState[endCoord[0]][endCoord[1]] = "."
                            self.carFuel[c.keys()] = c.values() -1
                            newBoard = Gameboard(self.carFuel,self.carOrientation, newState)
                            self.children = newBoard
                        else:
                            continue
