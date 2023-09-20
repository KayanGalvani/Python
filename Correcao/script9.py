#   Crie uma classe chamada ContaBancaria com os atributos titular e saldo. A classe deve ter dois métodos: depositar(valor) para adicionar um valor ao saldo e sacar(valor) para subtrair um valor do saldo.

#   A partir da classe ContaBancaria, crie duas subclasses: ContaPoupanca e ContaCorrente. Para a classe ContaPoupanca, sobrescreva o método sacar(valor) de modo que, a cada saque, seja descontada uma taxa de R$ 2.

#   Para a classe ContaCorrente, adicione um atributo limite e sobrescreva o método sacar(valor) de modo que o saque possa ser realizado mesmo que o saldo seja insuficiente, desde que não ultrapasse o limite definido.

class ContaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo

    def depositar(self, valor):
        self.saldo += valor

    def sacar(self, valor):
        if valor <= self.saldo:
            self.saldo -= valor
            return True
        else:
            return False

class ContaPoupanca(ContaBancaria):
    def sacar(self, valor):
        taxa = 2 
        if super().sacar(valor + taxa):
            return True
        else:
            return False

class ContaCorrente(ContaBancaria):
    def __init__(self, titular, saldo, limite):
        super().__init__(titular, saldo)
        self.limite = limite

    def sacar(self, valor):
        if valor <= (self.saldo + self.limite):
            if super().sacar(valor):
                return True
            else:
                return False
        else:
            return False

conta_poupanca = ContaPoupanca("João", 1000)
conta_corrente = ContaCorrente("Maria", 1500, 500)

print(f"Saldo da conta poupança: R${conta_poupanca.saldo}")
conta_poupanca.sacar(200)
print(f"Saldo após saque na conta poupança: R${conta_poupanca.saldo}")

print(f"Saldo da conta corrente: R${conta_corrente.saldo}")
conta_corrente.sacar(2000)
print(f"Saldo após saque na conta corrente: R${conta_corrente.saldo}")