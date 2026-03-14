"""LISTA DE EXERCÍCIOS - PYTHON (TEMA: LISTAS)
=============================================

NÍVEL 1 - INICIANTE
-------------------
3. CONTAGEM DE PARES
   Faça um programa que gere uma lista com 10 números aleatórios entre 1 e 100 
   e mostre quantos deles são pares. """

import random

#Mensagem inicial ao usuário
print("Olá! Este programa irá gerar uma lista com 10 números aleatórios entre 1 e 100 e contar quantos deles são pares.")
print("Pressione Enter para continuar...")
input()  # Espera o usuário pressionar Enter   

# Gerando uma lista com 10 números aleatórios entre 1 e 100
print("Gerando números aleatórios...")
lista_random =[]
for indice in range(10):
    numero_aleatorio = random.randint(1, 100)
    lista_random.append(numero_aleatorio)
print("Números gerados:", lista_random)

#Mensagem ao usuário sobre a contagem de números pares
print("Agora, vamos contar quantos desses números são pares...")
print("Pressione Enter para continuar...")
input()  # Espera o usuário pressionar Enter   

#Verificando se um número é par utilizando o operador de módulo (%)
contador_pares = 0
indice=0
for indice in lista_random:
    if indice % 2 == 0:
        contador_pares += 1
print("Quantidade de números pares:", contador_pares)
###################################################################################################