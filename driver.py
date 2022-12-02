from car import Car
from gameboard import Gameboard
import re

# Helper methods 

def parsePuzzle(input):
    """ check that the string is exactly of 36 characters
        and there is an ambulance """
    if ("A" not in input):
        print('Puzzle is not valid')
        return
    else:
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

# given the puzzle, set the fuel dictionnary 
def setFuel(input):
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


# Read input string, for now, 
# lets work with a string, we can establish io later
#input = "..I...BBI.K.GHAAKLGHDDKLG..JEEFF.J.."
#input = "BBIJ....IJCC..IAAMGDDK.MGH.KL.GHFFL."
input = "...............AA..................."
if len(input)>36 or len(input)<36:
    print('Input is wrong')
else:
    print("Input is valid")

# place input string in multidim array (6x6)
input_array = []

counter =0
while counter <36:
    temp_columns =[]
    for i in range(6): 
        temp_columns.append(input[counter])
        counter=counter+1
    input_array.append(temp_columns)

for i in range(6):
    for j in range(6):
        print(input_array[i][j], end=" ")
    print("")



# read the array and create car objects, setting them up in a list



cars_list = []
cars_dict = {}



# for i in range(6):
#     for j in range(6):
#         if input_array[i][j] != ".":
#             if len(cars_list) ==0:
#                 temp_obj=Car(input_array[i][j],(i,j),0,100)
#                 cars_list.append(temp_obj)
#             else:  
#                 for c in cars_list:
#                     if input_array[i][j] == c.name:
#                         c.set_coord(i,j)
#                         pass
#                     else:
#                         temp_obj=Car(input_array[i][j],(i,j),0,100)
#                         cars_list.append(temp_obj)
#                         break
        
for i in range(6):
    for j in range(6):
        if input_array[i][j] != ".":
            if len(cars_dict) ==0:
                if input_array[i][j+1] == input_array[i][j]:
                    temp_obj=Car(input_array[i][j],(i,j),100, "h")
                    cars_dict.update({input_array[i][j]: temp_obj})
                else:
                    temp_obj=Car(input_array[i][j],(i,j),100, "v")
                    cars_dict.update({input_array[i][j]: temp_obj})
            else:
                if input_array[i][j] in cars_dict:
                      x=cars_dict.get(input_array[i][j])
                      x.update_coord(i,j)
                else:
                    if j+1 in range(6):
                        if input_array[i][j+1] == input_array[i][j]:
                            temp_obj=Car(input_array[i][j],(i,j),100, "h")
                            cars_dict.update({input_array[i][j]: temp_obj})
                        else:
                            temp_obj=Car(input_array[i][j],(i,j),100, "v")
                            cars_dict.update({input_array[i][j]: temp_obj})
                    else:
                        temp_obj=Car(input_array[i][j],(i,j),100, "v")
                        cars_dict.update({input_array[i][j]: temp_obj})


carFuel = {}
carOrientation ={}
                
for x in cars_dict.values():
    carFuel[x.name] = x.fuel
    carOrientation[x.name] = x.orientation


# board = Gameboard(carFuel,carOrientation,input_array)
# board.createGraph()
# for k in range(len(cars_list)):
#     print(cars_list[k])

string = "IJBBCCIJDDL.IJAAL.EEK.L...KFF..GGHH. F0 G6"
carFuelTest2  = setFuel(string)

print(carFuelTest2)
