from car import Car


# Read input string, for now, 
# lets work with a string, we can establish io later
input = "..I...BBI.K.GHAAKLGHDDKLG..JEEFF.J.."

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

for i in range(6):
    for j in range(6):
        if input_array[i][j] != ".":
            if len(cars_list) ==0:
                temp_obj=Car(input_array[i][j],(i,j),0,100)
                cars_list.append(temp_obj)
            else:  
                for c in cars_list:
                    if input_array[i][j] == c.name:
                        c.set_coord(i,j)
                        pass
                    else:
                        temp_obj=Car(input_array[i][j],(i,j),0,100)
                        cars_list.append(temp_obj)
                        continue
                        break
        
                
                
                

for k in range(len(cars_list)):
    print(cars_list[k])


# figure out the orientatiob of each car 
# once all objects have been set-up, place them on a 2d board

# create a goal board 
# UCS 

