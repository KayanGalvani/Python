#Desenvolva duas classes: Computador e SistemaOperacional.

    #A classe SistemaOperacional deve possuir os atributos: nome (ex: Windows, Linux, MacOS) e versao.
    #A classe Computador deve possuir um atributo chamado sistema, que será uma instância da classe SistemaOperacional

class SistemaOperacional:
    def __init__(self, nome, versao):
        self.nome = nome
        self.versao = versao

class Computador:
    def __init__(self, sistema):
        self.sistema = sistema

sistemaLinux = SistemaOperacional("Linux", "Ubutun")

meuComputador = Computador(sistemaLinux)

print("Meu computador está usando o sistema operacional", meuComputador.sistema.nome)
print("Versão:", meuComputador.sistema.versao)