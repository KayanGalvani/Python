#Elabore duas classes: Carro e Motor.

    #A classe Motor deve ter os atributos: tipo (ex: Gasolina, Diesel, Elétrico) e potencia (em cavalos).
    #A classe Carro deve possuir um atributo chamado motor, que será uma instância da classe Motor.

class Motor:
    def __init__(self, tipo, potencia):
        self.tipo = tipo
        self.potencia = potencia

class Carro:
    def __init__(self, motor):
        self.motor = motor

motorFlex = Motor("Motor Flex", 1000)

motorFlex = Carro(motorFlex)

# Acessando os atributos das instâncias
print("Tipo de motor:", motorFlex.motor.tipo)
print("Potência do motor:", motorFlex.motor.potencia, "cavalos")