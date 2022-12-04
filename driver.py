from queue import PriorityQueue
from car import Car
from gameboard import Gameboard
import re
import heapq
from heuristics import Heuristics
from search import UCS, Greedy, ASTAR

# ========================HELPER METHODS========================= 

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
                    if(1+j in range(6)):
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


# =========================SEARCH ALGORITHMS(TO-REMOVE)======================= 

def testucs(root): 
    queue = PriorityQueue()
    queue.put((0, [root]))
    # iterate over the items in the queue
    while not queue.empty():
        # get the highest priority item
        pair = queue.get()
        current = pair[1][-1]

        # if it's the goal, return
        if current.state[2][5] == 'A':
            return pair[1]
        # add all the edges to the priority queue
        for edge in current.children:
            # create a new path with the node from the edge
            new_path = list(pair[1])
            new_path.append(edge.board)
            # append the new path to the queue with the edges priority
            queue.put((pair[0] + edge.cost, new_path))
    return None

def testbfs(root):

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

def testgreedy(root):
    frontier = PriorityQueue()
    frontier.put(root, 0)
    came_from = dict()
    cost_so_far = dict()
    came_from[root] = None
    cost_so_far[root] = 0

    while not frontier.empty():
        current = frontier.get()

        if current.state[2][5] == 'A':
            path = []
            for key in came_from:
                path.append(came_from[key])
            
            return path
            break
        
        for next in current.children:
            new_cost = cost_so_far[current] + next.cost
            if next not in cost_so_far or new_cost < cost_so_far[next]:
                cost_so_far[next.board] = new_cost
                priority = new_cost+h1(next.board.state)
                frontier.put(next.board, priority)
                came_from[next.board] = current



# ///////////////////////////////MAIN///////////////////////////////////////////

def main():
    # input = "..I...BBI.K.GHAAKLGHDDKLG..JEEFF.J.."
    # input = "BBIJ....IJCC..IAAMGDDK.MGH.KL.GHFFL."
    # input = "...............AA..................."
    # input = "IJBBCCIJDDL.IJAAL.EEK.L...KFF..GGHH. F0 G6"
    # input = "IIB...C.BHHHC.AAD.....D.EEGGGF.....F"
    # input = "BB.G.HE..G.HEAAG.I..FCCIDDF..I..F..."
    # input = "JBBCCCJDD..MJAAL.MFFKL.N..KGGN.HH..."
    filename = 'C:\\Users\\Krish\\.vscode\\472-MP2\\Input\\50_puzzles.txt'
    input = []
    puzzlenum = []
    with open(filename) as file:
        while (line := file.readline().rstrip()):
            if line[0]=="#":
                puzzlenum.append(line[1])
                continue
            else:
                input.append(line)
    #print(len(input))

    # place input string in multidim array (6x6)
    for puzzle in input:
        input_array = parsePuzzle(puzzle)
        printBoard(input_array)


        # read the array and create car objects, setting them up in a list
        cars_dict = createCars(input_array)

        # create dictionnaries for root board
        carFuel = createFuelDict(puzzle)
        carOrientation =createOrientationDict(cars_dict)
        print(carFuel)
        print(carOrientation)


        board = Gameboard(carFuel,carOrientation,input_array)
        board.createGraph()
       



        # TESTING SEARCH ALGOS

        print("------------------")

        answer1, answer2 = ASTAR.astar(board, 'h4')
        print((answer1))
        print(answer2)

        print("------------------")

        # for j in answer1:
        #     printBoard(j.state)
        #     print(" ")

if __name__=="__main__":
    main()

