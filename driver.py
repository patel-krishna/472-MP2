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



# read multidimensional array by row and create horizontal cars
# read md array by column and create vertical cars 



cars_list = []

for i in range(6):
    for j in range(6):
        if input_array[i][j] != ".":
            for c in Car.carsList:
                if input_array[i][j] == c.name:
                    c.set_coord(i,j)
                else:
                    Car(input_array[i][j],(i,j),0,100)

print(Car.carsList)


# place car on board