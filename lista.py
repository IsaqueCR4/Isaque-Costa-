# Programa para cadastrar nomes de alunos em uma lista

alunos = []  # Lista vazia para armazenar os nomes

while True:
    nome = input("Digite o nome do aluno (ou 'sair' para encerrar): ")
    
    if nome.lower() == "sair":  # Condição para parar o programa
        break
    
    alunos.append(nome)  # Adiciona o nome à lista

print("\nLista de alunos cadastrados:")
for aluno in alunos:
    print(f"- {aluno}")
