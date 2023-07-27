class Pajaro:
    alas = True

    def __init__(self, color, especie):
        self.color = color
        self.especie = especie

    def piar(self):
        print("pio")

    def volar(self, metros):
        print(f"El pajaro {self.especie} volo {metros} mts")


mi_pajaro = Pajaro('rojo', 'Tucan')

print(mi_pajaro.piar())
print(mi_pajaro.volar(25))
