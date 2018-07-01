class Bike:
    def __init__(self, color, material):
        self.color = color
        self.material = material
    def brake(self):
        print("Braking")

redbike = Bike('red', 'fiber')
bluebike = Bike('blue','plastic')

bluebike.brake()
        
