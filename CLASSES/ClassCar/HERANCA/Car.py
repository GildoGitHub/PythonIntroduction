class Carro():

    def __init__(self,mark,model,year) -> None:
        self.mark = mark
        self.model = model
        self.year = year
        pass

    def getDescricao(self):
        return self.mark+" "+self.model+" "+str(self.year)