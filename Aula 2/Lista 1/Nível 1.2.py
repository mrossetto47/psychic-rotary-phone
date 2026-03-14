"""LISTA DE EXERCÍCIOS - PYTHON (TEMA: LISTAS)
=============================================

NÍVEL 1 - INICIANTE
-------------------

2. MAIOR E MENOR VALOR
   Crie um programa que leia 7 números inteiros, armazene-os em uma lista e mostre 
   o maior e o menor valor digitados, juntamente com suas respectivas posições."""

# Criando uma lista vazia para armazenar os números
lista_numeros = []

# Solicitando ao usuário que insira 7 números inteiros
for indice in range(7):
# Solicitando o número ao usuário e utilizando o indice na string para indicar qual número está sendo solicitado
#numero deve ser convertido para inteiro
    numero = int(input("Digite o " + str(indice + 1) + "º número inteiro: "))
#Adicionando o número à lista
    lista_numeros.append(numero)

# Encontrando o maior e o menor valor na lista
maior_valor = max(lista_numeros)
menor_valor = min(lista_numeros)

# Encontrando as posições do maior valor
posicao_maior = lista_numeros.index(maior_valor)

#Verificar se tem números repetidos para o maior valor
if lista_numeros.count(maior_valor) > 1:
    print("Existe mais de um número com o valor máximo:", maior_valor)
else:
    # Printar o maior e menor valor juntamente com suas respectivas posições
    print("O maior valor digitado é:", maior_valor, "na posição", posicao_maior)

# Encontrando as posições do menor valor
posicao_menor = lista_numeros.index(menor_valor)
#Verificar se tem números repetidos para o menor valor
if lista_numeros.count(menor_valor) > 1:
    print("Existe mais de um número com o valor mínimo:", menor_valor)
else:
    print("O menor valor digitado é:", menor_valor, "na posição", posicao_menor)
#################################################################################################