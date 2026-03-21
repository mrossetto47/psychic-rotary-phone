"""LISTA DE EXERCÍCIOS - PYTHON (TEMA: DICIONÁRIOS)
=================================================

NÍVEL 1 - INICIANTE
-------------------

2. CONTAGEM DE CARACTERES
   Escreva um programa que receba uma palavra ou frase do usuário e crie um dicionário
   onde cada chave é uma letra e cada valor é o número de vezes que essa letra aparece.
   Considere apenas letras (ignore espaços e diferenças entre maiúsculas/minúsculas).
"""
# Mensagem inicial ao usuario
print("Olá! Este programa lerá uma palavra ou frase fornecida por você e contará quantas vezes cada letra aparece.\n"
      "Pressione Enter para continuar...")
input()  # Espera o usuário pressionar Enter

# Criando dicionário para armazenar a contagem de caracteres
contagem = {}

# Lendo a palavra ou frase do usuário
entrada = input("Digite uma palavra ou frase para contar os caracteres: ")

# Vamos processar a entrada do usuário
# Devemos verificar caractere por caractere, ignorar espaços e case (caps)
# Para isso, vamos precisar de um looṕ 

