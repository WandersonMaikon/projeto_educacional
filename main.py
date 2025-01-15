from professor import Professor
from curso import Curso

# Exemplo de uso
curso1 = Curso("Técnico em Informática", limite_horas=40, data_inicio="2025-01-27")
curso1.adicionar_disciplina("Lógica de Programação", 15)
curso1.adicionar_disciplina("Redes de Computadores", 20)

calendario = curso1.gerar_calendario()

# Exibindo o cronograma gerado
print("Cronograma de Aulas:")
for item in calendario:
    print(f"Disciplina: {item['disciplina']} | Data: {item['data']} | Horas: {item['horas']}")
