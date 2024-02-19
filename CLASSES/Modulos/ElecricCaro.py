import car

class Electrico(car.Car):

    def __init__(self, make, model,bateria, year, odemeterReading=0) -> None:
        super().__init__(make, model, year, odemeterReading)
        self.bateria = bateria
        pass

    def getBaterryInfo(self):
        return "YOUR BATERRY IS "+str(self.bateria)
    
    pass
