class Dog():
    """Uma tentativa simples de modelar um cachorro"""

    def __init__(self,name, age):
        """Inicializacao de atributos name e age."""
        self.name = name
        self.age = age
    
    def sit(self):
        """Simula um cachorro sentado em resposta a um comando"""
        print(self.name.title()+ " is now sitting.")
    
    def roll_over(self):
        """Simula um cachorro rolando em resposta a um comando"""
        print(self.name.title()+ " rolled over!")
    
my_dog = Dog('Dor',7)
yourDog = Dog('Maria',23)
print("My dog's name is "+my_dog.name.title()+" and he is "+str(my_dog.age)+" yeras old")
my_dog.sit()
my_dog.roll_over()
print()
print("Your dog's name is "+yourDog.name.title()+" and he is "+str(yourDog.age)+" yeras old")
yourDog.sit()
yourDog.roll_over()
