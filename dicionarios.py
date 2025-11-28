# Sistema simples de cadastro de produtos usando dicionário

produtos = {}  # Dicionário para armazenar produtos

while True:
    nome = input("Digite o nome do produto (ou 'sair' para encerrar): ")

    if nome.lower() == "sair":
        break

    preco = float(input("Digite o preço do produto: R$ "))

    produtos[nome] = preco  # Armazena no dicionário

print("\n Lista de produtos cadastrados:")
for nome, preco in produtos.items():
    print(f"- {nome}: R$ {preco:.2f}")
