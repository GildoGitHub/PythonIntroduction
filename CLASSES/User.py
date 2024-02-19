class User():

    def __init__(self, firstName, lastName,**other) -> None:
        self.firstName = firstName
        self.lastName = lastName
        self.other = other
        self.login_attemps = 0
        pass

    def describeUser(self):
        print("My first name is "+self.firstName+" and my last is "+self.lastName)
        print("\n\tSEE MY OTHER INFORMATION FOLLOWING")
        for key,value in self.other.items():
            print("\t"+key+" "+str(value))
        pass

    def incrimentLoginAttemps(self):
        self.login_attemps+=1
        pass

    def resetAttemps(self):
        self.login_attemps = 0
        pass
    pass

class Admin(User):

    def __init__(self, firstName, lastName, **other) -> None:
        super().__init__(firstName, lastName, **other)
        self.privileges = Privileges()
        pass
    
    pass

class Privileges():

    def __init__(self,privileges=["Can add a post","Can delete post","Can bun a user"]) -> None:
        self.privileges = privileges
        pass
    
    def showPriviges(self):
        return self.privileges

    pass

adm = Admin("Gildo","Cumbane",age=13,favoritFood="Matapa")

print("\nI AM AN ADMIN, AND I HAVE THESE PRIVILEGES")

for privelege in adm.privileges.showPriviges():
    print(privelege.title())
