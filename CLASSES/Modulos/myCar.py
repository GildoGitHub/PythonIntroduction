import ElecricCaro as eCar

myNewCar = eCar.Electrico(make="Yamaha",model="S23",year=2001,odemeterReading=24,bateria=40)

print(myNewCar.getDescriptiveName())
myNewCar.updateOdometer(34)
print(myNewCar.getBaterryInfo())
