#ARQUIVO: README.md - PROJETO-AVALIACÃO_REGIMENTAL-A1
##Projeto de fundamentos em pytons  — Avaliação A1

Repositório destinado à Avaliação A1 da disciplina Técnicas de Desenvolvimento de Algoritmos, com foco em Estruturas Condicionais, Estruturas de Repetição, Listas e Dicionários, desenvolvidas por meio de atividades práticas durante o curso. (README.md)

# ARQUIVO: if_elif_else.py - Estruturas Condicionais
##  Sistema de Verificação de Idade para Eventos

Este programa realiza a verificação da idade informada pelo usuário para determinar se a entrada em um evento é permitida ou não.

  - Como funciona o programa

O sistema solicita que o usuário digite a idade e, com base no valor informado, utiliza **estruturas condicionais (if/elif/else)** para decidir o tipo de acesso ao evento:

 Idade - Resultado 
 Menor que 12 anos : ❌ Entrada não permitida 
 Entre 12 e 17 anos : ⚠️ Entrada permitida somente com responsável 
18 anos ou mais : ✅ Entrada totalmente liberada 

Ao final, o programa exibe uma mensagem de agradecimento ao usuário.

   - Como executar

1. Certifique-se de ter o **Python 3.x** instalado no seu computador.
2. Salve o código em um arquivo com o nome:  
    `verificacao_idade.py`
3. Execute no terminal ou prompt de comando com:

(if_elif_else.py)
# ARQUIVO: for_while.py - Estruturas de Repetição
## 🧩 Contador de Números Pares (FOR e WHILE)

Este programa exibe apenas os números pares entre 1 e 100, utilizando duas estruturas de repetição:

FOR → percorre os números automaticamente dentro do intervalo

WHILE → conta manualmente até atingir o limite

Para identificar se o número é par, o programa verifica se o resultado da divisão por 2 tem resto igual a zero (numero % 2 == 0).

Ambas as estruturas geram o mesmo resultado final, apenas com maneiras diferentes de repetir o código.

▶️ Como executar o programa

Salve o arquivo com o nome contador_pares.py

Execute no terminal ou CMD com o comando:

python contador_pares.py

🖨️ Resultado esperado

O programa vai imprimir apenas números pares:

2
4
6
8
...
98
100
 # ARQUIVO: lista.py - Lista
 ## Cadastro de Alunos com Listas em Python

Este programa permite cadastrar nomes de alunos em uma lista utilizando um loop while.
O usuário pode adicionar quantos nomes quiser e, quando desejar encerrar o cadastro, basta digitar "sair".

🔹 Como funciona o programa:

O programa começa com uma lista vazia chamada alunos.

Cada nome digitado é adicionado à lista.

Quando o usuário digita "sair", o loop é interrompido.

No final, todos os alunos cadastrados são exibidos na tela.

🧠 Recursos utilizados:

Listas

Laço de repetição while

Condicional if

Método .append()

Função input()
 # ARQUIVO: dicionários.py - Dicionários
 ## Sistema de Cadastro de Produtos com Dicionário

Este programa permite cadastrar produtos com seus respectivos preços e armazená-los em um dicionário no Python.
O usuário pode cadastrar vários produtos e encerrar a qualquer momento digitando "sair".

Cada produto é salvo como:

Chave → nome do produto

Valor → preço do produto

Ao finalizar o cadastro, o sistema exibe todos os produtos inseridos.
▶️ Como executar o programa

1️⃣ Salve o arquivo com o nome:

cadastro_produtos.py


2️⃣ Execute o script no terminal ou CMD com:

python cadastro_produtos.py

📝 Exemplo de uso

Entrada do usuário:

Digite o nome do produto (ou 'sair' para encerrar): Arroz
Digite o preço do produto: R$ 7.50
Digite o nome do produto (ou 'sair' para encerrar): Feijão
Digite o preço do produto: R$ 8.20
Digite o nome do produto (ou 'sair' para encerrar): sair


Saída exibida:

Lista de produtos cadastrados:
- Arroz: R$ 7.50
- Feijão: R$ 8.20

 
