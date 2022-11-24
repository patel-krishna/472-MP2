class Car(object): 

    # carsList = []
<<<<<<< Updated upstream
    def __init__(self, name, coordinates, position, fuel,orientation):
=======
    def __init__(self, name, coordinates, fuel,orientation):
>>>>>>> Stashed changes
        self.name = name
        self.coordinates = [coordinates]
        self.fuel = fuel
        self.orientation = orientation
        # Car.carsList.append(self)

    def __str__(self): 
        return f"{self.name}{self.coordinates}"

<<<<<<< Updated upstream
    def set_coord(self,x, y):
        self.coordinates.append((x,y))

    def move(self, direction, spaces):
        if self.fuel < spaces:
            print("not enough fuel to move")
        else:
            #check if direction is valid
            if direction == "right" or direction == "left" and self.orientation == "h":
                print()
            elif direction == "down" or direction == "up" and self.orientation == "v":
                print()
            else:
                print("invalid move")
=======
    def update_coord(self,x, y):
        self.coordinates.append((x,y))

    def adjust_coord(self,direction):
        if direction=="left":
            for coord in self.coordinates:
                coord[1] = coord[1]-1
        if direction=="right":
            for coord in self.coordinates:
                coord[1] = coord[1]+1
        if direction=="up":
            for coord in self.coordinates:
                coord[0] = coord[0]-1
        if direction=="down":
            for coord in self.coordinates:
                coord[0] = coord[0]+1

>>>>>>> Stashed changes
