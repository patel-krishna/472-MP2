class Car(object): 

    # carsList = []
    def __init__(self, name, coordinates, fuel,orientation):
        self.name = name
        self.coordinates = [coordinates]
        self.fuel = fuel
        self.orientation = orientation
        # Car.carsList.append(self)

    def __str__(self): 
        return f"{self.name}{self.coordinates}"

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

