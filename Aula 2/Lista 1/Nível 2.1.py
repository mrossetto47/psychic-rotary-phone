"""
NÍVEL 2 - INTERMEDIÁRIO
-----------------------

5. MÉDIA E ACIMA
   Crie um programa que leia as notas de uma turma (quantidade indefinida). 
   O programa deve parar quando o usuário digitar -1. 
   Calcule a média da turma e mostre quantos alunos obtiveram nota acima dessa média.
"""
# Criando uma lista vazia para armazenar as notas
lista_notas = []
# Mensagem inicial ao usuário
print("Olá! Este programa irá ler as notas de uma turma. Digite -1 para encerrar a entrada de notas.")
print("Pressione Enter para continuar...")
input()  # Espera o usuário pressionar Enter

# Solicitando ao usuário que insira as notas
indice = 0
while True:
    nota = float(input("Digite a nota (ou o valor -1 para encerrar):"))
    # Checando se a nota é um número válido (0 a 10)
    if 0 <= nota <= 10:
        lista_notas.append(nota)
        indice += 1
    elif nota == -1:
        break
    else:
        print("Nota inválida. Por favor, insira uma nota entre 0 e 10.")

# Mostrando as notas registradas
print("Notas registradas:", lista_notas)
# Mensagem ao usuário sobre o cálculo da média e contagem de alunos acima da média
