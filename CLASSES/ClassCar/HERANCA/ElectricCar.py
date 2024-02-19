import Car as carro
class ElectriCar(carro.Carro):

    def __init__(self, mark, model, year,bt) -> None:
        """INICIALIZA ATRIBUTOS DE UM CARRO ELECTRICO"""
        super().__init__(mark, model, year)
        self.baterria = bt
    pass

    def assuntoBt(self):
        self.baterria.descricaoBateria()