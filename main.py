from professor import Professor
from curso import Curso, Feriados

# Criando feriados
feriados = Feriados()
feriados.adicionar_feriado("2025-01-20")  # Feriado exemplo
feriados.adicionar_feriado("2025-01-25")  # Feriado exemplo

# Criando professores
professor1 = Professor("Wanderson", 2345)
professor2 = Professor("Ana", 6789)

# Criando cursos
curso1 = Curso("Técnico em Informática", limite_horas=40, data_inicio="2025-01-15", feriados=feriados)
curso1.adicionar_disciplina("Sistemas operacionais", 15)
curso1.adicionar_disciplina("Redes de Computadores", 20)

curso2 = Curso("Lógica de programação", limite_horas=30, data_inicio="2025-02-01", feriados=feriados)
curso2.adicionar_disciplina("Protocolos de Rede", 20)

# Associando professores aos cursos
curso1.adicionar_professor(professor1)
curso2.adicionar_professor(professor2)

# Gerando calendário de um curso
calendario_1 = curso1.gerar_calendario()
calendario_2 = curso2.gerar_calendario()
print("Cronograma de Aulas do Curso 1:")
print("\nInformações dos Professores:")
print(professor1)
for item in calendario_1:
    print(f"Disciplina: {item['disciplina']} | Data: {item['data']} | Horas: {item['horas']}")

# Exibindo os cursos ministrados pelos professores
print("\nInformações dos Professores:")
print(professor2)
for item in calendario_2:
    print(f"Disciplina: {item['disciplina']} | Data: {item['data']} | Horas: {item['horas']}")
