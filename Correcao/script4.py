#   Crie duas classes: Autor e Livro.

    #   A classe Autor deve possuir os atributos: nome e data_nascimento.
    #   A classe Livro deve ter os atributos: titulo e autor, onde autor será uma instância da classe Autor

class Autor:
    def __init__(self, nome, data_nascimento):
        self.nome = nome
        self.data_nascimento = data_nascimento

class Livro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor

autorName = Autor("Dieimes", "30 de julho de 2004")

livroPython = Livro("Livro Python", autorName)

print("Livro:", livroPython.titulo)
print("Autor:", livroPython.autor.nome)
print("Data de Nascimento do Autor:", livroPython.autor.data_nascimento)