from queue import PriorityQueue
from car import Car
from gameboard import Gameboard
import re

# Helper methods 

def parsePuzzle(input):
    if ("A" in input):
        # the string is valid so take the puzzle and place it on a a 2D array
        array = []
        counter = 0
        while counter <36:
            temp_columns =[]
            for i in range(6):
                temp_columns.append(input[counter])
                counter=counter+1
            array.append(temp_columns)
        return array
    else:
        print("Puzzle is not valid, missing Ambulance")
        return

def printBoard(array):

    for i in range(6):
        for j in range(6):
            print(array[i][j], end=" ")
        print("")


# given the puzzle string, set the fuel dictionnary 
def createFuelDict(input):
    carFuel = {}
    tempCar= re.sub('[^a-zA-Z]+', '', input)
    carName = list(set(tempCar))
    if len(input) >= 36:
       for i in range (len(carName)):
            for k in carName:
                carFuel[k] = carFuel.setdefault(k, 100)
    if len(input)>36:
        temp = input[37:len(input)]
        for i in range(len(temp)-1):
            if(temp[i] != " " and temp[i+1].isnumeric()):
                carFuel.update({temp[i]: int(temp[i+1])})
                i=i+1
            else: 
                pass

    return carFuel
       
# given a 2D array, create a dictionary of cars with the initial puzzle
def createCars(array):
    cars_dict = {}
    for i in range(6):
        for j in range(6):
            if array[i][j] != ".":
                if len(cars_dict) ==0:
                    if array[i][j+1] == array[i][j]:
                        temp_obj=Car(array[i][j],(i,j),100, "h")
                        cars_dict.update({array[i][j]: temp_obj})
                    else:
                        temp_obj=Car(array[i][j],(i,j),100, "v")
                        cars_dict.update({array[i][j]: temp_obj})
                else:
                    if array[i][j] in cars_dict:
                          x=cars_dict.get(array[i][j])
                          x.update_coord(i,j)
                    else:
                        if j+1 in range(6):
                            if array[i][j+1] == array[i][j]:
                                temp_obj=Car(array[i][j],(i,j),100, "h")
                                cars_dict.update({array[i][j]: temp_obj})
                            else:
                                temp_obj=Car(array[i][j],(i,j),100, "v")
                                cars_dict.update({array[i][j]: temp_obj})
                        else:
                            temp_obj=Car(array[i][j],(i,j),100, "v")
                            cars_dict.update({array[i][j]: temp_obj})
    return cars_dict

# def createFuelDict(cars_dict):
#     carFuel = {}
#     for x in cars_dict.values():
#         carFuel[x.name] = x.fuel
#     return carFuel

# given a dictionnary of cars, create a dictionnary of the orientation of cars 
def createOrientationDict(cars_dict):
    carOrientation = {}
    for x in cars_dict.values():
        carOrientation[x.name] = x.orientation
    return carOrientation


# SEARCH ALGORITHMS 

def ucs(root): 
    queue = PriorityQueue()
    queue.put((0, [root]))
    # iterate over the items in the queue
    while not queue.empty():
        # get the highest priority item
        pair = queue.get()
        current = pair[1][-1]
        # if it's the goal, return
        if current.state[3][5] == 'A':
            return pair[1]
        # add all the edges to the priority queue
        for edge in current.children:
            # create a new path with the node from the edge
            new_path = list(pair[1])
            new_path.append(edge.destination)
            # append the new path to the queue with the edges priority
            queue.put((pair[0] + edge.cost, new_path))

def bfs(root):
    return 

# Read input string, for now, 
# lets work with a string, we can establish io later


#input = "..I...BBI.K.GHAAKLGHDDKLG..JEEFF.J.."
#input = "BBIJ....IJCC..IAAMGDDK.MGH.KL.GHFFL."
#input = "...............AA..................."
input = "..............AABB.................."
#input = "IJBBCCIJDDL.IJAAL.EEK.L...KFF..GGHH. F0 G6"


# place input string in multidim array (6x6)
input_array = parsePuzzle(input)
printBoard(input_array)


# read the array and create car objects, setting them up in a list
cars_dict = createCars(input_array)

# create dictionnaries for root board
carFuel = createFuelDict(input)
carOrientation =createOrientationDict(cars_dict)
print(carFuel)
print(carOrientation)


board = Gameboard(carFuel,carOrientation,input_array)
board.createGraph()
# for k in range(len(cars_list)):
#     print(cars_list[k])

# string = "IJBBCCIJDDL.IJAAL.EEK.L...KFF..GGHH. F0 G6"

