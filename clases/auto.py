from clases.vehiculo import Vehículo

class Auto(Vehículo):
    def __init__(self, marca=None, modelo=None, color=None, numero_puertas=None, numero_pasajeros=None):
        super().__init__(marca, modelo, color)
        self._numero_puertas = None
        self._numero_pasajeros = None
        self.set_numero_puertas(numero_puertas)
        self.set_numero_pasajeros(numero_pasajeros)

    def set_numero_puertas(self, numero_puertas):
        if numero_puertas is not None:
            self._numero_puertas = numero_puertas

    def set_numero_pasajeros(self, numero_pasajeros):
        if numero_pasajeros is not None:
            self._numero_pasajeros = numero_pasajeros

    def get_numero_puertas(self):
        return self._numero_puertas

    def get_numero_pasajeros(self):
        return self._numero_pasajeros

    def imprimirAuto(self):
        if self.validarAuto():
            return f"{super().imprimir()} | Puertas: {self.get_numero_puertas()} | Pasajeros: {self.get_numero_pasajeros()}"
        return ""

    def validarAuto(self):
        return self.get_numero_puertas() is not None and self.get_numero_pasajeros() is not None

    def ruido(self):
        print("RRRRR")
