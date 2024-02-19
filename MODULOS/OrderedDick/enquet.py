import collections as colec

class DicionarioEnquete():
    
    def run(self):
        pergutas = colec.OrderedDict()
        print()
        while True:
            name = input("Insert your name or N to stop enquet: ")

            if name.lower() != 'n':
                language = input("Insert your favority programing language: ")
                pergutas[name]=language
            else:
                break

            print()
            pass

        if pergutas:
            for key, value in pergutas.items():
                print("The",key.title()+"'s favorite language is",value.title())
        else:
            print("-----------Empty list-------------")
        pass

    pass