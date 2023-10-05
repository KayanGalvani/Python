class Curso:
    def __init__(self, nome, duracao):
        self.nome = nome
        self.duracao = duracao

    def detalhes_do_curso(self):
        return f"Curso: {self.nome}, Duração: {self.duracao} anos"


class Presencial(Curso):
    def __init__(self, nome, duracao, numero_de_vagas):
        super().__init__(nome, duracao)
        self.numero_de_vagas = numero_de_vagas

    def detalhes_do_curso(self):
        curso_base = super().detalhes_do_curso()
        return f"{curso_base}, Vagas: {self.numero_de_vagas}"


class Online(Curso):
    def __init__(self, nome, duracao, plataforma_online):
        super().__init__(nome, duracao)
        self.plataforma_online = plataforma_online

    def detalhes_do_curso(self):
        curso_base = super().detalhes_do_curso()
        return f"{curso_base}, Plataforma Online: {self.plataforma_online}"


curso_presencial = Presencial("Curso Presencial", 2, 30)
curso_online = Online("Curso Online", 1.5, "Plataforma X")

print(curso_presencial.detalhes_do_curso())
print(curso_online.detalhes_do_curso())