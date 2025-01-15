class Professor:
    def __init__(self, nome, matricula, curso, hora_curso):
        self.nome = nome
        self.matricula = matricula
        self.curso = curso
        self.hora_curso = hora_curso  # Limite de horas para o curso
        self.disciplinas = []  # Lista para armazenar disciplinas como pares (nome, horas)
        self.horas_usadas = 0  # Controle das horas já alocadas no curso

    def adicionar_disciplina(self, disciplina, hora_disciplina):
        """
        Adiciona uma disciplina ao professor, respeitando o limite de horas do curso.
        """
        if self.horas_usadas + hora_disciplina > self.hora_curso:
            raise ValueError(
                f"Não é possível adicionar a disciplina '{disciplina}'. "
                f"O total de horas ({self.horas_usadas + hora_disciplina}) excede o limite do curso ({self.hora_curso})."
            )

        self.disciplinas.append({"nome": disciplina, "horas": hora_disciplina})
        self.horas_usadas += hora_disciplina

    def __str__(self):
        if not self.disciplinas:
            disciplinas_str = "Nenhuma"
        else:
            disciplinas_str = "\n".join(
                [f"  - {d['nome']}: {d['horas']} horas" for d in self.disciplinas]
            )

        return (
            f"Professor: {self.nome} (Matrícula: {self.matricula}, Curso: {self.curso})\n"
            f"Disciplinas:\n{disciplinas_str}\n"
            f"Horas totais utilizadas: {self.horas_usadas}/{self.hora_curso}"
        )


# Criando um professor e adicionando curso
professor = Professor("Wanderson", 2345, "Técnico em Informática", hora_curso=40)

# Adicionando disciplinas
try:
    professor.adicionar_disciplina("Lógica de Programação", 0)
    professor.adicionar_disciplina("Redes de Computadores", 20)
    professor.adicionar_disciplina("Segurança da Informação", 10)
except ValueError as e:
    print(e)

# Exibindo o professor
print(professor)