class Professor:
    def __init__(self, nome, matricula):
        self.nome = nome
        self.matricula = matricula
        self.cursos = []  # Lista de cursos ministrados pelo professor

    def adicionar_curso(self, curso):
        """Adiciona um curso à lista de cursos ministrados pelo professor."""
        self.cursos.append(curso)

    def __str__(self):
        cursos_str = ", ".join([curso.nome for curso in self.cursos]) if self.cursos else "Nenhum"
        return f"Professor: {self.nome} (Matrícula: {self.matricula})\nCursos: {cursos_str}"

