import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QWidget, QVBoxLayout, QLabel, QLineEdit

class MainJanela(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("MainJanela")
        self.setGeometry(100, 100, 400, 200)

        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout()

        self.label = QLabel("Mensagens:")
        self.layout.addWidget(self.label)

        self.mensagens = []

        self.botao_nova_janela = QPushButton("Nova Janela")
        self.botao_nova_janela.clicked.connect(self.abrirNovaJanela)
        self.layout.addWidget(self.botao_nova_janela)

        self.central_widget.setLayout(self.layout)

    def abrirNovaJanela(self):
        self.nova_janela = NovaJanela(self)
        self.nova_janela.show()

    def adicionarMensagem(self, mensagem):
        self.mensagens.append(mensagem)
        self.label.setText("Mensagens:\n" + "\n".join(self.mensagens))


class NovaJanela(QWidget):
    def __init__(self, main_janela):
        super().__init__()
        self.setWindowTitle("Nova Janela")
        self.setGeometry(200, 200, 400, 150)

        self.main_janela = main_janela

        self.layout = QVBoxLayout()

        self.nome_label = QLabel("Nome:")
        self.layout.addWidget(self.nome_label)
        self.nome_input = QLineEdit()
        self.layout.addWidget(self.nome_input)

        self.mensagem_label = QLabel("Mensagem:")
        self.layout.addWidget(self.mensagem_label)
        self.mensagem_input = QLineEdit()
        self.layout.addWidget(self.mensagem_input)

        self.botao_enviar = QPushButton("Enviar")
        self.botao_enviar.clicked.connect(self.enviarMensagem)
        self.layout.addWidget(self.botao_enviar)

        self.setLayout(self.layout)

    def enviarMensagem(self):
        nome = self.nome_input.text()
        mensagem = self.mensagem_input.text()

        if nome and mensagem:
            mensagem_completa = f"{nome}: {mensagem}"
            self.main_janela.adicionarMensagem(mensagem_completa)
            self.close()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    janela = MainJanela()
    janela.show()
    sys.exit(app.exec_())
    