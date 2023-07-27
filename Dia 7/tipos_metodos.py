class Pajaro:
    alas = True

    def __init__(self, color, especie):
        self.color = color
        self.especie = especie
    def piar(self):
        print("pio")

    def volar(self, metros):
        self.piar()
        print(f"El pajaro {self.especie} volo {metros} mts")

    def pintar_negro(self):
        self.color = "negro"
        print(f"Ahora el pajaro es {self.color}")

    @classmethod
    def poner_huevos(cls, cantidad):
        print(f"Puso {cantidad} huevos")
        cls.alas = False
        print(cls.alas)

    @staticmethod
    def mirar():
        print("Esta mirando a la derecha")


piolin = Pajaro('amarillo', 'Periquito')

print(piolin.piar())
print(piolin.volar(25))
print(piolin.pintar_negro())

piolin.alas = False
print(piolin.alas)

Pajaro.poner_huevos(4)
Pajaro.mirar()

