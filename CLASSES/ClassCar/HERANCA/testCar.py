import ElectricCar as el
import Baterry as bt


beC1 = bt.Baterry(fabrico="Yunday",batterySize=50)
carro1 = el.ElectriCar(model="T5",mark="Nissan",year=2001,bt=beC1)
print(carro1.assuntoBt())