"""LISTA DE EXERCÍCIOS - PYTHON (TEMA: LISTAS)
=============================================

NÍVEL 1 - INICIANTE
-------------------

1. SOMA DOS ELEMENTOS
   Escreva um programa que crie uma lista com 5 números inteiros fornecidos pelo usuário 
   e exiba a soma de todos os elementos."""

# Criando uma lista vazia para armazenar os números
lista_numeros = []

# Solicitando ao usuário que insira 5 números inteiros
for indice in range(5):
# Solicitando o número ao usuário e utilizando o indice na string para indicar qual número está sendo solicitado
#numero deve ser convertido para inteiro
    numero = int(input("Digite o " + str(indice + 1) + "º número inteiro: "))
#Adicionando o número à lista
    lista_numeros.append(numero)
# Calculando a soma dos elementos da lista
soma = lista_numeros[0] + lista_numeros[1] + lista_numeros[2] + lista_numeros[3] + lista_numeros[4]   
#Printar a soma dos elementos
print("A soma dos números é:", soma)
    
##########################################################################################################################               
 