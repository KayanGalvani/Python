#   Crie uma classe chamada Documento que tenha os atributos titulo e conteudo e um método exibir que retorna uma representação do documento no formato: "Título: [título], Conteúdo: [conteúdo]". A partir dessa classe, crie duas subclasses: Email e Relatorio.

#   Para a classe Email, adicione os atributos remetente e destinatario, e sobrescreva o método exibir para incluir essas informações adicionais.

#   Para a classe Relatorio, adicione um atributo data e também sobrescreva o método exibir para exibir essa informação.


class Documento:
    def __init__(self, titulo, conteudo):
        self.titulo = titulo
        self.conteudo = conteudo

    def exibir(self):
        return f"Título: {self.titulo}, Conteúdo: {self.conteudo}"

class Email(Documento):
    def __init__(self, titulo, conteudo, remetente, destinatario):
        super().__init__(titulo, conteudo)
        self.remetente = remetente
        self.destinatario = destinatario

    def exibir(self):
        documento_pai = super().exibir()
        return f"{documento_pai}, Remetente: {self.remetente}, Destinatário: {self.destinatario}"

class Relatorio(Documento):
    def __init__(self, titulo, conteudo, data):
        super().__init__(titulo, conteudo)
        self.data = data

    def exibir(self):
        documento_pai = super().exibir()
        return f"{documento_pai}, Data: {self.data}"

documento = Documento("Documento Genérico", "Este é um documento genérico.")
email = Email("Email Importante", "Conteúdo do email", "remetente@example.com", "destinatario@example.com")
relatorio = Relatorio("Relatório Mensal", "Dados do relatório", "01/09/2023")

print(documento.exibir())
print(email.exibir())
print(relatorio.exibir())