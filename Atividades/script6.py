#   Definir o conceito de composição.
#   Criar dois exemplos práticos usando Python que demonstrem a aplicação da composição.

class Motor:
    def start(self):
        print("Motor ligado")

    def stop(self):
        print("Motor desligado")

class Roda:
    def roll(self):
        print("Roda girando")

class Carro:
    def __init__(self):
        self.motor = Motor()
        self.roda1 = Roda()
        self.roda2 = Roda()
        self.roda3 = Roda()
        self.roda4 = Roda()

    def drive(self):
        self.motor.start()
        self.roda1.roll()
        self.roda2.roll()
        self.roda3.roll()
        self.roda4.roll()
        self.motor.stop()

meu_carro = Carro()
meu_carro.drive()