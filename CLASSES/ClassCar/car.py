class Car():
    """Uma Tentaiva simples de representar um carro"""

    def __init__(self,make, model, year) -> None:
        """Inicializa os atributos que descrevem um carro"""
        self.make = make 
        self.model = model
        self.year = year
        self.odemeter = 0
        pass

    def getDescriptName(self):
        return str(self.year)+' '+self.make+' '+self.model+' '+str(self.odemeter)
    
    def readOdometer(self):
        """Esse método exibe uma milhagem do carro"""
        print("This car has "+str(self.odemeter)+" miles in on it")
    
    def updateOdemeter(self,miliage):
        """Define o valor de leitura de hôdometro com o valor especificado."""
        if miliage > self.odemeter:
            self.odemeter = miliage
        else:
            print("Coloca um valor maior que "+str(self.odemeter))

    pass

newCar = Car(make="TOYOTA",year=2013,model='A32')

newCar.updateOdemeter(29)
print(newCar.getDescriptName())
newCar.readOdometer()

newCar.updateOdemeter(29.9)
print(newCar.getDescriptName())
newCar.readOdometer()

