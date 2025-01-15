from datetime import datetime, timedelta

class Curso:
    def __init__(self, nome, limite_horas, data_inicio):
        self.nome = nome
        self.limite_horas = limite_horas
        self.disciplinas = []  # Lista de disciplinas
        self.data_inicio = datetime.strptime(data_inicio, "%Y-%m-%d")  # Converte data para datetime
        self.horas_usadas = 0

    def adicionar_disciplina(self, nome_disciplina, horas):
        """Adiciona uma disciplina ao curso, verificando o limite de horas."""
        if self.horas_usadas + horas > self.limite_horas:
            raise ValueError(
                f"Não é possível adicionar a disciplina '{nome_disciplina}'. "
                f"O total de horas ({self.horas_usadas + horas}) excede o limite do curso ({self.limite_horas})."
            )
        self.disciplinas.append({"nome": nome_disciplina, "horas": horas})
        self.horas_usadas += horas

    def gerar_calendario(self):
        """Gera o calendário com base nas disciplinas e horas."""
        calendario = []
        data_atual = self.data_inicio

        for disciplina in self.disciplinas:
            nome = disciplina["nome"]
            horas_restantes = disciplina["horas"]

            while horas_restantes > 0:
                if data_atual.weekday() < 5:  # Verifica se é um dia útil (segunda a sexta)
                    horas_no_dia = min(horas_restantes, 4)  # Máximo de 4 horas por dia
                    calendario.append(
                        {"disciplina": nome, "data": data_atual.strftime("%Y-%m-%d"), "horas": horas_no_dia}
                    )
                    horas_restantes -= horas_no_dia
                data_atual += timedelta(days=1)  # Avança para o próximo dia

        return calendario

    def __str__(self):
        disciplinas_str = "\n".join(
            [f"  - {d['nome']}: {d['horas']} horas" for d in self.disciplinas]
        ) if self.disciplinas else "Nenhuma"
        return (
            f"Curso: {self.nome} (Limite de Horas: {self.limite_horas}, Início: {self.data_inicio.strftime('%Y-%m-%d')})\n"
            f"Disciplinas:\n{disciplinas_str}\nHoras totais utilizadas: {self.horas_usadas}/{self.limite_horas}"
        )
