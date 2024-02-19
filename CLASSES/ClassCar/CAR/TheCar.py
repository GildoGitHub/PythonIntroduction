class TheCar():
    """REPRESENTA UMA CLASSE QUE MODELA UM CARRO GERAL"""

    def __init__(self,mark,model,year) -> None:
        self.mark = mark
        self.model = model
        self.year = year
        self.odometro = 0
        pass

    def carDescription(self):
        return self.mark+" "+self.model+" "+str(self.year)
    
    def odometroDescription(self):
        return "The odometro is "+str(self.odometro)
    
    def updateOdometro(self,newValue):
        if(newValue>0):
            self.odometro+=newValue
        else:
            print("The value must to be posetive")
        pass

    def oilCapacity(self):
        return "A capacidade do oleo é "+str(20)
    
    pass

class Bateria():
    """Esta classe modela bateria de um carro electrico"""
    
    def __init__(self,baterrySize=100) -> None:
        self.baterrySize = baterrySize
        pass

    def describeBaterry(self):
        return "The car has a "+str(self.baterrySize)+" Kwh baterry"
    pass

class TheElectricCar(TheCar):
    """Esta classe modela um carro electrica"""

    def __init__(self, mark, model, year) -> None:
        super().__init__(mark, model, year)
        self.baterrySize=Bateria()
        pass
    pass

myTesla =  TheElectricCar("AAAA","Q3",2000)
print(myTesla.baterrySize.describeBaterry())