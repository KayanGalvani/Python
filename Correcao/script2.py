class Estudante:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def apresentar(self):
        mensagem = f"Nome: {self.nome}, Idade: {self.idade} anos"
        return mensagem

estudante1 = Estudante("Kayan", 19)
estudante2 = Estudante("Kaue", 20)
estudante3 = Estudante("Dieimes", 67)

print(estudante1.apresentar())
print(estudante2.apresentar())
print(estudante3.apresentar())