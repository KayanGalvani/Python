#   Crie uma classe chamada Veiculo que possua atributos para cor e preco. A classe deve também possuir um método chamado detalhes que retorna uma string contendo a cor e o preço do veículo.
#   A partir desta classe base, derive duas subclasses: Carro e Bicicleta.

    #   Para a classe Carro, adicione um atributo para numero_portas.
    #   Para a classe Bicicleta, adicione um atributo para tipo (por exemplo, "montanha" ou "estrada").

#   Ambas as subclasses devem sobrescrever o método detalhes para incluir suas características adicionais.

class Veiculo:
    def __init__(self, cor, preco):
        self.cor = cor
        self.preco = preco

    def detalhes(self):
        return f"Cor: {self.cor}, Preço: R${self.preco:.2f}"

class Carro(Veiculo):
    def __init__(self, cor, preco, numero_portas):
        super().__init__(cor, preco)
        self.numero_portas = numero_portas

    def detalhes(self):
        detalhes_veiculo = super().detalhes()
        return f"{detalhes_veiculo}, Número de Portas: {self.numero_portas}"

class Bicicleta(Veiculo):
    def __init__(self, cor, preco, tipo):
        super().__init__(cor, preco)
        self.tipo = tipo

    def detalhes(self):
        detalhes_veiculo = super().detalhes()
        return f"{detalhes_veiculo}, Tipo: {self.tipo}"

# Exemplo de uso
carro = Carro("Vermelho", 30000.0, 4)
bicicleta = Bicicleta("Azul", 1000.0, "Montanha")

print(carro.detalhes())
print(bicicleta.detalhes())