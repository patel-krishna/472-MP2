# from car import Car
#TODO: fix move not moving properly
#TODO: fix the identical grandparent loop
#TODO: Add nodes for each move possible (one for each empty space)
#TODO: figure out why only H is moving
from copy import deepcopy

from sys import exit
from queue import PriorityQueue
visited_boards = []


class Gameboard(object):
    def __init__(self, carFuel, carOrientation, state):
        self.carFuel = carFuel
        self.carOrientation = carOrientation
        self.children = []
        self.state = state

    def createGraph(self):
        print("Current Board:")
        for i in range(6):
            for j in range(6):
                print(self.state[i][j], end=" ")
            print("")
        if self.state[2][5]=="A":
            print("Win")
            return True
            #exit("Win")
        moved = False
        if self.checkFuel():
            print("Current Board:")
            for i in range(6):
                for j in range(6):
                    print(self.state[i][j], end=" ")
                print("")
            for c in self.carFuel:
                if self.carOrientation.get(c) == "h":
                    print("CHECKING ALL POSSIBLE MOVES FOR CURRENT CAR " + c)
                    hcoords = self.getHorizontalCoordinates(c)
                    if len(hcoords) >0:
                        startCoord = hcoords[0]
                        endCoord = hcoords[-1]
                        row = startCoord[0]
                        column = startCoord[1]
                        #check left
                        if self.carFuel.get(c)>0:
                            count = 1
                            while column-1 in range(6) and self.state[row][column-1] == ".":
                                self.moveCarLeft(c,hcoords,count)
                                moved = True
                                column-=1
                                count+=1

                        row = endCoord[0]
                        column = endCoord[1]
                        #check right
                        if self.carFuel.get(c) != None:
                            if self.carFuel.get(c)>0:
                                count=1
                                while column+1 in range(6) and self.state[row][column+1] == ".":
                                    self.moveCarRight(c,hcoords,count)
                                    moved = True
                                    column+=1
                                    count+=1

                elif self.carOrientation.get(c) == "v":
                    print("CHECKING ALL POSSIBLE MOVES FOR CURRENT CAR " + c)
                    vcoords = self.getVerticalCoordinates(c)
                    startCoord = vcoords[0]
                    endCoord = vcoords[-1]
                    row = startCoord[0]
                    column = startCoord[1]
                    #check up
                    if self.carFuel.get(c)>0:
                        count=1
                        while row-1 in range(6) and self.state[row-1][column]==".":
                            self.moveCarUp(c, vcoords, count)
                            moved=True
                            row -= 1
                            count+=1
                        row = endCoord[0]
                        column = endCoord[1]
                    #check down
                    if self.carFuel.get(c)>0:
                        count = 1
                        while row+1 in range(6) and self.state[row+1][column] == ".":
                            self.moveCarDown(c,vcoords, count)
                            moved = True
                            row+=1
                            count+=1
                # if not moved:
                #     print("no solution")
                #     return False
        else:
            return "no solution"
        for a in self.children:
            win = a.board.createGraph()
            if win:
                return True

    def carAtExit(self,coords):
        for c in coords:
            if c[0]==2 and c[1]==5:
                print("Car at exit")
                return True
        return False

    def checkVisited(self, newstate):
        for v in visited_boards:
            if newstate == v:
                return True
        return False

    def removeCar(self,car):
        print("Car erased:")
        print(car)
        #self.carFuel.pop(car)

    def checkFuel(self):
        fuelLeft = False
        for c in self.carFuel:
            if self.carFuel.get(c)>0:
                fuelLeft = True
        return fuelLeft

    def moveCarUp(self, c,coords, increment):
        newState = deepcopy(self.state)
        for i in coords:
            newState[i[0]][i[1]]= "."
            newState[i[0]-increment][i[1]] = c
        self.carFuel[c] = self.carFuel.get(c) -1
        if self.checkVisited(newState):
            return None
        else:
            visited_boards.append(newState)
            newBoard = Gameboard(self.carFuel,self.carOrientation, newState)
            self.add_child(newBoard)

    def moveCarDown(self,c,coords,increment):
        newState = deepcopy(self.state)
        for i in reversed(coords):
            newState[i[0]][i[1]]= "."
            newState[i[0]+increment][i[1]] = c
        self.carFuel[c] = self.carFuel.get(c) -1
        if self.checkVisited(newState):
            return None
        else:
            visited_boards.append(newState)
            newBoard = Gameboard(self.carFuel,self.carOrientation, newState)
            self.add_child(newBoard)

    def moveCarLeft(self, c, coords, increment):
        newState = deepcopy(self.state)
        carPosition = self.carAtExit(coords)
        if carPosition:
            x=2
            y=5
            towCar = newState[x][y]
            print("CAR TO TOW")
            print(towCar)
            if towCar != "A":
                while newState[x][y] == towCar:
                    print("towing" + towCar)
                    print(newState[x][y])
                    newState[x][y] = "."
                    if y-1 in range(6):
                        y-= 1
                    else:
                        break
                self.removeCar(towCar)
        else:
            for i in coords:
                newState[i[0]][i[1]] = "."
                newState[i[0]][i[1]-increment] = c
            self.carFuel[c] = self.carFuel.get(c) -1

        if self.checkVisited(newState):
            return None
        else:
            visited_boards.append(newState)
            newBoard = Gameboard(self.carFuel,self.carOrientation, newState)
            self.add_child(newBoard)


    def moveCarRight(self,c,coords, increment):
        newState = deepcopy(self.state)
        for i in reversed(coords):
            newState[i[0]][i[1]] = "."
            newState[i[0]][i[1]+increment] = c
        self.carFuel[c] = self.carFuel.get(c) -1
        carPosition = self.carAtExit(coords)
        if carPosition:
            x=2
            y=5
            towCar = newState[x][y]
            print("Car to TOW:" + towCar)
            # if towCar != "A":
            #     while newState[x][y] == towCar:
            #         print("towing" + towCar)
            #         newState[x][y] = "."
            #         if y-1 in range(6):
            #             y-= 1
            #         else:
            #             break
            #     self.removeCar(towCar)
        if self.checkVisited(newState):
            return None
        else:
            visited_boards.append(newState)
            newBoard = Gameboard(self.carFuel,self.carOrientation, newState)
            self.add_child(newBoard)

    def getHorizontalCoordinates(self,c):
        coords = []
        for i in range(6):
            for j in range(6):
                if self.state[i][j] == c:
                    coords.append([i,j])
                    if j+1 in range(6):
                        tempj = j+1
                        while self.state[i][tempj] == c:
                            if tempj+1 in range(6):
                                tempj+=1
                            else:
                                break
        return coords

    def getVerticalCoordinates(self,c):
        coords = []
        for i in range(6):
            for j in range(6):
                if self.state[i][j] == c:
                    coords.append([i,j])
                    if i+1 in range(6):
                        tempi = i+1
                        while self.state[tempi][j] == c:
                            if tempi+1 in range(6):
                                tempi+=1
                            else:
                                break
        return coords

    def add_child(self, newBoard, cost=1):
        child = Child(self, newBoard, cost)
        self.children.append(child)

    def __lt__(self,other):
        """
        Perform the less than operation (self < other).
        
        Args:
            other: the other Node to compare to
        """
        return (self.state < other.state)

    def __gt__(self,other):
        """
        Perform the greater than operation (self > other).
        
        Args:
            other: the other Node to compare to
        """
        return (self.state > other.state)


class Child(object):

    def __init__(self, parent: Gameboard, board: Gameboard, cost: int=1):
        """
        Initialize a new child.

        Args:
            parent: parent of the child
            board: the current board of the child
            cost: the cost of the edge (default 1)
        """

        self.parent = parent
        self.board = board
        self.cost = cost
    
    def setCost(self, int):
        self.cost = int