#"Polimorfismo" siempre va a mandar a llamar la función
from clases.vehiculo import Vehículo
class Moto(Vehículo):
    def __init__(self, marca=None, modelo=None, color=None):
        super().__init__(marca, modelo, color)
    def ruido(self):
        print("RRRRR")
        