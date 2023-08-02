from random import randint
class Persona:

    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido


class Cliente(Persona):

    def __init__(self,nombre, apellido, numero_cuenta, balance):
        self.numero_cuenta = numero_cuenta
        self.balance = balance
        super().__init__(nombre, apellido)

    def __str__(self):
        return f"El cliente {self.nombre} {self.apellido}. " \
               f"tiene {self.balance} € en la cuenta número {self.numero_cuenta} "

    def depositar(self, cantidad):
        self.balance = self.balance + cantidad

    def retirar(self, cantidad):
        if cantidad > self.balance:
            return -1
        else:
            self.balance = self.balance - cantidad
            return 1


def random_with_n_digits(n):
    range_start = 10**(n-1)
    range_end = (10**n)-1
    return randint(range_start, range_end)


def crear_cliente():
    print("Vamos a crear su cuenta de cliente. Proporcionenos los datos que le solicitemos a continuación")
    nombre = input("Indicanos cual es tu nombre: ")
    apellido = input("Ahora indicanos tus apellidos: ")
    cantidad = input("Por último dinos cual va ser tu primer ingreso al abrir la cuenta (Solo número): ")
    numero = random_with_n_digits(8)
    mi_cliente = Cliente(nombre, apellido, numero, int(cantidad))
    print("Los datos de su cliente son\n")
    print(mi_cliente)
    return mi_cliente

def inicio():

    mi_cliente = crear_cliente()
    finished = False

    while not finished:
        print("Elija que acción quiere hacer")
        print(" - 1. Ingresar dinero")
        print(" - 2. Retirar dinero")
        print(" - 3. Salir")
        opcion = input('Ingresa el número de la opción elegida: ')

        if opcion == '1':
            cantidad_ingreso = input("¿Que cantidad va depositar?: ")
            print(f'Depositamos {cantidad_ingreso}€')
            mi_cliente.depositar(int(cantidad_ingreso))
            print(mi_cliente)
            continue
        elif opcion == '2':
            cantidad_retirar = input("¿Que cantidad va retirar?: ")
            print(f'Retiramos {cantidad_retirar}€')
            if mi_cliente.retirar(int(cantidad_retirar)) == -1:
                print(f'La cuenta tiene {mi_cliente.balance} € no puede retirar {cantidad_retirar} €')
                continue
            else:
                print(mi_cliente)
                continue

        elif opcion == '3':
            finished = True
            print(' Gracias por usar nuestro banco, hasta pronto')


inicio()

