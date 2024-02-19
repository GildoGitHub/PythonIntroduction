class Restaurant():
    """This class creat and discribe a restaurant!"""

    def __init__(self, restaurantName, cuisineType) -> None:
        """This method init a class restaurant"""
        self.restaurantName = restaurantName
        self.cuisineType = cuisineType
        pass
    
    def describeRestaurant(self):
        """This method describe a restaurant"""
        print("My restarant name is "+self.restaurantName+" and his cuisine type is "+self.cuisineType)
        pass

    def openRestaurant(self):
        """This method tell us if the restaurant is open or closed"""
        print("THE RESTAURANT IS OPEN")
        pass