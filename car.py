class Car: 

    def __init__(self, name, coordinates, position, fuel):
        self.name = name
        self.coordinates = coordinates
        self.position = position
        self.fuel = fuel

    def __str__(self): 
        return f"{self.name}"