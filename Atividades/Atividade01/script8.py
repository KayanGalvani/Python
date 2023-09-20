#   Crie uma classe chamada Produto com os atributos nome e preco. A classe deve ter um método chamado desconto que aplica um desconto percentual ao preço do produto e retorna o preço com desconto. A partir da classe Produto, crie duas subclasses: Livro e Jogo.

#   Para a classe Livro, adicione o atributo autor e sobrescreva o método desconto para aplicar um desconto adicional de 10% (além do desconto geral do produto).

#   Para a classe Jogo, adicione o atributo plataforma (por exemplo, 'PC', 'PS5', etc.) e não modifique o método desconto.

class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def desconto(self, percentual):
        desconto = self.preco * (percentual / 100)
        preco_com_desconto = self.preco - desconto
        return preco_com_desconto

class Livro(Produto):
    def __init__(self, nome, preco, autor):
        super().__init__(nome, preco)
        self.autor = autor

    def desconto(self, percentual):
        preco_com_desconto = super().desconto(percentual)
        
        desconto_adicional = preco_com_desconto * 0.10
        preco_com_desconto -= desconto_adicional
        
        return preco_com_desconto

class Jogo(Produto):
    def __init__(self, nome, preco, plataforma):
        super().__init__(nome, preco)
        self.plataforma = plataforma

produto = Produto("Produto Genérico", 100)
livro = Livro("Livro Interessante", 50, "Autor Desconhecido")
jogo = Jogo("Jogo Divertido", 60, "PS5")

print(f"Produto com desconto: R${produto.desconto(20)}")

print(f"Livro com desconto: R${livro.desconto(15)}")

print(f"Jogo com desconto: R${jogo.desconto(10)}")