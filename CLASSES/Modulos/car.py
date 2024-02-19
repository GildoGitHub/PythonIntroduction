class Car():

    def __init__(self,make,model,year,odemeterReading = 0) -> None:
        self.make = make
        self.model = model
        self.year = year
        self.odometro = odemeterReading
        pass

    def getDescriptiveName(self):
        name = self.make.upper()+" - "+self.model+" - "+str(self.odometro)
        return name
    
    def redOdemeter(self):
        return "O odometro ee "+str(self.odometro)
    
    def updateOdometer(self,addValue):
        if addValue>=0:
            self.odometro+=addValue
        else:
            print("You can not add negative or zero value")
        pass
    pass