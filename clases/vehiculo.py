class Vehículo:
    def __init__(self, marca=None, modelo=None, color=None):
        self._marca = None
        self._modelo = None
        self._color = None
        self.set_marca(marca)
        self.set_modelo(modelo)
        self.set_color(color)

    def set_marca(self, marca):
        if marca is not None:
            self._marca = marca

    def set_modelo(self, modelo):
        if modelo is not None:
            self._modelo = modelo

    def set_color(self, color):
        if color is not None:
            self._color = color

    def get_marca(self):
        return self._marca

    def get_modelo(self):
        return self._modelo

    def get_color(self):
        return self._color

    def imprimir(self):
        return f"Marca: {self.get_marca()} | Modelo: {self.get_modelo()} | Color: {self.get_color()}"

    def ruido(self):
        print("Ruido genérico")
