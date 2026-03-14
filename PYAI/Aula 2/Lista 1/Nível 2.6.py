"""LISTA DE EXERCÍCIOS - PYTHON (TEMA: LISTAS)
=============================================

NÍVEL 2 - INTERMEDIÁRIO
-----------------------

6. REMOVENO DUPLICATAS
   Desenvolva um programa que receba uma lista de números inteiros (pode ter valores repetidos) 
   e crie uma nova lista apenas com os valores únicos, mantendo a ordem de primeira aparição.
   """

# Mensagem inicial ao usuário
print("Olá! Este programa irá ler uma lista de números inteiros e remover os duplicados, mantendo a ordem de primeira aparição.")
print("Pressione Enter para continuar...")
input()  # Espera o usuário pressionar Enter

# Criando lista vazia
lista_usuario = []

# Recebendo lista de valores inteiros
# O comando split() "quebra" a entrada sempre que há um espaço
lista_usuario = input("Digite uma lista de números separados por um espaço:").split()

# Mensagem ao Usuário
print("A lista digitada foi:", lista_usuario,"\n")
print("Agora, vamos fazer a limpeza!")
print("Pressione Enter para continuar...")
input()  # Espera o usuário pressionar Enter

# Vamos encontrar as ocorrências duplicadas e remover as ocorrências depois da primeira
lista_unica = []  # Lista para armazenar os valores únicos
for numero in lista_usuario:
    if numero not in lista_unica:  # Verifica se o número já está na lista de únicos
        lista_unica.append(numero)  # Se não estiver, adiciona à lista de únicos

# Mensagem ao Usuário
print("A lista organizada é a seguinte:", lista_unica)

############################################################################################################