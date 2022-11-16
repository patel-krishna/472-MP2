class Car(object): 

    # carsList = []
    def __init__(self, name, coordinates, position, fuel,orientation):
        self.name = name
        self.coordinates = [coordinates]
        self.position = position
        self.fuel = fuel
        self.orientation = orientation
        # Car.carsList.append(self)

    def __str__(self): 
        return f"{self.name}{self.coordinates}"

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