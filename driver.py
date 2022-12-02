from queue import PriorityQueue
from car import Car
from gameboard import Gameboard
import re
import heapq

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
                            temp_obj=Car(array[i][j], (i,j), 100, "v")
                            cars_dict.update({array[i][j]: temp_obj})
                            continue
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


# ================SEARCH ALGORITHMS======================= 

def ucs(root): 
    queue = PriorityQueue()
    queue.put((0, [root]))
    # iterate over the items in the queue
    while not queue.empty():
        # get the highest priority item
        pair = queue.get()
        print("pair " + str(pair))
        current = pair[1][-1]
        print("current")
        print(current) 
        # if it's the goal, return
        if current.state[2][5] == 'A':
            printBoard(pair[1])
            return pair[1]
        # add all the edges to the priority queue
        for edge in current.children:
            # create a new path with the node from the edge
            new_path = list(pair[1].state)
            print(pair[1])
            new_path.append(edge.board)
            printBoard(edge.board.state)
            # append the new path to the queue with the edges priority
            print(pair[0])
            print(edge.cost)
            queue.put((pair[0] + edge.cost, new_path))

def bfs(root):

    # track of visited nodes
    visited = set()  
    # BFS traversal result
    bfs_traversal = list()
    # queue
    queue = list()

    # push the root node to the queue and mark it as visited 
    queue.append(root)
    visited.add(root)

    # loop until queue empty 
    while queue: 
        # take the first board from the queue and add it to the traversal list
        current_node = queue.pop(0)
        bfs_traversal.append(current_node)

        # if the current board is in a winning state, then return the bfs traversale
        if current_node.state[2][5] == "A" and current_node.state[2][4] == "A" :
            return bfs_traversal
        # else, check the children of that node 
        else: 
            for children in current_node.children:
                # if the children node havent been visited yet
                # push them onto the queue and mark them as visited 
                if children.board not in visited:
                    visited.add(children.board)
                    queue.append(children.board)

# Dijkstra's algorithm 
def shortestPath(root):
    h = []

    heapq.heappush(h, (0, root))
    path = []
    while len(h) !=0:
        current_cost, current_node = heapq.heappop(h)
        path.append(current_node)
        if current_node.state[2][5] == "A" and current_node.state[2][4] == "A":
             return path
        else:
             for children in current_node.children:
                heapq.heappush(h, (current_cost+children.cost, children.board))


# -------------------------------------------------------------------------MAIN


# Read input string, for now, 
# lets work with a string, we can establish io later


#input = "..I...BBI.K.GHAAKLGHDDKLG..JEEFF.J.."
# input = "BBIJ....IJCC..IAAMGDDK.MGH.KL.GHFFL."
input = "...............AA..................."
# input = "IJBBCCIJDDL.IJAAL.EEK.L...KFF..GGHH. F0 G6"


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



# TESTING SEARCH ALGOS
# string = "IJBBCCIJDDL.IJAAL.EEK.L...KFF..GGHH. F0 G6"

print("------------------")

print(len(board.children))
answer = shortestPath(board)
print(len(answer))

print("--------")

for i in answer: 
    printBoard(i.state)
    print(" ")


