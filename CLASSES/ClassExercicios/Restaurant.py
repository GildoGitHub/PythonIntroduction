class MyRestaurant():

    def __init__(self, restaurantName, cuisineType) -> None:
        """This method init a class restaurant"""
        self.restaurantName = restaurantName
        self.cuisineType = cuisineType
        self.numberServer = 20
        pass

    def showNumberServed(self):
        return self.numberServer
    
    def updateNumberServed(self, number):
        if number <= 0:
            print("Invalid number")
        else:
            self.numberServer+=number
        pass
    pass

class IceScreamStand(MyRestaurant):

    def __init__(self, restaurantName, cuisineType) -> None:
        super().__init__(restaurantName, cuisineType)
        self.flavores = ["Morango","Maca","Chocolate"]
        pass

    def showFlovers(self):
        return self.flavores
    pass

ic = IceScreamStand("GildoSorvets","ASX")

print("Lista de sabores de sorvetes da sorvetaria:")
for sabor in ic.showFlovers():
    print("   ",sabor.title())