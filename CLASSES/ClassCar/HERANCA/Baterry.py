class Baterry():
    """ESTA CLASSE REPRESENTA ALGUMAS BATERIAS DE UM CARRO ELECTRICO"""

    def __init__(self,batterySize,fabrico) -> None:
        self.batterySize=batterySize
        self.fabrico=fabrico
        pass

    def descricaoBateria(self):
        """EXIBE INFORMACOES SOBRE A BATERRIA"""
        return "Bateria da marca "+self.fabrico+" com capacidade "+str(self.batterySize)
pass