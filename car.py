class Car(object): 

    # carsList = []
    def __init__(self, name, coordinates, position, fuel):
        self.name = name
        self.coordinates = [coordinates]
        self.position = position
        self.fuel = fuel
        # Car.carsList.append(self)

    def __str__(self): 
        return f"{self.name}{self.coordinates}"

    def set_coord(self,x, y):
        self.coordinates.append((x,y))