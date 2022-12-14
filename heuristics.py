class Heuristics:
# method that checks how many cars are blocking the ambulance 
# returns a string 
    def h1(array):
        counter = 0
        setCars= set()
        for i in range(2,6):
            if array[2][i] != "A":
                if array[2][i] not in setCars:
                    setCars.add(array[2][i])
                    counter=+1
        return counter

    # method that checks for blocked positions aka h2
    def h2(array):
        counter = 0
        for i in range(2,6):
            if array[2][i] != 'A' and array[2][i] != ".":
                counter=+1
        return counter

    # method that returns the the h1 heuristics multiplied by lambda 
    def h3(array,int=5):
        temp = Heuristics.h1(array)
        return (int*temp)

# TODO: heuristic 4: how many elements are in the last column, if last column is empty h4(n) = 0
    def h4(array):
        counter = 0
        for i in range (0, 6):
            if array[5][i] != 'A':
                counter +=1
        return counter 


