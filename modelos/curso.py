from datetime import datetime, timedelta
class Feriados:
    """Gerencia os feriados do ano."""
    def __init__(self):
        self.feriados = set()

    def adicionar_feriado(self, data_feriado):
        """Adiciona um feriado à lista. Aceita strings no formato YYYY-MM-DD."""
        self.feriados.add(datetime.strptime(data_feriado, "%Y-%m-%d").date())

    def eh_feriado(self, data):
        """Verifica se uma data (datetime.date) é um feriado."""
        return data in self.feriados

class Curso:
    """Representa um curso com disciplinas, professores e calendário gerado."""

    def __init__(self, nome, limite_horas, data_inicio, feriados):
        self.nome = nome  # Nome do curso
        self.limite_horas = limite_horas  # Limite de horas para o curso
        self.disciplinas = []  # Lista de disciplinas
        self.professores = []  # Lista de professores associados ao curso
        self.data_inicio = datetime.strptime(data_inicio, "%Y-%m-%d")  # Data de início do curso
        self.horas_usadas = 0  # Controle de horas já alocadas
        self.feriados = feriados  # Instância da classe Feriados

    def adicionar_disciplina(self, nome_disciplina, horas):
        """
        Adiciona uma disciplina ao curso, verificando o limite de horas.
        """
        if self.horas_usadas + horas > self.limite_horas:
            raise ValueError(
                f"Não é possível adicionar a disciplina '{nome_disciplina}'. "
                f"O total de horas ({self.horas_usadas + horas}) excede o limite do curso ({self.limite_horas})."
            )
        self.disciplinas.append({"nome": nome_disciplina, "horas": horas})
        self.horas_usadas += horas

    def adicionar_professor(self, professor):
        """
        Adiciona um professor ao curso e vincula o curso ao professor.
        """
        self.professores.append(professor)
        professor.adicionar_curso(self)  # Vincula o curso ao professor

    def gerar_calendario(self):
        """
        Gera o calendário do curso com base nas disciplinas, horas, feriados e dias úteis.
        Se sobrar tempo em um dia, ele é usado para a próxima disciplina.
        """
        calendario = []
        data_atual = self.data_inicio
        horas_disponiveis_no_dia = 4  # Quantidade fixa de horas por dia

        for disciplina in self.disciplinas:
            nome = disciplina["nome"]
            horas_restantes = disciplina["horas"]

            while horas_restantes > 0:
                # Verifica se o dia é útil (segunda a sexta) e não é feriado
                if data_atual.weekday() < 5 and not self.feriados.eh_feriado(data_atual.date()):
                    if horas_disponiveis_no_dia > 0:  # Há tempo no dia para alocar horas
                        horas_no_dia = min(horas_restantes, horas_disponiveis_no_dia)
                        calendario.append(
                            {"disciplina": nome, "data": data_atual.strftime("%Y-%m-%d"), "horas": horas_no_dia}
                        )
                        horas_restantes -= horas_no_dia
                        horas_disponiveis_no_dia -= horas_no_dia
                    else:
                        # Dia está cheio, passar para o próximo
                        data_atual += timedelta(days=1)
                        horas_disponiveis_no_dia = 4
                else:
                    # Se for fim de semana ou feriado, passa para o próximo dia útil
                    data_atual += timedelta(days=1)
                    horas_disponiveis_no_dia = 4

        return calendario

    def __str__(self):
        """
        Retorna uma representação amigável do curso, incluindo disciplinas e professores.
        """
        professores_str = ", ".join([prof.nome for prof in self.professores]) if self.professores else "Nenhum"
        disciplinas_str = "\n".join(
            [f"  - {d['nome']}: {d['horas']} horas" for d in self.disciplinas]
        ) if self.disciplinas else "Nenhuma"
        return (
            f"Curso: {self.nome} (Limite de Horas: {self.limite_horas}, Início: {self.data_inicio.strftime('%Y-%m-%d')})\n"
            f"Disciplinas:\n{disciplinas_str}\n"
            f"Professores: {professores_str}\n"
            f"Horas totais utilizadas: {self.horas_usadas}/{self.limite_horas}"
        )
