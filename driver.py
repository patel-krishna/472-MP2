from car import Car
from gameboard import Gameboard

# Read input string, for now, 
# lets work with a string, we can establish io later
#input = "..I...BBI.K.GHAAKLGHDDKLG..JEEFF.J.."
input = "BBIJ....IJCC..IAAMGDDK.MGH.KL.GHFFL."
#input = "...............AA..................."
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


board = Gameboard(carFuel,carOrientation,input_array)
board.createGraph()
# for k in range(len(cars_list)):
#     print(cars_list[k])


# figure out the orientatiob of each car 
# once all objects have been set-up, place them on a 2d board

# create a goal board 
# UCS 
